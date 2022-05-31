# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'consultation.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import images_rc

class Ui_Consulation(object):
    def setupUi(self, Consulation):
        if not Consulation.objectName():
            Consulation.setObjectName(u"Consulation")
        Consulation.resize(945, 911)
        self.verticalLayout = QVBoxLayout(Consulation)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.scrollArea = QScrollArea(Consulation)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 941, 907))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.slideframe = QFrame(self.scrollAreaWidgetContents)
        self.slideframe.setObjectName(u"slideframe")
        self.slideframe.setMaximumSize(QSize(16777215, 0))
        self.slideframe.setFrameShape(QFrame.StyledPanel)
        self.slideframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.slideframe)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 2, 2, 2)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.searchbox = QLineEdit(self.slideframe)
        self.searchbox.setObjectName(u"searchbox")
        self.searchbox.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setPointSize(14)
        self.searchbox.setFont(font)

        self.horizontalLayout.addWidget(self.searchbox)

        self.searchpatient = QPushButton(self.slideframe)
        self.searchpatient.setObjectName(u"searchpatient")
        icon = QIcon()
        icon.addFile(u":/images/images/folder-saved-search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchpatient.setIcon(icon)

        self.horizontalLayout.addWidget(self.searchpatient)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.slideframe)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_9.addWidget(self.slideframe)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 2, 2, 2)
        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.pushButton_3 = QPushButton(self.frame_8)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"background-color: rgba(166, 166, 166,255);\n"
"border :1px solid rgb(171, 171, 171);\n"
"/*border-radius:10px;\n"
"*/")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/dentist.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(32, 42))

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.btnslide = QToolButton(self.frame_8)
        self.btnslide.setObjectName(u"btnslide")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/arrow-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnslide.setIcon(icon2)
        self.btnslide.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.btnslide)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(11)
        self.frame_9.setFont(font2)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.groupBox = QGroupBox(self.frame_9)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font2)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.ncin = QLineEdit(self.groupBox)
        self.ncin.setObjectName(u"ncin")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ncin)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.nom = QLineEdit(self.groupBox)
        self.nom.setObjectName(u"nom")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nom)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.prenom = QLineEdit(self.groupBox)
        self.prenom.setObjectName(u"prenom")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.prenom)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.age = QLineEdit(self.groupBox)
        self.age.setObjectName(u"age")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.age)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Male = QRadioButton(self.groupBox)
        self.Male.setObjectName(u"Male")

        self.horizontalLayout_6.addWidget(self.Male, 0, Qt.AlignLeft)

        self.Female = QRadioButton(self.groupBox)
        self.Female.setObjectName(u"Female")

        self.horizontalLayout_6.addWidget(self.Female, 0, Qt.AlignLeft)

        self.toh = QRadioButton(self.groupBox)
        self.toh.setObjectName(u"toh")

        self.horizontalLayout_6.addWidget(self.toh)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lastyear = QComboBox(self.groupBox)
        self.lastyear.setObjectName(u"lastyear")

        self.horizontalLayout_7.addWidget(self.lastyear)


        self.formLayout.setLayout(7, QFormLayout.FieldRole, self.horizontalLayout_7)

        self.town = QComboBox(self.groupBox)
        self.town.setObjectName(u"town")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.town)

        self.prof = QComboBox(self.groupBox)
        self.prof.setObjectName(u"prof")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.prof)


        self.horizontalLayout_5.addLayout(self.formLayout)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_9)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font2)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.indiceC = QSpinBox(self.groupBox_2)
        self.indiceC.setObjectName(u"indiceC")
        self.indiceC.setMaximum(32)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.indiceC)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.indiceA = QSpinBox(self.groupBox_2)
        self.indiceA.setObjectName(u"indiceA")
        self.indiceA.setMaximum(32)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.indiceA)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.indiceO = QSpinBox(self.groupBox_2)
        self.indiceO.setObjectName(u"indiceO")
        self.indiceO.setMaximum(32)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.indiceO)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_13)

        self.indeiceAutre = QSpinBox(self.groupBox_2)
        self.indeiceAutre.setObjectName(u"indeiceAutre")
        self.indeiceAutre.setMaximum(32)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.indeiceAutre)


        self.verticalLayout_6.addLayout(self.formLayout_2)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame_9)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font2)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.intervention1 = QComboBox(self.groupBox_3)
        self.intervention1.setObjectName(u"intervention1")
        self.intervention1.setFocusPolicy(Qt.WheelFocus)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.intervention1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.intervention2 = QComboBox(self.groupBox_3)
        self.intervention2.setObjectName(u"intervention2")
        self.intervention2.setFocusPolicy(Qt.WheelFocus)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.intervention2)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_16)

        self.intervention3 = QComboBox(self.groupBox_3)
        self.intervention3.setObjectName(u"intervention3")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.intervention3)


        self.verticalLayout_7.addLayout(self.formLayout_3)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.frame_9)
        self.groupBox_4.setObjectName(u"groupBox_4")
        font3 = QFont()
        font3.setPointSize(10)
        self.groupBox_4.setFont(font3)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.diagnostic = QTextEdit(self.groupBox_4)
        self.diagnostic.setObjectName(u"diagnostic")
        self.diagnostic.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_8.addWidget(self.diagnostic)


        self.verticalLayout_4.addWidget(self.groupBox_4)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 2, 2, 2)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.clearinputs = QPushButton(self.frame_10)
        self.clearinputs.setObjectName(u"clearinputs")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/gtk-delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clearinputs.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.clearinputs, 0, Qt.AlignRight)

        self.seeconsultation = QPushButton(self.frame_10)
        self.seeconsultation.setObjectName(u"seeconsultation")
        icon4 = QIcon()
        icon4.addFile(u":/images/images/redeyes.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.seeconsultation.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.seeconsultation, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_10, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.searchframeslide = QFrame(self.frame_2)
        self.searchframeslide.setObjectName(u"searchframeslide")
        self.searchframeslide.setMaximumSize(QSize(0, 16777215))
        self.searchframeslide.setFrameShape(QFrame.StyledPanel)
        self.searchframeslide.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.searchframeslide)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.frame_4 = QFrame(self.searchframeslide)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        font4 = QFont()
        font4.setPointSize(12)
        self.label_18.setFont(font4)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_18)


        self.verticalLayout_10.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_11 = QFrame(self.searchframeslide)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(self.frame_11)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.patienterrornotfound = QLabel(self.frame)
        self.patienterrornotfound.setObjectName(u"patienterrornotfound")
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(False)
        self.patienterrornotfound.setFont(font5)

        self.horizontalLayout_11.addWidget(self.patienterrornotfound)


        self.verticalLayout_11.addWidget(self.frame)

        self.tableWidget = QTableWidget(self.frame_11)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_11.addWidget(self.tableWidget)


        self.verticalLayout_10.addWidget(self.frame_11)


        self.horizontalLayout_2.addWidget(self.searchframeslide)

        self.slideFrameConsult = QFrame(self.frame_2)
        self.slideFrameConsult.setObjectName(u"slideFrameConsult")
        self.slideFrameConsult.setMaximumSize(QSize(0, 16777215))
        self.slideFrameConsult.setFrameShape(QFrame.StyledPanel)
        self.slideFrameConsult.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.slideFrameConsult)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_5 = QFrame(self.slideFrameConsult)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_17)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.slideFrameConsult)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.consulation = QTextEdit(self.frame_6)
        self.consulation.setObjectName(u"consulation")

        self.verticalLayout_5.addWidget(self.consulation)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.slideFrameConsult)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.btngeneratecarnet = QPushButton(self.frame_7)
        self.btngeneratecarnet.setObjectName(u"btngeneratecarnet")

        self.horizontalLayout_9.addWidget(self.btngeneratecarnet)

        self.saveconsultation = QPushButton(self.frame_7)
        self.saveconsultation.setObjectName(u"saveconsultation")
        icon5 = QIcon()
        icon5.addFile(u":/images/images/document-save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveconsultation.setIcon(icon5)
        self.saveconsultation.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.saveconsultation)

        self.printconsultation = QPushButton(self.frame_7)
        self.printconsultation.setObjectName(u"printconsultation")
        icon6 = QIcon()
        icon6.addFile(u":/images/images/document-print.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.printconsultation.setIcon(icon6)
        self.printconsultation.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.printconsultation)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.horizontalLayout_2.addWidget(self.slideFrameConsult)


        self.verticalLayout_9.addWidget(self.frame_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Consulation)

        QMetaObject.connectSlotsByName(Consulation)
    # setupUi

    def retranslateUi(self, Consulation):
        Consulation.setWindowTitle(QCoreApplication.translate("Consulation", u"Form", None))
        self.searchbox.setPlaceholderText(QCoreApplication.translate("Consulation", u"Recherche d'un patient", None))
        self.searchpatient.setText("")
        self.label.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("Consulation", u"Consulation dentaire", None))
        self.btnslide.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Consulation", u"Information Personnel du patient ", None))
        self.label_2.setText(QCoreApplication.translate("Consulation", u"NCIN", None))
        self.ncin.setPlaceholderText(QCoreApplication.translate("Consulation", u"NCIN du patient", None))
        self.label_3.setText(QCoreApplication.translate("Consulation", u"NOM", None))
        self.nom.setPlaceholderText(QCoreApplication.translate("Consulation", u"NOM du patient", None))
        self.label_4.setText(QCoreApplication.translate("Consulation", u"PRENOM", None))
        self.prenom.setPlaceholderText(QCoreApplication.translate("Consulation", u"PRENOM du patient", None))
        self.label_5.setText(QCoreApplication.translate("Consulation", u"AGE", None))
        self.age.setPlaceholderText(QCoreApplication.translate("Consulation", u"AGE du patient", None))
        self.label_6.setText(QCoreApplication.translate("Consulation", u"SEX", None))
        self.Male.setText(QCoreApplication.translate("Consulation", u"M", None))
        self.Female.setText(QCoreApplication.translate("Consulation", u"F", None))
        self.toh.setText(QCoreApplication.translate("Consulation", u"x", None))
        self.label_7.setText(QCoreApplication.translate("Consulation", u"LIEUX DE R\u00c9SIDENCE", None))
        self.label_8.setText(QCoreApplication.translate("Consulation", u"PROFESSION", None))
        self.label_9.setText(QCoreApplication.translate("Consulation", u" ANN\u00c9E DE LA DERNIER PARICIPATION", None))
        self.lastyear.setPlaceholderText(QCoreApplication.translate("Consulation", u"Dernier ann\u00e9e de participation", None))
        self.town.setPlaceholderText(QCoreApplication.translate("Consulation", u"Ville du patient", None))
        self.prof.setPlaceholderText(QCoreApplication.translate("Consulation", u"Profession", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Consulation", u"INDICE CAO", None))
        self.label_11.setText(QCoreApplication.translate("Consulation", u"C                                                                      ", None))
        self.label_10.setText(QCoreApplication.translate("Consulation", u"A                                                                      ", None))
        self.label_12.setText(QCoreApplication.translate("Consulation", u"O", None))
        self.label_13.setText(QCoreApplication.translate("Consulation", u"Autre", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Consulation", u"INTERVENTION", None))
        self.label_14.setText(QCoreApplication.translate("Consulation", u"1                                                                      ", None))
        self.intervention1.setPlaceholderText(QCoreApplication.translate("Consulation", u"Intervention N\u00b0 1", None))
        self.label_15.setText(QCoreApplication.translate("Consulation", u"2                                                                      ", None))
        self.intervention2.setPlaceholderText(QCoreApplication.translate("Consulation", u"Intervention N\u00b0 2", None))
        self.label_16.setText(QCoreApplication.translate("Consulation", u"3", None))
        self.intervention3.setPlaceholderText(QCoreApplication.translate("Consulation", u"Intervention N\u00b0 3", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Consulation", u"Diagnostic Du Patient", None))
        self.diagnostic.setPlaceholderText(QCoreApplication.translate("Consulation", u"Diagnostic du patient", None))
        self.clearinputs.setText("")
        self.seeconsultation.setText("")
        self.label_18.setText(QCoreApplication.translate("Consulation", u"<strong>Resultat de recherche", None))
        self.patienterrornotfound.setText("")
        self.label_17.setText(QCoreApplication.translate("Consulation", u"<strong>Carnet De Consulation Du Patient</strong>", None))
        self.btngeneratecarnet.setText(QCoreApplication.translate("Consulation", u"Afficher le carnet", None))
        self.saveconsultation.setText("")
        self.printconsultation.setText("")
    # retranslateUi

