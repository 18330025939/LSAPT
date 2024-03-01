# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_multiTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MultiTest(object):
    def setupUi(self, MultiTest):
        MultiTest.setObjectName("MultiTest")
        MultiTest.resize(1234, 858)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MultiTest.sizePolicy().hasHeightForWidth())
        MultiTest.setSizePolicy(sizePolicy)
        MultiTest.setMinimumSize(QtCore.QSize(1234, 858))
        MultiTest.setMaximumSize(QtCore.QSize(1234, 858))
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(MultiTest)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_3 = QtWidgets.QFrame(MultiTest)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("background-color:rgb(223, 223, 223)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.frame_3.setMidLineWidth(3)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setContentsMargins(0, 2, 0, 2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnOpen = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpen.sizePolicy().hasHeightForWidth())
        self.btnOpen.setSizePolicy(sizePolicy)
        self.btnOpen.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/open1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOpen.setIcon(icon)
        self.btnOpen.setIconSize(QtCore.QSize(24, 24))
        self.btnOpen.setAutoDefault(False)
        self.btnOpen.setFlat(True)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout_3.addWidget(self.btnOpen)
        self.btnSave = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy)
        self.btnSave.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/save1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSave.setIcon(icon1)
        self.btnSave.setIconSize(QtCore.QSize(24, 24))
        self.btnSave.setCheckable(False)
        self.btnSave.setAutoDefault(False)
        self.btnSave.setFlat(True)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout_3.addWidget(self.btnSave)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.boxSerialSelect = QtWidgets.QComboBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boxSerialSelect.sizePolicy().hasHeightForWidth())
        self.boxSerialSelect.setSizePolicy(sizePolicy)
        self.boxSerialSelect.setObjectName("boxSerialSelect")
        self.boxSerialSelect.addItem("")
        self.boxSerialSelect.addItem("")
        self.boxSerialSelect.addItem("")
        self.boxSerialSelect.addItem("")
        self.boxSerialSelect.addItem("")
        self.boxSerialSelect.addItem("")
        self.boxSerialSelect.addItem("")
        self.boxSerialSelect.addItem("")
        self.boxSerialSelect.addItem("")
        self.boxSerialSelect.addItem("")
        self.horizontalLayout_3.addWidget(self.boxSerialSelect)
        self.boxBaudSelect = QtWidgets.QComboBox(self.frame_3)
        self.boxBaudSelect.setObjectName("boxBaudSelect")
        self.boxBaudSelect.addItem("")
        self.boxBaudSelect.addItem("")
        self.boxBaudSelect.addItem("")
        self.boxBaudSelect.addItem("")
        self.horizontalLayout_3.addWidget(self.boxBaudSelect)
        self.btnSerialConnect = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSerialConnect.sizePolicy().hasHeightForWidth())
        self.btnSerialConnect.setSizePolicy(sizePolicy)
        self.btnSerialConnect.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/connect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSerialConnect.setIcon(icon2)
        self.btnSerialConnect.setIconSize(QtCore.QSize(24, 24))
        self.btnSerialConnect.setAutoDefault(False)
        self.btnSerialConnect.setDefault(False)
        self.btnSerialConnect.setFlat(True)
        self.btnSerialConnect.setObjectName("btnSerialConnect")
        self.horizontalLayout_3.addWidget(self.btnSerialConnect)
        spacerItem1 = QtWidgets.QSpacerItem(782, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 2)
        self.horizontalLayout_3.setStretch(4, 2)
        self.horizontalLayout_3.setStretch(5, 1)
        self.horizontalLayout_3.setStretch(6, 20)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_9.addWidget(self.frame_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame = QtWidgets.QFrame(MultiTest)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    background-color:rgb(163, 244, 244);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(4)
        self.frame.setMidLineWidth(2)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 2, 0, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.labelModel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.labelModel.setFont(font)
        self.labelModel.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 75 14pt \"等线\";")
        self.labelModel.setText("")
        self.labelModel.setObjectName("labelModel")
        self.horizontalLayout.addWidget(self.labelModel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.labelTestFile = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.labelTestFile.setFont(font)
        self.labelTestFile.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 75 14pt \"等线\";")
        self.labelTestFile.setText("")
        self.labelTestFile.setObjectName("labelTestFile")
        self.horizontalLayout.addWidget(self.labelTestFile)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 2)
        self.horizontalLayout.setStretch(5, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.labelVersion = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.labelVersion.setFont(font)
        self.labelVersion.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 75 14pt \"等线\";")
        self.labelVersion.setText("")
        self.labelVersion.setObjectName("labelVersion")
        self.horizontalLayout_2.addWidget(self.labelVersion)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.labelMode = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.labelMode.setFont(font)
        self.labelMode.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 75 14pt \"等线\";")
        self.labelMode.setText("")
        self.labelMode.setObjectName("labelMode")
        self.horizontalLayout_2.addWidget(self.labelMode)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 2)
        self.horizontalLayout_2.setStretch(5, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_8.addWidget(self.frame)
        self.tableWidget = QtWidgets.QTableWidget(MultiTest)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget\n"
"{\n"
"    font: 12pt \"等线\";\n"
"}\n"
"")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_8.addWidget(self.tableWidget)
        self.editTestInfor = QtWidgets.QTextEdit(MultiTest)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editTestInfor.setFont(font)
        self.editTestInfor.setStyleSheet("QTextEdit\n"
"{\n"
"    background-color: rgb(2, 2, 2);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 12pt \"等线\";\n"
"}")
        self.editTestInfor.setFrameShadow(QtWidgets.QFrame.Plain)
        self.editTestInfor.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.editTestInfor.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.editTestInfor.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.editTestInfor.setReadOnly(True)
        self.editTestInfor.setObjectName("editTestInfor")
        self.verticalLayout_8.addWidget(self.editTestInfor)
        self.frame_5 = QtWidgets.QFrame(MultiTest)
        self.frame_5.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setContentsMargins(1, 0, 1, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_16.addWidget(self.label_12)
        self.labelTotalNumber = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.labelTotalNumber.setFont(font)
        self.labelTotalNumber.setObjectName("labelTotalNumber")
        self.horizontalLayout_16.addWidget(self.labelTotalNumber)
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_16.addWidget(self.label_6)
        self.labelSkipNumber = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.labelSkipNumber.setFont(font)
        self.labelSkipNumber.setObjectName("labelSkipNumber")
        self.horizontalLayout_16.addWidget(self.labelSkipNumber)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_16.addWidget(self.label_7)
        self.labelPassNumber = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.labelPassNumber.setFont(font)
        self.labelPassNumber.setObjectName("labelPassNumber")
        self.horizontalLayout_16.addWidget(self.labelPassNumber)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_16.addWidget(self.label_8)
        self.labelFailNumber = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.labelFailNumber.setFont(font)
        self.labelFailNumber.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelFailNumber.setObjectName("labelFailNumber")
        self.horizontalLayout_16.addWidget(self.labelFailNumber)
        self.verticalLayout_6.addLayout(self.horizontalLayout_16)
        self.verticalLayout_8.addWidget(self.frame_5)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 6)
        self.verticalLayout_8.setStretch(2, 2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.frame_4 = QtWidgets.QFrame(MultiTest)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setLineWidth(0)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/images/Lanner-logo.png"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: rgb(231, 231, 231);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 2, 0, 2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_14.addWidget(self.label_10)
        self.editSID = QtWidgets.QLineEdit(self.frame_2)
        self.editSID.setClearButtonEnabled(False)
        self.editSID.setObjectName("editSID")
        self.horizontalLayout_14.addWidget(self.editSID)
        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.editOPID = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editOPID.sizePolicy().hasHeightForWidth())
        self.editOPID.setSizePolicy(sizePolicy)
        self.editOPID.setObjectName("editOPID")
        self.horizontalLayout_5.addWidget(self.editOPID)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.labelImage = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelImage.sizePolicy().hasHeightForWidth())
        self.labelImage.setSizePolicy(sizePolicy)
        self.labelImage.setMinimumSize(QtCore.QSize(231, 201))
        self.labelImage.setMaximumSize(QtCore.QSize(231, 201))
        self.labelImage.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 20pt \"新宋体\";")
        self.labelImage.setScaledContents(False)
        self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImage.setObjectName("labelImage")
        self.verticalLayout_4.addWidget(self.labelImage)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.labelTestNumber = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.labelTestNumber.setFont(font)
        self.labelTestNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTestNumber.setObjectName("labelTestNumber")
        self.horizontalLayout_4.addWidget(self.labelTestNumber)
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.btnRetry = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRetry.sizePolicy().hasHeightForWidth())
        self.btnRetry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.btnRetry.setFont(font)
        self.btnRetry.setObjectName("btnRetry")
        self.verticalLayout_4.addWidget(self.btnRetry)
        self.btnStop = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.btnStop.setFont(font)
        self.btnStop.setObjectName("btnStop")
        self.verticalLayout_4.addWidget(self.btnStop)
        self.btnContinue = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnContinue.sizePolicy().hasHeightForWidth())
        self.btnContinue.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.btnContinue.setFont(font)
        self.btnContinue.setObjectName("btnContinue")
        self.verticalLayout_4.addWidget(self.btnContinue)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.btnContinue_2 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnContinue_2.sizePolicy().hasHeightForWidth())
        self.btnContinue_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.btnContinue_2.setFont(font)
        self.btnContinue_2.setObjectName("btnContinue_2")
        self.verticalLayout_4.addWidget(self.btnContinue_2)
        self.btnContinue_3 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnContinue_3.sizePolicy().hasHeightForWidth())
        self.btnContinue_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.btnContinue_3.setFont(font)
        self.btnContinue_3.setObjectName("btnContinue_3")
        self.verticalLayout_4.addWidget(self.btnContinue_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.verticalLayout_4.setStretch(0, 3)
        self.verticalLayout_4.setStretch(2, 6)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_4.setStretch(4, 2)
        self.verticalLayout_4.setStretch(5, 1)
        self.verticalLayout_4.setStretch(6, 1)
        self.verticalLayout_4.setStretch(7, 1)
        self.verticalLayout_4.setStretch(8, 2)
        self.verticalLayout_4.setStretch(9, 1)
        self.verticalLayout_4.setStretch(10, 1)
        self.verticalLayout_4.setStretch(11, 1)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6.addWidget(self.frame_4)
        self.horizontalLayout_6.setStretch(0, 4)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.retranslateUi(MultiTest)
        QtCore.QMetaObject.connectSlotsByName(MultiTest)
        MultiTest.setTabOrder(self.editTestInfor, self.btnStop)
        MultiTest.setTabOrder(self.btnStop, self.btnRetry)
        MultiTest.setTabOrder(self.btnRetry, self.tableWidget)

    def retranslateUi(self, MultiTest):
        _translate = QtCore.QCoreApplication.translate
        MultiTest.setWindowTitle(_translate("MultiTest", "MultiTest"))
        self.boxSerialSelect.setItemText(0, _translate("MultiTest", "Serial-COM1"))
        self.boxSerialSelect.setItemText(1, _translate("MultiTest", "Serial-COM2"))
        self.boxSerialSelect.setItemText(2, _translate("MultiTest", "Serial-COM3"))
        self.boxSerialSelect.setItemText(3, _translate("MultiTest", "Serial-COM4"))
        self.boxSerialSelect.setItemText(4, _translate("MultiTest", "Serial-COM5"))
        self.boxSerialSelect.setItemText(5, _translate("MultiTest", "Serial-COM6"))
        self.boxSerialSelect.setItemText(6, _translate("MultiTest", "Serial-COM7"))
        self.boxSerialSelect.setItemText(7, _translate("MultiTest", "Serial-COM8"))
        self.boxSerialSelect.setItemText(8, _translate("MultiTest", "Serial-COM9"))
        self.boxSerialSelect.setItemText(9, _translate("MultiTest", "Serial-COM10"))
        self.boxBaudSelect.setItemText(0, _translate("MultiTest", "9600"))
        self.boxBaudSelect.setItemText(1, _translate("MultiTest", "19200"))
        self.boxBaudSelect.setItemText(2, _translate("MultiTest", "57600"))
        self.boxBaudSelect.setItemText(3, _translate("MultiTest", "115200"))
        self.label_2.setText(_translate("MultiTest", "Model:"))
        self.label_4.setText(_translate("MultiTest", "TestFile:"))
        self.label.setText(_translate("MultiTest", "Version:"))
        self.label_3.setText(_translate("MultiTest", "Mode:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MultiTest", "Step"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MultiTest", "TestItem"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MultiTest", "Result"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MultiTest", "Date"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MultiTest", "StartTime"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MultiTest", "EndTime"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MultiTest", "Msg"))
        self.editTestInfor.setHtml(_translate("MultiTest", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'等线\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
        self.label_12.setText(_translate("MultiTest", "Total:"))
        self.labelTotalNumber.setText(_translate("MultiTest", "0"))
        self.label_6.setText(_translate("MultiTest", "Skip:"))
        self.labelSkipNumber.setText(_translate("MultiTest", "0"))
        self.label_7.setText(_translate("MultiTest", "Pass:"))
        self.labelPassNumber.setText(_translate("MultiTest", "0"))
        self.label_8.setText(_translate("MultiTest", "Fail:"))
        self.labelFailNumber.setText(_translate("MultiTest", "0"))
        self.label_10.setText(_translate("MultiTest", "SID:"))
        self.label_11.setText(_translate("MultiTest", "OPID:"))
        self.labelImage.setText(_translate("MultiTest", "无照片"))
        self.label_9.setText(_translate("MultiTest", "今天共测试:"))
        self.labelTestNumber.setText(_translate("MultiTest", "0"))
        self.label_13.setText(_translate("MultiTest", "片"))
        self.btnRetry.setText(_translate("MultiTest", "开始/重测"))
        self.btnStop.setText(_translate("MultiTest", "停止"))
        self.btnContinue.setText(_translate("MultiTest", "继续"))
        self.btnContinue_2.setText(_translate("MultiTest", "重启"))
        self.btnContinue_3.setText(_translate("MultiTest", "关机"))
import icons_rc
import images_rc