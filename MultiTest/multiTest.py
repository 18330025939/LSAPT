import json
import datetime
import os
import shutil
import threading

from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from Lib.console import SerialPort
from Lib.item import TableWidgetIO, TestItems
from Lib.logger import TestLogger
from Lib.ui import UI
from MultiTest.ui_multiTest import Ui_MultiTest
from PyQt5.QtCore import Qt, pyqtSignal, QEventLoop, QTimer


class MultiTestWindow(QWidget):
    notify_signal = pyqtSignal(str)

    def __init__(self, form):
        super().__init__()
        self.form = form
        self.ui = Ui_MultiTest()
        self.ui.setupUi(self.form)
        # self.form.show()
        self.pid_sid_len = 16
        self.current_dir = None
        self.table_file_path = None

        self.test_instr = None
        self.show_info = None
        self.test_passed = None
        self.test_failed = None
        self.test_image_path = None
        self.test_timeout = None
        self.test_skip = None

        self.platform_name = None
        self.dst_dir = None

        self.test_log = TestLogger()
        self.test_progress_log = TestLogger()

        self.serial = SerialPort()

        self.serial_link = False
        self.thread = threading.Thread(target=self.thread_function)
        self.running = False
        self.pause_event = threading.Event()
        self.handle_event = threading.Event()

        self.time = QTimer()
        self.time.timeout.connect(self.thread_finished)
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.command_timeout)

        self.current_row = 0
        self.rows = 0
        self.columns = self.ui.tableWidget.columnCount()
        self.table = self.ui.tableWidget

        self.testTable = TestItems(self.ui.tableWidget)
        self.testTable_header = []

        self.form.closeEvent = self.on_close
        self.ui.btnRetry.clicked.connect(self.retry_test)
        self.ui.btnStop.clicked.connect(self.stop_test)
        self.ui.btnContinue.clicked.connect(self.continue_test)
        self.ui.btnOpen.clicked.connect(self.open_test_file)
        # self.ui.btnSave.clicked.connect(self.save_text_log)
        self.ui.btnSerialConnect.clicked.connect(self.serial_connect)
        self.ui.btnSerialDisconnect.clicked.connect(self.serial_disconnect)

    def on_close(self, event):
        self.form.hide()

    def continue_test(self):
        self.pause_event.set()

    def stop_test(self):
        self.pause_event.clear()

    def set_label_image(self, image_path):
        if os.path.exists(image_path) and os.path.isfile(image_path):
            pixmap = QPixmap(image_path)
            scaled_pixmap = pixmap.scaled(self.ui.labelImage.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.labelImage.setPixmap(scaled_pixmap)
            self.ui.labelImage.setAlignment(Qt.AlignCenter)
            mes_box = QMessageBox()
            mes_box.setIcon(QMessageBox.Information)
            mes_box.setText("请根据照片判断是否测试通过！")
            mes_box.setWindowTitle('提示')
            mes_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            yes_button = mes_box.button(QMessageBox.Yes)
            yes_button.setText('通过')
            no_button = mes_box.button(QMessageBox.No)
            no_button.setText('不通过')
            result = mes_box.exec_()
            if result == QMessageBox.Yes:
                return True
            elif result == QMessageBox.No:
                return False

    def handle_test_result(self, message):
        # received_data = f'Received data: {message}'
        self.test_progress_log.add_data('Received data:')
        self.test_progress_log.add_data(message)
        current_time = datetime.datetime.now().time().strftime('%H:%M:%S')
        self.testTable.set_item(self.current_row, self.testTable_header.index('EndTime'), current_time)
        if os.path.exists(self.test_image_path) and os.path.isfile(self.test_image_path):
            if not self.set_label_image(self.test_image_path):
                self.show_info = '不通过'
            else:
                self.show_info = message
            self.ui.labelImage.setText("无照片")
        if self.show_info in message:
            self.testTable.set_item(self.current_row, self.testTable_header.index('Result'), "Passed")
            self.testTable.set_item(self.current_row, self.testTable_header.index('Msg'), self.test_passed)
            self.testTable.set_row_background(self.current_row, Qt.green)
            self.ui.labelPassNumber.setText(str(int(self.ui.labelPassNumber.text()) + 1))
        elif 'Timeout' in message:
            self.testTable.set_item(self.current_row, self.testTable_header.index('Result'), "Timeout")
            self.testTable.set_row_background(self.current_row, QColor("red"))
            self.ui.labelFailNumber.setText(str(int(self.ui.labelFailNumber.text()) + 1))
        else:
            self.testTable.set_item(self.current_row, self.testTable_header.index('Result'), "Failed")
            self.testTable.set_item(self.current_row, self.testTable_header.index('Msg'), self.test_failed)
            self.testTable.set_row_background(self.current_row, QColor("red"))
            self.ui.labelFailNumber.setText(str(int(self.ui.labelFailNumber.text()) + 1))

        self.ui.labelTotalNumber.setText(str(int(self.ui.labelTotalNumber.text()) + 1))
        self.handle_event.set()
        # self.serial_flag = True

    def thread_function(self):
        while self.running:
            if self.current_row >= self.rows:
                break
            self.pause_event.wait()
            # print(self.current_row, self.testTable_header.index('TestItem'))
            test_name = self.table.item(self.current_row, self.testTable_header.index('TestItem')).text()
            if test_name is None:
                self.current_row += 1
                continue
            if not self.analysis_test_script(test_name):
                self.ui.labelTotalNumber.setText(str(int(self.ui.labelTotalNumber.text()) + 1))
                self.ui.labelSkipNumber.setText(str(int(self.ui.labelSkipNumber.text()) + 1))
                continue
            # print(self.test_instr, self.test_timeout)
            # 先不考虑多行的测试指令
            self.serial.send_command(self.test_instr, self.test_timeout)
            # if int(self.test_timeout) > 0:
            #     self.timer.start(int(self.test_timeout) * 1000)
            self.handle_event.clear()
            self.testTable.set_item(self.current_row, self.testTable_header.index('Result'), 'Running')
            current_date = datetime.datetime.now().strftime('%Y/%m/%d')
            self.testTable.set_item(self.current_row, self.testTable_header.index('Date'), current_date)
            current_time = datetime.datetime.now().time().strftime('%H:%M:%S')
            self.testTable.set_item(self.current_row, self.testTable_header.index('StartTime'), current_time)
            self.handle_event.wait()
            # self.timer.stop()
            self.current_row += 1

    # def command_timeout(self):
    #     print('timeout')
    #     self.timer.stop()

    def set_sid_pid(self):
        self.ui.editSID.clear()
        event_loop = QEventLoop()
        self.ui.editSID.returnPressed.connect(event_loop.quit)
        self.ui.editSID.setFocus(Qt.PopupFocusReason)
        event_loop.exec_()
        self.ui.editOPID.clear()
        event_loop = QEventLoop()
        self.ui.editOPID.returnPressed.connect(event_loop.quit)
        self.ui.editOPID.setFocus(Qt.PopupFocusReason)
        event_loop.exec_()

    def thread_finished(self):
        if self.running and self.current_row >= self.rows and not self.thread.is_alive():
            self.time.stop()
            self.ui.labelTestNumber.setText(str(int(self.ui.labelTestNumber.text()) + 1))
            self.save_text_log()
            mes_box = QMessageBox()
            mes_box.setIcon(QMessageBox.Information)
            mes_box.setText("测试完成，请进行下一步操作！")
            mes_box.setWindowTitle('提示')
            mes_box.setStandardButtons(QMessageBox.Abort)
            continue_button = mes_box.addButton('继续', QMessageBox.YesRole)
            abort_button = mes_box.button(QMessageBox.Abort)
            abort_button.setText('中止')
            mes_box.setDefaultButton(QMessageBox.Abort)
            result = mes_box.exec()
            clicked_button = mes_box.clickedButton()
            if clicked_button == mes_box.button(QMessageBox.Abort):
                pass
            elif clicked_button == continue_button:
                self.retry_test()

    def thread_start(self):
        if self.serial_link:
            self.running = False
            self.current_row = 0
            # time.sleep(1)
            self.running = True
            self.pause_event.set()
            self.handle_event.set()
            self.thread = threading.Thread(target=self.thread_function)
            self.thread.start()
            self.time.start(1000)
        else:
            mes_box = QMessageBox()
            mes_box.setIcon(QMessageBox.Warning)
            mes_box.setText("串口未连接！")
            mes_box.setWindowTitle('警告')
            mes_box.exec_()

    def retry_test(self):
        self.set_sid_pid()
        new_dir = os.path.join(self.current_dir, self.platform_name + '_' + self.ui.editSID.text())
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        if os.path.exists(new_dir):
            file_path = os.path.join(str(new_dir), UI.testProcessLog)
            self.test_progress_log.select_file(file_path)
        self.import_table_widget(self.table_file_path)
        self.thread_start()

    def analysis_test_script(self, name):
        file_path = os.path.join(self.current_dir, name + '.json').replace('\\', '/')
        with open(file_path, 'r') as file:
            data = json.load(file)

            for key, value in data.items():
                if key == UI.configWin.get_test_instr_object_name():
                    self.test_instr = value
                    self.test_progress_log.add_data('Sent data:')
                    self.test_progress_log.add_data(value)
                elif key == UI.configWin.get_show_info_object_name():
                    self.show_info = value
                elif key == UI.configWin.get_test_pass_object_name():
                    self.test_passed = value
                elif key == UI.configWin.get_test_fail_object_name():
                    self.test_failed = value
                elif key == UI.configWin.get_image_path_object_name():
                    self.test_image_path = value
                elif key == UI.configWin.get_timeout_object_name():
                    self.test_timeout = value
                elif key == UI.configWin.get_test_skip_object_name():
                    self.test_skip = value

        if self.test_skip:
            return False
        return True

    def import_table_widget(self, file_path):
        # self.rows = TableWidgetIO.import_table_widget(self.ui.tableWidget, file_path)
        if self.running and self.current_row != 0:
            for row in range(self.rows):
                self.testTable.set_row_background(row, QColor('white'))
                for col in range(self.testTable_header.index('Result'), self.columns):
                    item = self.ui.tableWidget.item(row, col)
                    if item and item.text().strip():
                        item.setText('')
            self.ui.labelTotalNumber.setText('0')
            self.ui.labelSkipNumber.setText('0')
            self.ui.labelPassNumber.setText('0')
            self.ui.labelFailNumber.setText('0')
            self.ui.editTestInfor.clear()
        else:
            self.rows = TableWidgetIO.import_table_widget(self.ui.tableWidget, file_path)

    def open_test_file(self):
        file_path, _ = QFileDialog().getOpenFileName(None, "打开文件", "", "JSON Files (" + UI.testItemsPlatFile + ")")
        if file_path:
            self.import_table_widget(file_path)
            if not self.rows:
                mes_box = QMessageBox()
                mes_box.setIcon(QMessageBox.Warning)
                mes_box.setText("文件打开失败，请检查文件格式或内容！")
                mes_box.setWindowTitle('警告')
                mes_box.exec_()
                return False
            self.current_dir = os.path.dirname(file_path)
            self.table_file_path = file_path
            self.ui.labelTestFile.setText(os.path.basename(file_path))
            for col in range(self.columns):
                header_item = self.table.horizontalHeaderItem(col)
                if header_item is not None:
                    self.testTable_header.append(header_item.text())
            temp_path = os.path.join(self.current_dir, UI.platformInfoFile)
            if os.path.exists(temp_path):
                with open(temp_path, 'r') as file:
                    data = json.load(file)
                for key, value in data.items():
                    if key == UI.platWin.get_hw_platform_object_name():
                        self.platform_name = value
                        self.ui.labelModel.setText(value)
                    elif key == UI.platWin.get_hw_version_object_name():
                        self.ui.labelVersion.setText(value)
                    elif key == UI.platWin.get_hw_mode_object_name():
                        self.ui.labelMode.setText(value)
                    elif key == 'ftpServer':
                        for k, v in value.items():
                            if k == UI.platWin.get_ftp_path_object_name():
                                self.dst_dir = v

    def save_test_parameters(self):
        if self.test_log is not None:
            self.test_log.add_data(self.ui.labelModel.objectName().replace('label', '') + '=' + self.ui.labelModel.text())
            self.test_log.add_data(self.ui.labelTestFile.objectName().replace('label', '') + '=' + self.ui.labelTestFile.text())
            self.test_log.add_data(self.ui.labelVersion.objectName().replace('label', '') + '=' + self.ui.labelVersion.text())
            self.test_log.add_data(self.ui.labelMode.objectName().replace('label', '') + '=' + self.ui.labelMode.text())
            self.test_log.add_data(self.ui.editSID.objectName().replace('edit', '') + '=' + self.ui.editSID.text())
            self.test_log.add_data(self.ui.editOPID.objectName().replace('edit', '') + '=' + self.ui.editOPID.text())
            self.test_log.add_data(self.ui.labelTotalNumber.objectName().replace('label', '') + '=' + self.ui.labelTotalNumber.text())
            self.test_log.add_data(self.ui.labelPassNumber.objectName().replace('label', '') + '=' + self.ui.labelPassNumber.text())
            self.test_log.add_data(self.ui.labelFailNumber.objectName().replace('label', '') + '=' + self.ui.labelFailNumber.text())
            self.test_log.add_data(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def save_text_log(self):
        new_dir = os.path.join(self.current_dir, self.platform_name + '_' + self.ui.editSID.text()).replace('\\', '/')
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        if os.path.exists(new_dir):
            file_path = os.path.join(str(new_dir), str(UI.testResultLog))
            if self.test_log.select_file(file_path):
                self.save_test_parameters()
                self.test_log.add_separator()
                self.test_log.add_table_header(self.ui.tableWidget)
                self.test_log.add_separator()
                self.test_log.add_table_data(self.ui.tableWidget)

            tmp_dir = os.path.join(self.dst_dir, self.platform_name + '_' + self.ui.editSID.text()).replace('\\', '/')
            if os.path.exists(tmp_dir):
                for root, dirs, files in os.walk(str(tmp_dir), topdown=False):
                    for file in files:
                        file_path = os.path.join(root, file)
                        os.remove(file_path)
                os.rmdir(tmp_dir)
            if os.path.exists(self.dst_dir):
                shutil.move(str(new_dir), self.dst_dir)

    def serial_connect(self):
        port_name = self.ui.boxSerialSelect.currentText()
        baud_rate = self.ui.boxBaudSelect.currentText()

        if self.serial.open(port_name, baud_rate) is True:
            self.serial.data_received.connect(self.handle_serial_data)
            self.notify_signal.connect(self.handle_test_result)
            self.serial_link = True
            mes_box = QMessageBox()
            mes_box.setIcon(QMessageBox.Information)
            mes_box.setText("串口连接成功！")
            mes_box.setWindowTitle('提示')
            mes_box.exec_()
        else:
            mes_box = QMessageBox()
            mes_box.setIcon(QMessageBox.Warning)
            mes_box.setText("串口连接失败,请检查串口是否正确连接！")
            mes_box.setWindowTitle('警告')
            mes_box.exec_()

    def serial_disconnect(self):
        self.serial.close()
        self.serial_link = False
        mes_box = QMessageBox()
        mes_box.setIcon(QMessageBox.Information)
        mes_box.setText("串口已断开！")
        mes_box.setWindowTitle('提示')
        mes_box.exec_()

    def handle_serial_data(self, data):
        # print('data', data)
        self.ui.editTestInfor.append(data)
        self.notify_signal.emit(data)
