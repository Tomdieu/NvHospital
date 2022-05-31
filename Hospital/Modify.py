# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Modify.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import images_rc

class Ui_Modify(object):
    def setupUi(self, Modify):
        if not Modify.objectName():
            Modify.setObjectName(u"Modify")
        Modify.resize(654, 565)
        self.verticalLayout = QVBoxLayout(Modify)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Modify)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(Modify)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.groupBox_3 = QGroupBox(self.frame_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.tableWidget = QTableWidget(self.groupBox_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_7.addWidget(self.tableWidget)

        self.slideframe = QFrame(self.groupBox_3)
        self.slideframe.setObjectName(u"slideframe")
        self.slideframe.setMaximumSize(QSize(16777215, 0))
        self.slideframe.setFrameShape(QFrame.StyledPanel)
        self.slideframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.slideframe)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.msg = QLabel(self.slideframe)
        self.msg.setObjectName(u"msg")

        self.verticalLayout_8.addWidget(self.msg)


        self.verticalLayout_7.addWidget(self.slideframe)


        self.horizontalLayout.addWidget(self.groupBox_3)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.groupBox_2 = QGroupBox(self.frame_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 2, 2, 2)
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/images/images/folder-saved-search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addWidget(self.groupBox_2)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.groupBox = QGroupBox(self.frame_5)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.male = QRadioButton(self.groupBox)
        self.male.setObjectName(u"male")

        self.horizontalLayout_3.addWidget(self.male)

        self.female = QRadioButton(self.groupBox)
        self.female.setObjectName(u"female")

        self.horizontalLayout_3.addWidget(self.female)

        self.tohide = QRadioButton(self.groupBox)
        self.tohide.setObjectName(u"tohide")

        self.horizontalLayout_3.addWidget(self.tohide)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)

        self.nom = QLineEdit(self.groupBox)
        self.nom.setObjectName(u"nom")

        self.gridLayout.addWidget(self.nom, 1, 1, 1, 1)

        self.ncin = QLineEdit(self.groupBox)
        self.ncin.setObjectName(u"ncin")

        self.gridLayout.addWidget(self.ncin, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.age = QLineEdit(self.groupBox)
        self.age.setObjectName(u"age")

        self.horizontalLayout_4.addWidget(self.age)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.prenom = QLineEdit(self.groupBox)
        self.prenom.setObjectName(u"prenom")

        self.gridLayout.addWidget(self.prenom, 2, 1, 1, 1)

        self.quartier = QComboBox(self.groupBox)
        self.quartier.setObjectName(u"quartier")

        self.gridLayout.addWidget(self.quartier, 0, 3, 1, 1)

        self.profession = QComboBox(self.groupBox)
        self.profession.setObjectName(u"profession")

        self.gridLayout.addWidget(self.profession, 1, 3, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.btnmodifier = QPushButton(self.frame_7)
        self.btnmodifier.setObjectName(u"btnmodifier")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/reload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnmodifier.setIcon(icon1)
        self.btnmodifier.setIconSize(QSize(23, 23))

        self.horizontalLayout_5.addWidget(self.btnmodifier, 0, Qt.AlignLeft)

        self.btnsupprimer = QPushButton(self.frame_7)
        self.btnsupprimer.setObjectName(u"btnsupprimer")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/gtk-delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnsupprimer.setIcon(icon2)
        self.btnsupprimer.setIconSize(QSize(23, 23))

        self.horizontalLayout_5.addWidget(self.btnsupprimer, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_7)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Modify)

        QMetaObject.connectSlotsByName(Modify)
    # setupUi

    def retranslateUi(self, Modify):
        Modify.setWindowTitle(QCoreApplication.translate("Modify", u"Form", None))
        self.label.setText(QCoreApplication.translate("Modify", u"Modifier / Supprimer Un Patient", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Modify", u"Patient Enregistrez", None))
        self.msg.setText(QCoreApplication.translate("Modify", u"Error : Patient with information {} not found", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Modify", u"Recherche", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Modify", u"rechercher un patient", None))
        self.pushButton.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Modify", u"GroupBox", None))
        self.male.setText(QCoreApplication.translate("Modify", u"M", None))
        self.female.setText(QCoreApplication.translate("Modify", u"F", None))
        self.tohide.setText(QCoreApplication.translate("Modify", u"x", None))
        self.label_4.setText(QCoreApplication.translate("Modify", u"PRENOM", None))
        self.label_3.setText(QCoreApplication.translate("Modify", u"NOM", None))
        self.label_6.setText(QCoreApplication.translate("Modify", u"SEX", None))
        self.label_8.setText(QCoreApplication.translate("Modify", u"PROFESSION", None))
        self.label_2.setText(QCoreApplication.translate("Modify", u"NCIN", None))
        self.label_5.setText(QCoreApplication.translate("Modify", u"AGE", None))
        self.label_7.setText(QCoreApplication.translate("Modify", u"R\u00c9SIDENCE", None))
        self.quartier.setPlaceholderText(QCoreApplication.translate("Modify", u"R\u00e9sidence du patient", None))
        self.profession.setPlaceholderText(QCoreApplication.translate("Modify", u"profession du patient", None))
        self.btnmodifier.setText(QCoreApplication.translate("Modify", u"Modifier", None))
        self.btnsupprimer.setText(QCoreApplication.translate("Modify", u"Supprimer", None))
    # retranslateUi

