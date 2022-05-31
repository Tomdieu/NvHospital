# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apropos.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Apropos(object):
    def setupUi(self, Apropos):
        if not Apropos.objectName():
            Apropos.setObjectName(u"Apropos")
        Apropos.resize(463, 416)
        self.verticalLayout = QVBoxLayout(Apropos)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.frame = QFrame(Apropos)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(Apropos)
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
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"	background:transparent;\n"
"	color:black;\n"
"	border:1px solid rgb(171,171,171);\n"
"}")

        self.verticalLayout_3.addWidget(self.textEdit)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Apropos)

        QMetaObject.connectSlotsByName(Apropos)
    # setupUi

    def retranslateUi(self, Apropos):
        Apropos.setWindowTitle(QCoreApplication.translate("Apropos", u"Form", None))
        self.label.setText(QCoreApplication.translate("Apropos", u"\u00c0 propos de Naspitoo", None))
    # retranslateUi

