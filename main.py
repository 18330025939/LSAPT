from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QWidget
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtWidgets, QtCore
from MultiConfig.multiConfig import MultiConfigWindow
from AutoPrt.autoPrt import MainWindow
from Lib.ui import UI
from Lib.logger import Logger
import sys

if __name__ == '__main__':
    app =QApplication(sys.argv)
    # ui = QWidget()
    # UI.configWin = MultiConfigWindow(ui)
    # UI.configWin.show
    UI.logger = Logger('./lsapt.log')
    UI.mainWin = MainWindow()
    UI.mainWin.show()
    # ui = UiMainWindow()
    # ui.show()

    sys.exit(app.exec())


# pyinstaller --paths /usr/local/lib/python3.8/dist-packages/PyQt5/Qt5/ -F -w --onefile main.py
# pyrcc5 -o icons_rc.py icons/icons.qrc
# pyrcc5 -o images_rc.py images/images.qrc
# pyinstaller main.py --noconsole --hidden-import PySide2.QtXml