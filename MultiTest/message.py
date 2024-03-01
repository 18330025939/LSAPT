from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton

class CustomMessageBox(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('提示')
        self.setFixedSize(300, 150) # 设置固定大小

        layout = QVBoxLayout(self)

        label = QLabel('测试完成，请进行下一步操作！', self)
        layout.addWidget(label)

        continue_button = QPushButton('继续', self)
        continue_button.clicked.connect(self.accept)
        layout.addWidget(continue_button)

        stop_button = QPushButton('中止', self)
        stop_button.clicked.connect(self.reject)
        layout.addWidget(stop_button)


