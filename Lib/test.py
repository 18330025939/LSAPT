from PyQt5.QtCore import QCoreApplication, QIODevice, QTimer
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

class SerialPortHandler:
    def __init__(self, port1):
        self.port1 = port1
        # self.port2 = port2
        self.serial1 = QSerialPort()
        # self.serial2 = QSerialPort()
        self.timer = QTimer()

        self.timer.timeout.connect(self.read_data1)
        # self.serial1.readyRead.connect(self.send_data2)
        self.timer.start(100)

    def read_data1(self):
        if self.serial1.isOpen():
            data = self.serial1.readAll().data()
            if data:
                print("Received data from port1:", data)

    # def send_data2(self):
    #     if self.serial2.isOpen():
    #         data = self.serial2.readAll().data()
    #         if data:
    #             print("Received data from port2:", data)
    #             self.serial1.write(data)

    def open_serial_ports(self):
        for info in QSerialPortInfo.availablePorts():
            if info.portName() in self.port1:
                self.serial1.setPort(info)
            # elif info.portName() in self.port2:
            #     self.serial2.setPort(info)

        if self.serial1.open(QIODevice.ReadWrite):
            print("Opened", self.port1)

        # if self.serial2.open(QIODevice.ReadWrite):
        #     print("Opened", self.port2)

    def close_serial_ports(self):
        self.serial1.close()
        # self.serial2.close()

# Example usage
if __name__ == "__main__":
    app = QCoreApplication([])

    handler = SerialPortHandler("COM1")
    handler.open_serial_ports()


    # Do something else...

    handler.close_serial_ports()

    app.exec_()
