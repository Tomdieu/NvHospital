# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parametre.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import images_rc

class Ui_Parametre(object):
    def setupUi(self, Parametre):
        if not Parametre.objectName():
            Parametre.setObjectName(u"Parametre")
        Parametre.resize(545, 456)
        self.verticalLayout = QVBoxLayout(Parametre)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.frame = QFrame(Parametre)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(Parametre)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"QFrame#frame_3{\n"
"	border:0px solid rgb(171,171,171);\n"
"	border-radius:10px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.langFranc = QRadioButton(self.frame_3)
        self.langFranc.setObjectName(u"langFranc")
        self.langFranc.setChecked(True)

        self.horizontalLayout_2.addWidget(self.langFranc)

        self.langEng = QRadioButton(self.frame_3)
        self.langEng.setObjectName(u"langEng")

        self.horizontalLayout_2.addWidget(self.langEng)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame#frame_5{\n"
"	border:0px solid rgb(171,171,171);\n"
"	border-radius:10px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 3, 2, 3)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.btnAide = QPushButton(self.frame_5)
        self.btnAide.setObjectName(u"btnAide")

        self.horizontalLayout_3.addWidget(self.btnAide)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.frame_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.slidehelp = QFrame(Parametre)
        self.slidehelp.setObjectName(u"slidehelp")
        sizePolicy.setHeightForWidth(self.slidehelp.sizePolicy().hasHeightForWidth())
        self.slidehelp.setSizePolicy(sizePolicy)
        self.slidehelp.setMaximumSize(QSize(16777215, 0))
        self.slidehelp.setFrameShape(QFrame.StyledPanel)
        self.slidehelp.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.slidehelp)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.slidedown = QPushButton(self.slidehelp)
        self.slidedown.setObjectName(u"slidedown")
        icon = QIcon()
        icon.addFile(u":/images/images/arrow-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.slidedown.setIcon(icon)

        self.verticalLayout_3.addWidget(self.slidedown, 0, Qt.AlignLeft|Qt.AlignTop)

        self.textEdit = QTextEdit(self.slidehelp)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"	background:transparent;\n"
"}")

        self.verticalLayout_3.addWidget(self.textEdit)


        self.verticalLayout.addWidget(self.slidehelp)


        self.retranslateUi(Parametre)

        QMetaObject.connectSlotsByName(Parametre)
    # setupUi

    def retranslateUi(self, Parametre):
        Parametre.setWindowTitle(QCoreApplication.translate("Parametre", u"Form", None))
        self.label.setText(QCoreApplication.translate("Parametre", u"Param\u00e8tre", None))
        self.label_2.setText(QCoreApplication.translate("Parametre", u"Language : ", None))
        self.langFranc.setText(QCoreApplication.translate("Parametre", u"Fran\u00e7ais", None))
        self.langEng.setText(QCoreApplication.translate("Parametre", u"Englais", None))
        self.label_3.setText("")
        self.btnAide.setText(QCoreApplication.translate("Parametre", u"Aide", None))
        self.label_4.setText("")
        self.slidedown.setText("")
    # retranslateUi

