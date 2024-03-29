# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_platConfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlatConfig(object):
    def setupUi(self, PlatConfig):
        PlatConfig.setObjectName("PlatConfig")
        PlatConfig.resize(532, 653)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PlatConfig.sizePolicy().hasHeightForWidth())
        PlatConfig.setSizePolicy(sizePolicy)
        PlatConfig.setMinimumSize(QtCore.QSize(532, 653))
        PlatConfig.setMaximumSize(QtCore.QSize(532, 653))
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(PlatConfig)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame = QtWidgets.QFrame(PlatConfig)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelHWPlatName = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelHWPlatName.setFont(font)
        self.labelHWPlatName.setObjectName("labelHWPlatName")
        self.horizontalLayout.addWidget(self.labelHWPlatName)
        self.editHwPlatform = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editHwPlatform.setFont(font)
        self.editHwPlatform.setStyleSheet("font: 11pt \"宋体\";")
        self.editHwPlatform.setObjectName("editHwPlatform")
        self.horizontalLayout.addWidget(self.editHwPlatform)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelHwVersion = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelHwVersion.setFont(font)
        self.labelHwVersion.setObjectName("labelHwVersion")
        self.horizontalLayout_2.addWidget(self.labelHwVersion)
        self.editHwVersion = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editHwVersion.setFont(font)
        self.editHwVersion.setStyleSheet("font: 11pt \"宋体\";")
        self.editHwVersion.setObjectName("editHwVersion")
        self.horizontalLayout_2.addWidget(self.editHwVersion)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelHwTestMode = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelHwTestMode.setFont(font)
        self.labelHwTestMode.setObjectName("labelHwTestMode")
        self.horizontalLayout_3.addWidget(self.labelHwTestMode)
        self.editHwMode = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editHwMode.setFont(font)
        self.editHwMode.setStyleSheet("font: 11pt \"宋体\";")
        self.editHwMode.setObjectName("editHwMode")
        self.horizontalLayout_3.addWidget(self.editHwMode)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.editSysLogin = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editSysLogin.setFont(font)
        self.editSysLogin.setStyleSheet("font: 11pt \"宋体\";")
        self.editSysLogin.setObjectName("editSysLogin")
        self.horizontalLayout_4.addWidget(self.editSysLogin)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.editSysPassword = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editSysPassword.setFont(font)
        self.editSysPassword.setStyleSheet("font: 11pt \"宋体\";")
        self.editSysPassword.setObjectName("editSysPassword")
        self.horizontalLayout_5.addWidget(self.editSysPassword)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.editSysStartTimeout = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editSysStartTimeout.setFont(font)
        self.editSysStartTimeout.setStyleSheet("font: 11pt \"宋体\";")
        self.editSysStartTimeout.setObjectName("editSysStartTimeout")
        self.horizontalLayout_6.addWidget(self.editSysStartTimeout)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.chkSysAvoidLogin = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.chkSysAvoidLogin.setFont(font)
        self.chkSysAvoidLogin.setObjectName("chkSysAvoidLogin")
        self.verticalLayout_2.addWidget(self.chkSysAvoidLogin)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.editSysVersion = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editSysVersion.setFont(font)
        self.editSysVersion.setStyleSheet("font: 11pt \"宋体\";")
        self.editSysVersion.setObjectName("editSysVersion")
        self.horizontalLayout_7.addWidget(self.editSysVersion)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.editFtpHost = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editFtpHost.setFont(font)
        self.editFtpHost.setStyleSheet("font: 11pt \"宋体\";")
        self.editFtpHost.setObjectName("editFtpHost")
        self.horizontalLayout_8.addWidget(self.editFtpHost)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.editFtpPort = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editFtpPort.setFont(font)
        self.editFtpPort.setStyleSheet("font: 11pt \"宋体\";")
        self.editFtpPort.setObjectName("editFtpPort")
        self.horizontalLayout_9.addWidget(self.editFtpPort)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.editFtpUserName = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editFtpUserName.setFont(font)
        self.editFtpUserName.setStyleSheet("font: 11pt \"宋体\";")
        self.editFtpUserName.setObjectName("editFtpUserName")
        self.horizontalLayout_10.addWidget(self.editFtpUserName)
        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.editFtpPassword = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editFtpPassword.setFont(font)
        self.editFtpPassword.setStyleSheet("font: 11pt \"宋体\";")
        self.editFtpPassword.setObjectName("editFtpPassword")
        self.horizontalLayout_11.addWidget(self.editFtpPassword)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.labelFtpPath = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.labelFtpPath.setFont(font)
        self.labelFtpPath.setObjectName("labelFtpPath")
        self.horizontalLayout_12.addWidget(self.labelFtpPath)
        self.editFtpPath = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editFtpPath.setFont(font)
        self.editFtpPath.setStyleSheet("font: 11pt \"宋体\";")
        self.editFtpPath.setObjectName("editFtpPath")
        self.horizontalLayout_12.addWidget(self.editFtpPath)
        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(4, 1)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_7.setStretch(2, 1)
        self.horizontalLayout_13.addWidget(self.frame)

        self.retranslateUi(PlatConfig)
        QtCore.QMetaObject.connectSlotsByName(PlatConfig)

    def retranslateUi(self, PlatConfig):
        _translate = QtCore.QCoreApplication.translate
        PlatConfig.setWindowTitle(_translate("PlatConfig", "PlatConfig"))
        self.groupBox.setTitle(_translate("PlatConfig", "硬件平台信息"))
        self.labelHWPlatName.setText(_translate("PlatConfig", "主板名称："))
        self.labelHwVersion.setText(_translate("PlatConfig", "硬件版本："))
        self.labelHwTestMode.setText(_translate("PlatConfig", "测试模式："))
        self.groupBox_2.setTitle(_translate("PlatConfig", "软件系统信息"))
        self.label_4.setText(_translate("PlatConfig", "登录名称："))
        self.label_5.setText(_translate("PlatConfig", "登陆密码："))
        self.label_6.setText(_translate("PlatConfig", "启动超时时间："))
        self.chkSysAvoidLogin.setText(_translate("PlatConfig", "是否免密登录"))
        self.label_7.setText(_translate("PlatConfig", "系统版本："))
        self.groupBox_3.setTitle(_translate("PlatConfig", "FTP服务器信息"))
        self.label_8.setText(_translate("PlatConfig", "主机："))
        self.label_9.setText(_translate("PlatConfig", "端口："))
        self.label_10.setText(_translate("PlatConfig", "用户名："))
        self.label_11.setText(_translate("PlatConfig", "密码："))
        self.labelFtpPath.setText(_translate("PlatConfig", "存储路径："))
