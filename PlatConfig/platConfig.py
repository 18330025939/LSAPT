import json
import os
from PyQt5.QtWidgets import QWidget, QMessageBox
from Lib.ui import UI
from PlatConfig.ui_platConfig import Ui_PlatConfig


class PlatConfigWindow(QWidget):
    def __init__(self, form):
        super().__init__()
        self.form = form
        self.ui = Ui_PlatConfig()
        self.ui.setupUi(self.form)
        # self.form.show()
        self.platform_dir = None
        self.form.closeEvent = self.on_close

    def on_close(self, event):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle('保存配置')
        msg_box.setText('是否保存更改?')
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        yes_button = msg_box.button(QMessageBox.Yes)
        yes_button.setText('保存')
        no_button = msg_box.button(QMessageBox.No)
        no_button.setText('不保存')
        cancel_button = msg_box.button(QMessageBox.Cancel)
        cancel_button.setText('取消')
        reply = msg_box.exec_()
        if reply == QMessageBox.Yes:
            self.save_platform_info()
            event.accept()
            self.form.hide()
        elif reply == QMessageBox.No:
            event.accept()
            self.form.hide()
        else:
            event.ignore()

    def hw_platform_info(self):
        data = {}
        data.setdefault(self.ui.editHwPlatform.objectName(), self.ui.editHwPlatform.text())
        data.setdefault(self.ui.editHwVersion.objectName(), self.ui.editHwVersion.text())
        data.setdefault(self.ui.editHwMode.objectName(), self.ui.editHwMode.text())
        return data

    def sw_system_info(self):
        data = {'system': {}}
        data['system'].setdefault(self.ui.editSysLogin.objectName(), self.ui.editSysLogin.text())
        data['system'].setdefault(self.ui.editSysPassword.objectName(), self.ui.editSysPassword.text())
        data['system'].setdefault(self.ui.editSysStartTimeout.objectName(), self.ui.editSysStartTimeout.text())
        data['system'].setdefault(self.ui.chkSysAvoidLogin.objectName(), self.ui.chkSysAvoidLogin.isChecked())
        data['system'].setdefault(self.ui.editSysVersion.objectName(), self.ui.editSysVersion.text())
        return data

    def ftp_server_info(self):
        data = {'ftpServer': {}}
        data['ftpServer'].setdefault(self.ui.editFtpHost.objectName(), self.ui.editFtpHost.text())
        data['ftpServer'].setdefault(self.ui.editFtpPort.objectName(), self.ui.editFtpPort.text())
        data['ftpServer'].setdefault(self.ui.editFtpUserName.objectName(), self.ui.editFtpUserName.text())
        data['ftpServer'].setdefault(self.ui.editFtpPassword.objectName(), self.ui.editFtpPassword.text())
        data['ftpServer'].setdefault(self.ui.editFtpPath.objectName(), self.ui.editFtpPath.text())
        return data

    def get_hw_plat_info(self):
        return self.platform_dir

    def save_platform_info(self):
        if self.ui.editHwPlatform.text() == "" and self.ui.editHwVersion.text() == "":
            return

        info = {}
        info.update(self.hw_platform_info())
        info.update(self.sw_system_info())
        info.update(self.ftp_server_info())

        current_dir = os.path.join(os.getcwd(), UI.testItemsDir, self.ui.editHwPlatform.text() + "_" + self.ui.editHwVersion.text())
        if not os.path.exists(current_dir):
            os.makedirs(current_dir)
        self.platform_dir = self.ui.editHwPlatform.text() + "_" + self.ui.editHwVersion.text()
        file_path = os.path.join(current_dir, UI.platformInfoFile)
        with open(file_path, 'w') as f:
            f.truncate(0)
            json.dump(info, f, ensure_ascii=False, indent=4)

    def set_platform_info(self, file_path):
        # file_path = os.path.join(path, UI.platformInfoFile)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                info = json.load(f)
            for key, value in info.items():
                if key == self.get_hw_platform_object_name():
                    self.ui.editHwPlatform.setText(value)
                elif key == self.get_hw_mode_object_name():
                    self.ui.editHwMode.setText(value)
                elif key == self.get_hw_version_object_name():
                    self.ui.editHwVersion.setText(value)

    def get_hw_platform_object_name(self):
        return self.ui.editHwPlatform.objectName()

    def get_hw_version_object_name(self):
        return self.ui.editHwVersion.objectName()

    def get_hw_mode_object_name(self):
        return self.ui.editHwMode.objectName()