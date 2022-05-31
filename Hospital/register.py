# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import images_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(624, 656)
        font = QFont()
        font.setPointSize(14)
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(2)
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
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 1, -1, -1)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setStyleSheet(u"border:none;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_6)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 19, -1, -1)
        self.patientsurname = QLineEdit(self.frame_3)
        self.patientsurname.setObjectName(u"patientsurname")

        self.gridLayout.addWidget(self.patientsurname, 2, 1, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.patientname = QLineEdit(self.frame_3)
        self.patientname.setObjectName(u"patientname")

        self.gridLayout.addWidget(self.patientname, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.frame_3)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 6, 1, 1, 1)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 5, 1, 1, 1)

        self.ncin = QLineEdit(self.frame_3)
        self.ncin.setObjectName(u"ncin")

        self.gridLayout.addWidget(self.ncin, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)

        self.patientage = QLineEdit(self.frame_3)
        self.patientage.setObjectName(u"patientage")

        self.gridLayout.addWidget(self.patientage, 3, 1, 1, 1)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 33))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sexmale = QRadioButton(self.frame_4)
        self.sexmale.setObjectName(u"sexmale")

        self.horizontalLayout_2.addWidget(self.sexmale, 0, Qt.AlignLeft)

        self.sexfemal = QRadioButton(self.frame_4)
        self.sexfemal.setObjectName(u"sexfemal")

        self.horizontalLayout_2.addWidget(self.sexfemal, 0, Qt.AlignLeft)

        self.toh = QRadioButton(self.frame_4)
        self.toh.setObjectName(u"toh")

        self.horizontalLayout_2.addWidget(self.toh)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setStyleSheet(u"border:none;")

        self.horizontalLayout_2.addWidget(self.label_7)


        self.gridLayout.addWidget(self.frame_4, 4, 1, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.savepatient = QPushButton(self.frame_3)
        self.savepatient.setObjectName(u"savepatient")
        self.savepatient.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/images/images/document-save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.savepatient.setIcon(icon)
        self.savepatient.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.savepatient)

        self.btndelete = QPushButton(self.frame_3)
        self.btndelete.setObjectName(u"btndelete")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/gtk-delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btndelete.setIcon(icon1)
        self.btndelete.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btndelete)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.errFrame = QFrame(self.frame_3)
        self.errFrame.setObjectName(u"errFrame")
        self.errFrame.setMaximumSize(QSize(16777215, 0))
        self.errFrame.setStyleSheet(u"border:none;")
        self.errFrame.setFrameShape(QFrame.StyledPanel)
        self.errFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.errFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.erromsg = QLabel(self.errFrame)
        self.erromsg.setObjectName(u"erromsg")

        self.verticalLayout_5.addWidget(self.erromsg)


        self.verticalLayout_4.addWidget(self.errFrame, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        QWidget.setTabOrder(self.ncin, self.patientname)
        QWidget.setTabOrder(self.patientname, self.patientsurname)
        QWidget.setTabOrder(self.patientsurname, self.patientage)
        QWidget.setTabOrder(self.patientage, self.sexmale)
        QWidget.setTabOrder(self.sexmale, self.sexfemal)
        QWidget.setTabOrder(self.sexfemal, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.comboBox_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Enregistrez un patient", None))
        self.patientsurname.setPlaceholderText(QCoreApplication.translate("Form", u"Entrez le prenom du patient", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"AGE", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"SEX", None))
        self.patientname.setPlaceholderText(QCoreApplication.translate("Form", u"Entrez le nom du patient obligtoire", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"PRENOMS", None))
        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("Form", u"Selectionner Votre profession", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Form", u"Lieux De R\u00e9sidence", None))
        self.ncin.setPlaceholderText(QCoreApplication.translate("Form", u"Entrez le ncin du patient", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"NCIN", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"LIEUX DE R\u00c9SIDENCE", None))
        self.patientage.setPlaceholderText(QCoreApplication.translate("Form", u"Entrez l'age obligatoire", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"PROFESSION", None))
        self.sexmale.setText(QCoreApplication.translate("Form", u"M", None))
        self.sexfemal.setText(QCoreApplication.translate("Form", u"F", None))
        self.toh.setText(QCoreApplication.translate("Form", u"x", None))
        self.label_7.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"NOM", None))
        self.savepatient.setText(QCoreApplication.translate("Form", u"Enregistre le patient", None))
        self.btndelete.setText(QCoreApplication.translate("Form", u"Nettoyer", None))
        self.erromsg.setText("")
    # retranslateUi

