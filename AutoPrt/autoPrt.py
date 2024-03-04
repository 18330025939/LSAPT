import threading

from PyQt5.QtWidgets import QMainWindow, QWidget
from AutoPrt.ui_autoPrt import Ui_AutoPrt
from MultiConfig.multiConfig import MultiConfigWindow
from Lib.ui import UI
from PlatConfig.platConfig import PlatConfigWindow
from MultiTest.multiTest import MultiTestWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AutoPrt()
        self.ui.setupUi(self)

        # self.closeEvent = self.on_close()
        self.ui.actMultiConfig.triggered.connect(self.act_multi_config)
        self.ui.actMultiTest.triggered.connect(self.act_multi_test)
        self.ui.actPlatformConfig.triggered.connect(self.act_platform_config)
        self.config_widget = QWidget()
        self.test_widget = QWidget()
        self.platform_widget = QWidget()
        UI.platWin = PlatConfigWindow(self.platform_widget)
        UI.configWin = MultiConfigWindow(self.config_widget)
        UI.testWin = MultiTestWindow(self.test_widget)

    def act_multi_config(self):
        if self.config_widget is None:
            self.config_widget = QWidget()
            UI.configWin = MultiConfigWindow(self.config_widget)
            self.ui.mdiArea.addSubWindow(UI.configWin)
        else:
            if self.config_widget.isVisible():
                # self.config_widget.hide()
                pass
            else:
                self.config_widget.show()
                self.ui.mdiArea.addSubWindow(UI.configWin)

    def act_multi_test(self):
        if self.test_widget is None:
            self.test_widget = QWidget()
            UI.testWin = MultiTestWindow(self.test_widget)
            self.ui.mdiArea.addSubWindow(UI.testWin)
        else:
            if self.test_widget.isVisible():
                pass
            else:
                self.test_widget.show()
                self.ui.mdiArea.addSubWindow(UI.testWin)

    def act_platform_config(self):
        if self.platform_widget is None:
            self.platform_widget = QWidget()
            UI.platWin = PlatConfigWindow(self.platform_widget)
            self.ui.mdiArea.addSubWindow(UI.platWin)
        else:
            # if self.config_widget is not None and self.config_widget.isVisible():
            #     self.config_widget.hide()
            if self.platform_widget.isVisible():
                pass
            else:
                self.platform_widget.show()
                self.ui.mdiArea.addSubWindow(UI.platWin)

