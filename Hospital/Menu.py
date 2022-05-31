# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 755)
        icon = QIcon()
        icon.addFile(u":/images/images/coro1.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/*QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.298, y1:0.187727, x2:0.736, y2:0.534, stop:0 rgba(150, 141, 139, 229), stop:0.81592 rgba(112, 210, 221, 210));\n"
"}*/")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.slideframe = QFrame(self.centralwidget)
        self.slideframe.setObjectName(u"slideframe")
        self.slideframe.setMinimumSize(QSize(0, 0))
        self.slideframe.setMaximumSize(QSize(0, 16777215))
        self.slideframe.setFrameShape(QFrame.StyledPanel)
        self.slideframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.slideframe)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.frame_3 = QFrame(self.slideframe)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton:hover{\n"
"	/*background-color:rgba(0,0,255,80);*/\n"
"	color:blue;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:lightgrey;\n"
"	border-radius:5px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 150))
        self.frame_4.setStyleSheet(u"QFrame#frame_4{\n"
"	background-color: qlineargradient(spread:pad, x1:0.298, y1:0.187727, x2:0.736, y2:0.534, stop:0 rgba(150, 141, 139, 229), stop:0.81592 rgba(112, 210, 221, 210));\n"
"	border:2px solid rgb(171, 171, 171);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background:transparent;")

        self.verticalLayout_6.addWidget(self.label)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btnsavepatient = QPushButton(self.frame)
        self.btnsavepatient.setObjectName(u"btnsavepatient")
        self.btnsavepatient.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	\n"
"}")

        self.verticalLayout_4.addWidget(self.btnsavepatient)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.btnconsult = QPushButton(self.frame)
        self.btnconsult.setObjectName(u"btnconsult")
        self.btnconsult.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	\n"
"}")

        self.verticalLayout_4.addWidget(self.btnconsult)

        self.btnmodify = QPushButton(self.frame)
        self.btnmodify.setObjectName(u"btnmodify")
        self.btnmodify.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	\n"
"}")

        self.verticalLayout_4.addWidget(self.btnmodify)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.btnsavedpatient = QPushButton(self.frame)
        self.btnsavedpatient.setObjectName(u"btnsavedpatient")
        self.btnsavedpatient.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	\n"
"}")

        self.verticalLayout_4.addWidget(self.btnsavedpatient)

        self.btnrecap = QPushButton(self.frame)
        self.btnrecap.setObjectName(u"btnrecap")
        self.btnrecap.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	\n"
"}")

        self.verticalLayout_4.addWidget(self.btnrecap)

        self.btnseebooklet = QPushButton(self.frame)
        self.btnseebooklet.setObjectName(u"btnseebooklet")
        self.btnseebooklet.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	\n"
"}")

        self.verticalLayout_4.addWidget(self.btnseebooklet)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.btnparametre = QPushButton(self.frame)
        self.btnparametre.setObjectName(u"btnparametre")
        self.btnparametre.setStyleSheet(u"QPushButton{\n"
"	border:none;	\n"
"}")

        self.verticalLayout_4.addWidget(self.btnparametre)

        self.btncredit = QPushButton(self.frame)
        self.btncredit.setObjectName(u"btncredit")
        self.btncredit.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}")

        self.verticalLayout_4.addWidget(self.btncredit)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_4)

        self.quitbtn = QPushButton(self.frame)
        self.quitbtn.setObjectName(u"quitbtn")
        self.quitbtn.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	\n"
"}")

        self.verticalLayout_4.addWidget(self.quitbtn)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_5, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.slideframe)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.headframe = QFrame(self.frame_2)
        self.headframe.setObjectName(u"headframe")
        self.headframe.setFrameShape(QFrame.StyledPanel)
        self.headframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.headframe)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.menubtn = QToolButton(self.headframe)
        self.menubtn.setObjectName(u"menubtn")
        font = QFont()
        font.setPointSize(11)
        self.menubtn.setFont(font)
        self.menubtn.setStyleSheet(u"QToolButton{\n"
"/*border-radius:17px;*/\n"
"image: url(:/images/images/format-justify-fill.svg);\n"
"border:1px solid rgb(171, 171, 171);\n"
"}\n"
"\n"
"QToolButton::pressed{\n"
"	background: rgba(171, 171, 171,60);\n"
"}\n"
"\n"
"/*QToolButton::hover{\n"
"	background : rgba(171, 171, 171,100);\n"
"}\n"
"*/")
        self.menubtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.menubtn, 0, Qt.AlignLeft)

        self.label_4 = QLabel(self.headframe)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(19)
        font1.setBold(True)
        self.label_4.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.settingsbtn = QToolButton(self.headframe)
        self.settingsbtn.setObjectName(u"settingsbtn")
        self.settingsbtn.setFont(font)
        self.settingsbtn.setStyleSheet(u"QToolButton{\n"
"border-radius:17px;\n"
"image: url(:/images/images/settings.svg);\n"
"border:1px solid rgb(171, 171, 171);\n"
"}\n"
"\n"
"QToolButton::pressed{\n"
"	background: rgba(171, 171, 171,60);\n"
"}")
        self.settingsbtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.settingsbtn, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.headframe, 0, Qt.AlignTop)

        self.mainframe = QFrame(self.frame_2)
        self.mainframe.setObjectName(u"mainframe")
        sizePolicy.setHeightForWidth(self.mainframe.sizePolicy().hasHeightForWidth())
        self.mainframe.setSizePolicy(sizePolicy)
        self.mainframe.setFrameShape(QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.mainframe)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\n"
"\n"
"\n"
"\n"
"User\n"
"Speciality", None))
        self.btnsavepatient.setText(QCoreApplication.translate("MainWindow", u"Enregistre Un Patient", None))
        self.btnconsult.setText(QCoreApplication.translate("MainWindow", u"Consulter Un Patient", None))
        self.btnmodify.setText(QCoreApplication.translate("MainWindow", u"Modifier les information d'un \n"
"patient", None))
        self.btnsavedpatient.setText(QCoreApplication.translate("MainWindow", u"Patient Enregistrez", None))
        self.btnrecap.setText(QCoreApplication.translate("MainWindow", u"Recapitulatif", None))
        self.btnseebooklet.setText(QCoreApplication.translate("MainWindow", u"Visualisez les carnet", None))
        self.btnparametre.setText(QCoreApplication.translate("MainWindow", u"Parametre", None))
        self.btncredit.setText(QCoreApplication.translate("MainWindow", u"\u00c0 propos", None))
        self.quitbtn.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Naspitoo V 2.0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"copyright \u00a9 2021", None))
        self.menubtn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<span style=\"color:tomato\">N</span>aspitoo", None))
        self.settingsbtn.setText("")
    # retranslateUi

