from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtCore import QIODevice, QByteArray, QTime


class SerialPort(QSerialPort):
    def __init__(self, parent=None):
        super().__init__(parent)

    def sendWithRetry(self, data: QByteArray, max_retry: int):
        self.clearError()
        retry_count = 0
        while retry_count < max_retry:
            if self.isOpen() and self.isWritable():
                self.write(data)
                if not self.waitForBytesWritten(1000):
                    retry_count += 1
                    continue
                return True
            else:
                self.clearError()
                self.open(QIODevice.ReadWrite)
                retry_count += 1
        return False

    def receiveWithTimeout(self, max_timeout: int):
        self.clearError()
        received_data = QByteArray()
        start_time = QTime.currentTime()
        while self.isOpen() and self.isReadable():
            if self.waitForReadyRead(1000):
                received_data += self.readAll()
            elapsed_time = start_time.msecsTo(QTime.currentTime())
            if elapsed_time >= max_timeout:
                break
        return received_data

serial_port = SerialPort()
serial_port.setPortName("COM1")
serial_port.setBaudRate(QSerialPort.Baud115200)
serial_port.setDataBits(QSerialPort.Data8)
serial_port.setParity(QSerialPort.NoParity)
serial_port.setStopBits(QSerialPort.OneStop)

if serial_port.open(QIODevice.ReadWrite):
    data = QByteArray(b'Hello, world!')
    if serial_port.sendWithRetry(data, 3):
        received_data = serial_port.receiveWithTimeout(1000)
        print(received_data)
    serial_port.close()


