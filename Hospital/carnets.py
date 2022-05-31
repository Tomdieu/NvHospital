# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'carnets.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Carnet(object):
    def setupUi(self, Carnet):
        if not Carnet.objectName():
            Carnet.setObjectName(u"Carnet")
        Carnet.resize(736, 613)
        self.verticalLayout = QVBoxLayout(Carnet)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.frame = QFrame(Carnet)
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

        self.frame_2 = QFrame(Carnet)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.tables = QComboBox(self.frame_5)
        self.tables.setObjectName(u"tables")

        self.horizontalLayout_3.addWidget(self.tables)


        self.verticalLayout_2.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.tableWidget = QTableWidget(self.frame_6)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_4.addWidget(self.tableWidget)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.textEdit = QTextEdit(self.frame_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"	background:transparent;\n"
"	border:1px solid rgb(171,171,171);\n"
"}")

        self.verticalLayout_3.addWidget(self.textEdit)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Carnet)

        QMetaObject.connectSlotsByName(Carnet)
    # setupUi

    def retranslateUi(self, Carnet):
        Carnet.setWindowTitle(QCoreApplication.translate("Carnet", u"Form", None))
        self.label.setText(QCoreApplication.translate("Carnet", u"Carnets Des Patients", None))
        self.label_2.setText(QCoreApplication.translate("Carnet", u"Table :", None))
    # retranslateUi

