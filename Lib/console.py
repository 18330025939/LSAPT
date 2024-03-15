from PyQt5.QtCore import QObject, pyqtSignal, QTimer, pyqtSlot, QByteArray, QIODevice, QTime
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from Lib.ui import UI
import time

class SerialPort(QObject):
    data_received = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        # 创建串口对象
        self.serial_port = QSerialPort()
        self.start_time = None
        self.end_time = None

        self.serial_port.setDataBits(QSerialPort.Data8)
        self.serial_port.setParity(QSerialPort.NoParity)
        self.serial_port.setStopBits(QSerialPort.OneStop)
        # self.serial_port.setFlowControl(QSerialPort.NoFlowControl)

        # 连接串口数据接收的信号和槽函数
        self.serial_port.readyRead.connect(self.handle_serial_data)
        self.buffer = b''
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.command_timeout_handler)
        # self.timer.setSingleShot(True)

    def open(self, port, baud):
        port_info_list = QSerialPortInfo.availablePorts()
        if len(port_info_list) == 0:
            return False
        for port_info in port_info_list:
            if port_info.portName() in port:
                self.serial_port.setPort(port_info)
                break

        if baud == '9600':
            self.serial_port.setBaudRate(QSerialPort.Baud9600)
        elif baud == '19200':
            self.serial_port.setBaudRate(QSerialPort.Baud19200)
        elif baud == '57600':
            self.serial_port.setBaudRate(QSerialPort.Baud57600)
        elif baud == '115200':
            self.serial_port.setBaudRate(QSerialPort.Baud115200)
        else:
            return False
        # 打开串口
        if self.serial_port.open(QIODevice.ReadWrite):
            return True
        else:
            return False

    def send_command(self, command, timeout):
        if self.serial_port.isOpen():
            data = command + '\n'
            byte_array = data.encode()
            UI.logger.log_debug('Serial Send data: %s', byte_array)
            self.buffer = b''
            # self.serial_port.writeData(byte_array)
            self.serial_port.write(byte_array)
            self.serial_port.waitForBytesWritten()
            if float(timeout) != 0:
                self.timer.start(int(float(timeout) * 1000))

    # def send_command(self, command, max_retry=3):
    #     self.serial_port.clearError()
    #     retry_count = 0
    #     data = command + '\n'
    #     byte_array = data.encode()
    #     while retry_count < max_retry:
    #         if self.serial_port.isOpen() and self.serial_port.isWritable():
    #             self.serial_port.write(byte_array)
    #             if not self.serial_port.waitForBytesWritten(1000):
    #                 retry_count += 1
    #                 continue
    #             return True
    #         else:
    #             self.serial_port.clearError()
    #             self.serial_port.open(QIODevice.ReadWrite)
    #             retry_count += 1
    #     return False

    # def command_timeout_handler(self):
    #     self.timer.stop()
    #     print('timeout')
    #     if self.serial_port.isOpen():
    #         self.data_received.emit('Timeout')

    def handle_serial_data(self):
        if self.serial_port.isOpen():
            self.serial_port.waitForReadyRead(10)
            if self.serial_port.bytesAvailable() > 0:
                data = self.serial_port.readAll().data()
                self.buffer += data
            if b'\r\n[root' in self.buffer and b']#' in self.buffer:
                UI.logger.log_debug('Serial receive data: %s', self.buffer)
                self.data_received.emit(self.buffer.decode())

    # def receive_timeout(self, timeout=500):
    #     self.serial_port.clearError()
    #     self.buffer = b''
    #     start_time = QTime.currentTime()
    #     while self.serial_port.isOpen() and self.serial_port.isReadable():
    #         if self.serial_port.waitForReadyRead(1000):
    #             self.buffer += self.serial_port.readAll().data()
    #
    #         elapsed_time = start_time.msecsTo(QTime.currentTime())
    #         if elapsed_time > timeout:
    #             break
    #     return self.buffer.decode()

    def close(self):
        if self.serial_port.isOpen():
            self.serial_port.waitForBytesWritten()
            self.serial_port.close()




