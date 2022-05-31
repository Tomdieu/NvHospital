# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nsconfig.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import images_rc

class Ui_NsConfig(object):
    def setupUi(self, NsConfig):
        if not NsConfig.objectName():
            NsConfig.setObjectName(u"NsConfig")
        NsConfig.resize(614, 690)
        self.verticalLayout = QVBoxLayout(NsConfig)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(NsConfig)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.scrollArea = QScrollArea(self.frame_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 582, 1234))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.btnreset = QPushButton(self.frame_7)
        self.btnreset.setObjectName(u"btnreset")
        icon = QIcon()
        icon.addFile(u":/images/images/reset.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnreset.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.btnreset, 0, Qt.AlignLeft)

        self.btnsaveconfig = QPushButton(self.frame_7)
        self.btnsaveconfig.setObjectName(u"btnsaveconfig")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/document-save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnsaveconfig.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.btnsaveconfig, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 200))
        self.frame_4.setStyleSheet(u"QFrame#frame_4{\n"
"	height:100%;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.groupBox = QGroupBox(self.frame_4)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.villetable = QTableWidget(self.groupBox)
        if (self.villetable.columnCount() < 1):
            self.villetable.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.villetable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.villetable.setObjectName(u"villetable")
        self.villetable.setAlternatingRowColors(False)
        self.villetable.setRowCount(0)
        self.villetable.horizontalHeader().setStretchLastSection(False)

        self.horizontalLayout_2.addWidget(self.villetable)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.activateville = QCheckBox(self.groupBox)
        self.activateville.setObjectName(u"activateville")

        self.verticalLayout_9.addWidget(self.activateville)

        self.btnaddville = QPushButton(self.groupBox)
        self.btnaddville.setObjectName(u"btnaddville")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnaddville.setIcon(icon2)

        self.verticalLayout_9.addWidget(self.btnaddville)

        self.btnremoveville = QPushButton(self.groupBox)
        self.btnremoveville.setObjectName(u"btnremoveville")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnremoveville.setIcon(icon3)

        self.verticalLayout_9.addWidget(self.btnremoveville)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)


        self.verticalLayout_5.addWidget(self.groupBox)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.groupBox_2 = QGroupBox(self.frame_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 200))
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.professiontable = QTableWidget(self.groupBox_2)
        if (self.professiontable.columnCount() < 1):
            self.professiontable.setColumnCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.professiontable.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        self.professiontable.setObjectName(u"professiontable")
        self.professiontable.horizontalHeader().setStretchLastSection(False)

        self.horizontalLayout.addWidget(self.professiontable)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.activateprof = QCheckBox(self.groupBox_2)
        self.activateprof.setObjectName(u"activateprof")

        self.verticalLayout_10.addWidget(self.activateprof)

        self.btnaddpro = QPushButton(self.groupBox_2)
        self.btnaddpro.setObjectName(u"btnaddpro")
        self.btnaddpro.setIcon(icon2)

        self.verticalLayout_10.addWidget(self.btnaddpro)

        self.btnremovepro = QPushButton(self.groupBox_2)
        self.btnremovepro.setObjectName(u"btnremovepro")
        self.btnremovepro.setIcon(icon3)

        self.verticalLayout_10.addWidget(self.btnremovepro)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_10)


        self.verticalLayout_6.addWidget(self.groupBox_2)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.groupBox_3 = QGroupBox(self.frame_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 200))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.interventiontable = QTableWidget(self.groupBox_3)
        if (self.interventiontable.columnCount() < 1):
            self.interventiontable.setColumnCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.interventiontable.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        self.interventiontable.setObjectName(u"interventiontable")
        self.interventiontable.horizontalHeader().setStretchLastSection(False)

        self.horizontalLayout_3.addWidget(self.interventiontable)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.activateint = QCheckBox(self.groupBox_3)
        self.activateint.setObjectName(u"activateint")

        self.verticalLayout_11.addWidget(self.activateint)

        self.btnaddinter = QPushButton(self.groupBox_3)
        self.btnaddinter.setObjectName(u"btnaddinter")
        self.btnaddinter.setIcon(icon2)

        self.verticalLayout_11.addWidget(self.btnaddinter)

        self.btnremoveinter = QPushButton(self.groupBox_3)
        self.btnremoveinter.setObjectName(u"btnremoveinter")
        self.btnremoveinter.setIcon(icon3)

        self.verticalLayout_11.addWidget(self.btnremoveinter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_11)


        self.verticalLayout_8.addWidget(self.groupBox_3)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.groupBox_4 = QGroupBox(self.frame_8)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 200))
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.anneetable = QTableWidget(self.groupBox_4)
        if (self.anneetable.columnCount() < 1):
            self.anneetable.setColumnCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.anneetable.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        self.anneetable.setObjectName(u"anneetable")
        self.anneetable.horizontalHeader().setDefaultSectionSize(210)
        self.anneetable.horizontalHeader().setStretchLastSection(False)
        self.anneetable.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_5.addWidget(self.anneetable)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.activateyear = QCheckBox(self.groupBox_4)
        self.activateyear.setObjectName(u"activateyear")

        self.verticalLayout_13.addWidget(self.activateyear)

        self.btnaddyear = QPushButton(self.groupBox_4)
        self.btnaddyear.setObjectName(u"btnaddyear")
        self.btnaddyear.setIcon(icon2)

        self.verticalLayout_13.addWidget(self.btnaddyear)

        self.btnremoveyear = QPushButton(self.groupBox_4)
        self.btnremoveyear.setObjectName(u"btnremoveyear")
        self.btnremoveyear.setIcon(icon3)

        self.verticalLayout_13.addWidget(self.btnremoveyear)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_13)


        self.verticalLayout_12.addWidget(self.groupBox_4)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QPushButton{\n"
"	height:30px;\n"
"}\n"
"\n"
"QPushButton#btnchoosesqlitefile{\n"
"	height:20%;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_11)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_7.setFont(font1)

        self.verticalLayout_17.addWidget(self.label_7)


        self.verticalLayout_14.addWidget(self.frame_11)

        self.errorslideframe = QFrame(self.frame_9)
        self.errorslideframe.setObjectName(u"errorslideframe")
        self.errorslideframe.setMaximumSize(QSize(16777215, 0))
        self.errorslideframe.setStyleSheet(u"QFrame#errorslideframe{\n"
"	border:0.5px solid rgb(171,171,171);\n"
"	border-left:6px solid red; \n"
"}")
        self.errorslideframe.setFrameShape(QFrame.StyledPanel)
        self.errorslideframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.errorslideframe)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.mysqldatabaseerrorconnextion = QLabel(self.errorslideframe)
        self.mysqldatabaseerrorconnextion.setObjectName(u"mysqldatabaseerrorconnextion")

        self.horizontalLayout_6.addWidget(self.mysqldatabaseerrorconnextion)


        self.verticalLayout_14.addWidget(self.errorslideframe)

        self.groupBox_5 = QGroupBox(self.frame_9)
        self.groupBox_5.setObjectName(u"groupBox_5")
        font2 = QFont()
        font2.setBold(True)
        self.groupBox_5.setFont(font2)
        self.groupBox_5.setStyleSheet(u"QGroupBox{\n"
"font-weight:bold;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(1, 1, 1, 1)
        self.frame_12 = QFrame(self.groupBox_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.radiomysql = QRadioButton(self.frame_12)
        self.radiomysql.setObjectName(u"radiomysql")
        icon4 = QIcon()
        icon4.addFile(u":/images/images/1200px-MySQL.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radiomysql.setIcon(icon4)
        self.radiomysql.setIconSize(QSize(32, 23))

        self.horizontalLayout_12.addWidget(self.radiomysql)

        self.radiosqlite = QRadioButton(self.frame_12)
        self.radiosqlite.setObjectName(u"radiosqlite")
        icon5 = QIcon()
        icon5.addFile(u":/images/images/1280px-SQLite370.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.radiosqlite.setIcon(icon5)
        self.radiosqlite.setIconSize(QSize(32, 23))
        self.radiosqlite.setChecked(True)

        self.horizontalLayout_12.addWidget(self.radiosqlite)


        self.verticalLayout_15.addWidget(self.frame_12)

        self.tabWidget = QTabWidget(self.groupBox_5)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setIconSize(QSize(32, 23))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_16 = QVBoxLayout(self.tab)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.username = QLineEdit(self.tab)
        self.username.setObjectName(u"username")

        self.gridLayout.addWidget(self.username, 1, 1, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.port = QLineEdit(self.tab)
        self.port.setObjectName(u"port")

        self.gridLayout.addWidget(self.port, 0, 3, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.database = QLineEdit(self.tab)
        self.database.setObjectName(u"database")

        self.gridLayout.addWidget(self.database, 2, 1, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)

        self.host = QLineEdit(self.tab)
        self.host.setObjectName(u"host")

        self.gridLayout.addWidget(self.host, 0, 1, 1, 1)

        self.password = QLineEdit(self.tab)
        self.password.setObjectName(u"password")

        self.gridLayout.addWidget(self.password, 1, 3, 1, 1)


        self.verticalLayout_16.addLayout(self.gridLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btnconnectmysql = QPushButton(self.tab)
        self.btnconnectmysql.setObjectName(u"btnconnectmysql")

        self.horizontalLayout_7.addWidget(self.btnconnectmysql, 0, Qt.AlignLeft)

        self.btnclosemysql = QPushButton(self.tab)
        self.btnclosemysql.setObjectName(u"btnclosemysql")

        self.horizontalLayout_7.addWidget(self.btnclosemysql, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.verticalLayout_16.addLayout(self.horizontalLayout_7)

        icon6 = QIcon()
        icon6.addFile(u":/images/images/1200px-MySQL.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon6, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_18 = QVBoxLayout(self.tab_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btnconnectsqlite = QPushButton(self.tab_2)
        self.btnconnectsqlite.setObjectName(u"btnconnectsqlite")

        self.horizontalLayout_8.addWidget(self.btnconnectsqlite)

        self.btnclosesqlite = QPushButton(self.tab_2)
        self.btnclosesqlite.setObjectName(u"btnclosesqlite")

        self.horizontalLayout_8.addWidget(self.btnclosesqlite)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 1, 0, 1, 2)

        self.btnchoosesqlitefile = QPushButton(self.tab_2)
        self.btnchoosesqlitefile.setObjectName(u"btnchoosesqlitefile")

        self.gridLayout_2.addWidget(self.btnchoosesqlitefile, 0, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.sqlitedatabasepath = QLineEdit(self.tab_2)
        self.sqlitedatabasepath.setObjectName(u"sqlitedatabasepath")

        self.gridLayout_2.addWidget(self.sqlitedatabasepath, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.tab_2, icon5, "")

        self.verticalLayout_15.addWidget(self.tabWidget)


        self.verticalLayout_14.addWidget(self.groupBox_5)


        self.horizontalLayout_10.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border:none;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.frame_10)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setTristate(False)

        self.horizontalLayout_11.addWidget(self.checkBox, 0, Qt.AlignTop)


        self.horizontalLayout_10.addWidget(self.frame_10)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(NsConfig)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(NsConfig)
    # setupUi

    def retranslateUi(self, NsConfig):
        NsConfig.setWindowTitle(QCoreApplication.translate("NsConfig", u"Form", None))
        self.label.setText(QCoreApplication.translate("NsConfig", u"Naspitoo Config", None))
        self.btnreset.setText(QCoreApplication.translate("NsConfig", u"Renitialiser", None))
        self.btnsaveconfig.setText(QCoreApplication.translate("NsConfig", u"Sauvegarder", None))
        self.groupBox.setTitle(QCoreApplication.translate("NsConfig", u"Lieux de r\u00e9sidence", None))
        ___qtablewidgetitem = self.villetable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("NsConfig", u"Ville", None));
        self.activateville.setText("")
        self.btnaddville.setText("")
        self.btnremoveville.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("NsConfig", u"Profession", None))
        ___qtablewidgetitem1 = self.professiontable.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("NsConfig", u"Profession", None));
        self.activateprof.setText("")
        self.btnaddpro.setText("")
        self.btnremovepro.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("NsConfig", u"Intervention", None))
        ___qtablewidgetitem2 = self.interventiontable.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("NsConfig", u"Intervention", None));
        self.activateint.setText("")
        self.btnaddinter.setText("")
        self.btnremoveinter.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("NsConfig", u"Annee de la dernier participation", None))
        ___qtablewidgetitem3 = self.anneetable.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("NsConfig", u"Dernier annee de participation", None));
        self.activateyear.setText("")
        self.btnaddyear.setText("")
        self.btnremoveyear.setText("")
        self.label_7.setText(QCoreApplication.translate("NsConfig", u"Connecter vous a une base de donnee", None))
        self.mysqldatabaseerrorconnextion.setText(QCoreApplication.translate("NsConfig", u"connexion Error !          {}", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("NsConfig", u"Type de base de donn\u00e9e", None))
        self.radiomysql.setText(QCoreApplication.translate("NsConfig", u"Mysql", None))
        self.radiosqlite.setText(QCoreApplication.translate("NsConfig", u"Sqlite", None))
        self.username.setText(QCoreApplication.translate("NsConfig", u"root", None))
        self.label_4.setText(QCoreApplication.translate("NsConfig", u"Database", None))
        self.port.setText(QCoreApplication.translate("NsConfig", u"3306", None))
        self.label_5.setText(QCoreApplication.translate("NsConfig", u"<span style=\"color:red\"> * </span>port", None))
        self.label_3.setText(QCoreApplication.translate("NsConfig", u"<span style=\"color:red\"> * </span>Username ", None))
        self.label_2.setText(QCoreApplication.translate("NsConfig", u"<span style=\"color:red\"> * </span>Host ", None))
        self.label_6.setText(QCoreApplication.translate("NsConfig", u"password", None))
        self.host.setText(QCoreApplication.translate("NsConfig", u"127.0.0.1", None))
        self.btnconnectmysql.setText(QCoreApplication.translate("NsConfig", u"Connect", None))
        self.btnclosemysql.setText(QCoreApplication.translate("NsConfig", u"Close", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("NsConfig", u"MySql       ", None))
        self.label_8.setText(QCoreApplication.translate("NsConfig", u"SQLite File Path", None))
        self.btnconnectsqlite.setText(QCoreApplication.translate("NsConfig", u"Connect", None))
        self.btnclosesqlite.setText(QCoreApplication.translate("NsConfig", u"Close", None))
        self.btnchoosesqlitefile.setText(QCoreApplication.translate("NsConfig", u"choose Database file", None))
        self.sqlitedatabasepath.setText(QCoreApplication.translate("NsConfig", u"DB/Hospital.db", None))
        self.sqlitedatabasepath.setPlaceholderText(QCoreApplication.translate("NsConfig", u"SQlite file path", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("NsConfig", u"sqlite        ", None))
        self.checkBox.setText("")
    # retranslateUi

