from PyQt5.QtCore import QObject, pyqtSignal, QTimer, pyqtSlot, QByteArray, QIODevice, QThread
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo


class SerialPort(QObject):
    data_received = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        # 创建串口对象
        self.serial_port = QSerialPort()

        self.serial_port.setDataBits(QSerialPort.Data8)
        self.serial_port.setParity(QSerialPort.NoParity)
        self.serial_port.setStopBits(QSerialPort.OneStop)
        # self.serial_port.setFlowControl(QSerialPort.NoFlowControl)

        # 连接串口数据接收的信号和槽函数
        self.serial_port.readyRead.connect(self.handle_serial_data)

        self.timer = QTimer()
        self.timer.timeout.connect(self.command_timeout_handler)
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
            # print('command', QByteArray(command.encode()))
            self.serial_port.write(QByteArray(command.encode()))
            self.serial_port.waitForBytesWritten(1000)
            if int(timeout) > 0:
                self.timer.start(int(timeout) * 1000)

    @pyqtSlot()
    def command_timeout_handler(self):
        self.timer.stop()
        if self.serial_port.isOpen():
            self.data_received.emit('Timeout')

    def handle_serial_data(self):
        if self.serial_port.isOpen():
            data = self.serial_port.readAll().data()
            str_data = data.decode('utf-8')
            self.data_received.emit(str_data)

    def close(self):
        if self.serial_port.isOpen():
            self.serial_port.close()



