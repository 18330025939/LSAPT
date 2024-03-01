# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_multiConfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MultiConfig(object):
    def setupUi(self, MultiConfig):
        MultiConfig.setObjectName("MultiConfig")
        MultiConfig.resize(1040, 856)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(MultiConfig)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.treeUserCasesLib = QtWidgets.QTreeWidget(MultiConfig)
        self.treeUserCasesLib.setColumnCount(2)
        self.treeUserCasesLib.setObjectName("treeUserCasesLib")
        self.treeUserCasesLib.header().setCascadingSectionResizes(False)
        self.treeUserCasesLib.header().setSortIndicatorShown(False)
        self.verticalLayout_3.addWidget(self.treeUserCasesLib)
        self.editRootItem = QtWidgets.QLineEdit(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editRootItem.sizePolicy().hasHeightForWidth())
        self.editRootItem.setSizePolicy(sizePolicy)
        self.editRootItem.setObjectName("editRootItem")
        self.verticalLayout_3.addWidget(self.editRootItem)
        self.verticalLayout_3.setStretch(0, 20)
        self.verticalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.frame = QtWidgets.QFrame(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.btnUnfold = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUnfold.sizePolicy().hasHeightForWidth())
        self.btnUnfold.setSizePolicy(sizePolicy)
        self.btnUnfold.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUnfold.setIcon(icon)
        self.btnUnfold.setIconSize(QtCore.QSize(32, 32))
        self.btnUnfold.setAutoDefault(False)
        self.btnUnfold.setDefault(False)
        self.btnUnfold.setFlat(True)
        self.btnUnfold.setObjectName("btnUnfold")
        self.verticalLayout_4.addWidget(self.btnUnfold)
        self.btnSave = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy)
        self.btnSave.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSave.setIcon(icon1)
        self.btnSave.setIconSize(QtCore.QSize(32, 32))
        self.btnSave.setAutoDefault(False)
        self.btnSave.setDefault(False)
        self.btnSave.setFlat(True)
        self.btnSave.setObjectName("btnSave")
        self.verticalLayout_4.addWidget(self.btnSave)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.setStretch(0, 5)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 5)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addWidget(self.frame)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.label_8 = QtWidgets.QLabel(MultiConfig)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.editTestName = QtWidgets.QLineEdit(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editTestName.sizePolicy().hasHeightForWidth())
        self.editTestName.setSizePolicy(sizePolicy)
        self.editTestName.setText("")
        self.editTestName.setPlaceholderText("")
        self.editTestName.setObjectName("editTestName")
        self.verticalLayout_2.addWidget(self.editTestName)
        self.chkBoxPdtDel = QtWidgets.QCheckBox(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkBoxPdtDel.sizePolicy().hasHeightForWidth())
        self.chkBoxPdtDel.setSizePolicy(sizePolicy)
        self.chkBoxPdtDel.setStyleSheet("QCheckBox\n"
"{\n"
"    color:red;\n"
"}")
        self.chkBoxPdtDel.setObjectName("chkBoxPdtDel")
        self.verticalLayout_2.addWidget(self.chkBoxPdtDel)
        self.chkBoxErrCtn = QtWidgets.QCheckBox(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkBoxErrCtn.sizePolicy().hasHeightForWidth())
        self.chkBoxErrCtn.setSizePolicy(sizePolicy)
        self.chkBoxErrCtn.setStyleSheet("QCheckBox\n"
"{\n"
"    color:red;\n"
"}")
        self.chkBoxErrCtn.setObjectName("chkBoxErrCtn")
        self.verticalLayout_2.addWidget(self.chkBoxErrCtn)
        self.chkBoxArtPart = QtWidgets.QCheckBox(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkBoxArtPart.sizePolicy().hasHeightForWidth())
        self.chkBoxArtPart.setSizePolicy(sizePolicy)
        self.chkBoxArtPart.setObjectName("chkBoxArtPart")
        self.verticalLayout_2.addWidget(self.chkBoxArtPart)
        self.rdoBtnOnlyTest = QtWidgets.QRadioButton(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdoBtnOnlyTest.sizePolicy().hasHeightForWidth())
        self.rdoBtnOnlyTest.setSizePolicy(sizePolicy)
        self.rdoBtnOnlyTest.setAutoExclusive(True)
        self.rdoBtnOnlyTest.setObjectName("rdoBtnOnlyTest")
        self.verticalLayout_2.addWidget(self.rdoBtnOnlyTest)
        self.rdoBtnSkipTest = QtWidgets.QRadioButton(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdoBtnSkipTest.sizePolicy().hasHeightForWidth())
        self.rdoBtnSkipTest.setSizePolicy(sizePolicy)
        self.rdoBtnSkipTest.setAutoExclusive(True)
        self.rdoBtnSkipTest.setObjectName("rdoBtnSkipTest")
        self.verticalLayout_2.addWidget(self.rdoBtnSkipTest)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(MultiConfig)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.editTestInstr = QtWidgets.QTextEdit(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.editTestInstr.sizePolicy().hasHeightForWidth())
        self.editTestInstr.setSizePolicy(sizePolicy)
        self.editTestInstr.setLineWrapColumnOrWidth(454344444)
        self.editTestInstr.setTabStopWidth(80)
        self.editTestInstr.setPlaceholderText("")
        self.editTestInstr.setObjectName("editTestInstr")
        self.verticalLayout.addWidget(self.editTestInstr)
        self.label_2 = QtWidgets.QLabel(MultiConfig)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.editShowInfo = QtWidgets.QLineEdit(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.editShowInfo.sizePolicy().hasHeightForWidth())
        self.editShowInfo.setSizePolicy(sizePolicy)
        self.editShowInfo.setPlaceholderText("")
        self.editShowInfo.setObjectName("editShowInfo")
        self.verticalLayout.addWidget(self.editShowInfo)
        self.label_3 = QtWidgets.QLabel(MultiConfig)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.editTimeOut = QtWidgets.QLineEdit(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.editTimeOut.sizePolicy().hasHeightForWidth())
        self.editTimeOut.setSizePolicy(sizePolicy)
        self.editTimeOut.setText("")
        self.editTimeOut.setPlaceholderText("")
        self.editTimeOut.setObjectName("editTimeOut")
        self.verticalLayout.addWidget(self.editTimeOut)
        self.label_4 = QtWidgets.QLabel(MultiConfig)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.editImgPath = QtWidgets.QLineEdit(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.editImgPath.sizePolicy().hasHeightForWidth())
        self.editImgPath.setSizePolicy(sizePolicy)
        self.editImgPath.setPlaceholderText("")
        self.editImgPath.setObjectName("editImgPath")
        self.verticalLayout.addWidget(self.editImgPath)
        self.label_5 = QtWidgets.QLabel(MultiConfig)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.editPassText = QtWidgets.QLineEdit(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.editPassText.sizePolicy().hasHeightForWidth())
        self.editPassText.setSizePolicy(sizePolicy)
        self.editPassText.setPlaceholderText("")
        self.editPassText.setObjectName("editPassText")
        self.verticalLayout.addWidget(self.editPassText)
        self.label_6 = QtWidgets.QLabel(MultiConfig)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.editFailText = QtWidgets.QLineEdit(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.editFailText.sizePolicy().hasHeightForWidth())
        self.editFailText.setSizePolicy(sizePolicy)
        self.editFailText.setPlaceholderText("")
        self.editFailText.setObjectName("editFailText")
        self.verticalLayout.addWidget(self.editFailText)
        self.label_7 = QtWidgets.QLabel(MultiConfig)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.editRetryText = QtWidgets.QLineEdit(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.editRetryText.sizePolicy().hasHeightForWidth())
        self.editRetryText.setSizePolicy(sizePolicy)
        self.editRetryText.setPlaceholderText("")
        self.editRetryText.setObjectName("editRetryText")
        self.verticalLayout.addWidget(self.editRetryText)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 1)
        self.verticalLayout.setStretch(9, 1)
        self.verticalLayout.setStretch(10, 1)
        self.verticalLayout.setStretch(11, 1)
        self.verticalLayout.setStretch(12, 1)
        self.verticalLayout.setStretch(13, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalScrollBar_3 = QtWidgets.QScrollBar(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalScrollBar_3.sizePolicy().hasHeightForWidth())
        self.verticalScrollBar_3.setSizePolicy(sizePolicy)
        self.verticalScrollBar_3.setMaximum(99)
        self.verticalScrollBar_3.setProperty("value", 2)
        self.verticalScrollBar_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_3.setObjectName("verticalScrollBar_3")
        self.horizontalLayout.addWidget(self.verticalScrollBar_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(6, 1)
        self.verticalLayout_2.setStretch(7, 1)
        self.verticalLayout_2.setStretch(8, 16)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.frame_2 = QtWidgets.QFrame(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.btnWrite = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnWrite.sizePolicy().hasHeightForWidth())
        self.btnWrite.setSizePolicy(sizePolicy)
        self.btnWrite.setMouseTracking(False)
        self.btnWrite.setText("")
        self.btnWrite.setIcon(icon)
        self.btnWrite.setIconSize(QtCore.QSize(32, 32))
        self.btnWrite.setAutoDefault(False)
        self.btnWrite.setDefault(False)
        self.btnWrite.setFlat(True)
        self.btnWrite.setObjectName("btnWrite")
        self.verticalLayout_5.addWidget(self.btnWrite)
        self.btnRead = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRead.sizePolicy().hasHeightForWidth())
        self.btnRead.setSizePolicy(sizePolicy)
        self.btnRead.setText("")
        self.btnRead.setIcon(icon1)
        self.btnRead.setIconSize(QtCore.QSize(32, 32))
        self.btnRead.setAutoDefault(False)
        self.btnRead.setDefault(False)
        self.btnRead.setFlat(True)
        self.btnRead.setObjectName("btnRead")
        self.verticalLayout_5.addWidget(self.btnRead)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.verticalLayout_5.setStretch(0, 5)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 1)
        self.verticalLayout_5.setStretch(3, 5)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnImport = QtWidgets.QPushButton(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnImport.sizePolicy().hasHeightForWidth())
        self.btnImport.setSizePolicy(sizePolicy)
        self.btnImport.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnImport.setIcon(icon2)
        self.btnImport.setIconSize(QtCore.QSize(32, 32))
        self.btnImport.setAutoDefault(False)
        self.btnImport.setDefault(False)
        self.btnImport.setFlat(True)
        self.btnImport.setObjectName("btnImport")
        self.horizontalLayout_2.addWidget(self.btnImport)
        self.btnExport = QtWidgets.QPushButton(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExport.sizePolicy().hasHeightForWidth())
        self.btnExport.setSizePolicy(sizePolicy)
        self.btnExport.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExport.setIcon(icon3)
        self.btnExport.setIconSize(QtCore.QSize(32, 32))
        self.btnExport.setAutoDefault(False)
        self.btnExport.setDefault(False)
        self.btnExport.setFlat(True)
        self.btnExport.setObjectName("btnExport")
        self.horizontalLayout_2.addWidget(self.btnExport)
        spacerItem4 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.tableTestItem = QtWidgets.QTableWidget(MultiConfig)
        self.tableTestItem.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.tableTestItem.sizePolicy().hasHeightForWidth())
        self.tableTestItem.setSizePolicy(sizePolicy)
        self.tableTestItem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableTestItem.setRowCount(30)
        self.tableTestItem.setObjectName("tableTestItem")
        self.tableTestItem.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableTestItem.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableTestItem.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setKerning(True)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        self.tableTestItem.setItem(0, 0, item)
        self.tableTestItem.horizontalHeader().setCascadingSectionResizes(False)
        self.tableTestItem.horizontalHeader().setDefaultSectionSize(114)
        self.tableTestItem.horizontalHeader().setHighlightSections(False)
        self.tableTestItem.horizontalHeader().setMinimumSectionSize(40)
        self.tableTestItem.horizontalHeader().setSortIndicatorShown(False)
        self.tableTestItem.horizontalHeader().setStretchLastSection(True)
        self.tableTestItem.verticalHeader().setVisible(False)
        self.tableTestItem.verticalHeader().setCascadingSectionResizes(False)
        self.tableTestItem.verticalHeader().setDefaultSectionSize(30)
        self.tableTestItem.verticalHeader().setHighlightSections(True)
        self.tableTestItem.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_6.addWidget(self.tableTestItem)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(MultiConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.Panel)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEdit.setMaximumBlockCount(50)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_6.addWidget(self.plainTextEdit)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 15)
        self.verticalLayout_6.setStretch(2, 3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(2, 4)
        self.horizontalLayout_3.setStretch(4, 6)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(MultiConfig)
        QtCore.QMetaObject.connectSlotsByName(MultiConfig)

    def retranslateUi(self, MultiConfig):
        _translate = QtCore.QCoreApplication.translate
        MultiConfig.setWindowTitle(_translate("MultiConfig", "MultiConfig"))
        self.treeUserCasesLib.headerItem().setText(0, _translate("MultiConfig", "用例库"))
        self.treeUserCasesLib.headerItem().setText(1, _translate("MultiConfig", "版本"))
        self.editRootItem.setPlaceholderText(_translate("MultiConfig", "根节点名称"))
        self.textEdit.setHtml(_translate("MultiConfig", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:11pt; font-weight:600;\">参数配置</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; color:#0055ff;\">方法名称: ShowMessage</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; color:#0055ff;\">方法描述: 显示提示框</span></p></body></html>"))
        self.label_8.setText(_translate("MultiConfig", "测试用例名称"))
        self.chkBoxPdtDel.setText(_translate("MultiConfig", "生产模式下可以删除"))
        self.chkBoxErrCtn.setText(_translate("MultiConfig", "不良继续"))
        self.chkBoxArtPart.setText(_translate("MultiConfig", "人为参与"))
        self.rdoBtnOnlyTest.setText(_translate("MultiConfig", "总是测试"))
        self.rdoBtnSkipTest.setText(_translate("MultiConfig", "跳过测试"))
        self.label.setText(_translate("MultiConfig", "测试指令"))
        self.label_2.setText(_translate("MultiConfig", "返回的信息"))
        self.label_3.setText(_translate("MultiConfig", "指令超时时间"))
        self.label_4.setText(_translate("MultiConfig", "测试通过的参考照片"))
        self.label_5.setText(_translate("MultiConfig", "PASS显示的文字"))
        self.label_6.setText(_translate("MultiConfig", "FAIL显示的文字"))
        self.label_7.setText(_translate("MultiConfig", "RETRY显示的文字"))
        self.tableTestItem.setSortingEnabled(False)
        item = self.tableTestItem.horizontalHeaderItem(0)
        item.setText(_translate("MultiConfig", "Level"))
        item = self.tableTestItem.horizontalHeaderItem(1)
        item.setText(_translate("MultiConfig", "测试项名称"))
        __sortingEnabled = self.tableTestItem.isSortingEnabled()
        self.tableTestItem.setSortingEnabled(False)
        self.tableTestItem.setSortingEnabled(__sortingEnabled)
        self.plainTextEdit.setPlaceholderText(_translate("MultiConfig", "测试用例相关信息"))
import icons_rc
