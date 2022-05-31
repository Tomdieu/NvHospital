# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patientsaved.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_PatientSaved(object):
    def setupUi(self, PatientSaved):
        if not PatientSaved.objectName():
            PatientSaved.setObjectName(u"PatientSaved")
        PatientSaved.resize(607, 497)
        self.verticalLayout = QVBoxLayout(PatientSaved)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(PatientSaved)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(PatientSaved)
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
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.tableWidget = QTableWidget(self.frame_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_3.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(PatientSaved)

        QMetaObject.connectSlotsByName(PatientSaved)
    # setupUi

    def retranslateUi(self, PatientSaved):
        PatientSaved.setWindowTitle(QCoreApplication.translate("PatientSaved", u"Form", None))
        self.label.setText(QCoreApplication.translate("PatientSaved", u"Patient Enregistrez", None))
    # retranslateUi

