# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recapitulatif.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import images_rc

class Ui_Recapitulatif(object):
    def setupUi(self, Recapitulatif):
        if not Recapitulatif.objectName():
            Recapitulatif.setObjectName(u"Recapitulatif")
        Recapitulatif.resize(815, 672)
        self.verticalLayout = QVBoxLayout(Recapitulatif)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.frame_2 = QFrame(Recapitulatif)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame = QFrame(Recapitulatif)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 779, 1254))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 121))
        self.frame_3.setMaximumSize(QSize(16777215, 121))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.sextable = QTableWidget(self.groupBox)
        if (self.sextable.columnCount() < 1):
            self.sextable.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.sextable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.sextable.rowCount() < 2):
            self.sextable.setRowCount(2)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.sextable.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.sextable.setVerticalHeaderItem(1, __qtablewidgetitem2)
        self.sextable.setObjectName(u"sextable")

        self.verticalLayout_4.addWidget(self.sextable)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 211))
        self.frame_4.setMaximumSize(QSize(16777215, 211))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.groupBox_2 = QGroupBox(self.frame_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.agetable = QTableWidget(self.groupBox_2)
        if (self.agetable.columnCount() < 1):
            self.agetable.setColumnCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.agetable.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        if (self.agetable.rowCount() < 5):
            self.agetable.setRowCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.agetable.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.agetable.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.agetable.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.agetable.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.agetable.setVerticalHeaderItem(4, __qtablewidgetitem8)
        self.agetable.setObjectName(u"agetable")

        self.verticalLayout_5.addWidget(self.agetable)


        self.horizontalLayout_2.addWidget(self.groupBox_2)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 241))
        self.frame_5.setMaximumSize(QSize(16777215, 241))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.groupBox_3 = QGroupBox(self.frame_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.professiontable = QTableWidget(self.groupBox_3)
        if (self.professiontable.columnCount() < 1):
            self.professiontable.setColumnCount(1)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.professiontable.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        if (self.professiontable.rowCount() < 6):
            self.professiontable.setRowCount(6)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.professiontable.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.professiontable.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.professiontable.setVerticalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.professiontable.setVerticalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.professiontable.setVerticalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.professiontable.setVerticalHeaderItem(5, __qtablewidgetitem15)
        self.professiontable.setObjectName(u"professiontable")

        self.horizontalLayout_4.addWidget(self.professiontable)


        self.horizontalLayout_3.addWidget(self.groupBox_3)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 181))
        self.frame_6.setMaximumSize(QSize(16777215, 181))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.groupBox_4 = QGroupBox(self.frame_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.residencetable = QTableWidget(self.groupBox_4)
        if (self.residencetable.columnCount() < 1):
            self.residencetable.setColumnCount(1)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.residencetable.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        if (self.residencetable.rowCount() < 4):
            self.residencetable.setRowCount(4)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.residencetable.setVerticalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.residencetable.setVerticalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.residencetable.setVerticalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.residencetable.setVerticalHeaderItem(3, __qtablewidgetitem20)
        self.residencetable.setObjectName(u"residencetable")

        self.horizontalLayout_6.addWidget(self.residencetable)


        self.horizontalLayout_5.addWidget(self.groupBox_4)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 271))
        self.frame_7.setMaximumSize(QSize(16777215, 271))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.groupBox_5 = QGroupBox(self.frame_7)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.interventiontable = QTableWidget(self.groupBox_5)
        if (self.interventiontable.columnCount() < 1):
            self.interventiontable.setColumnCount(1)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.interventiontable.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        if (self.interventiontable.rowCount() < 7):
            self.interventiontable.setRowCount(7)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.interventiontable.setVerticalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.interventiontable.setVerticalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.interventiontable.setVerticalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.interventiontable.setVerticalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.interventiontable.setVerticalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.interventiontable.setVerticalHeaderItem(5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.interventiontable.setVerticalHeaderItem(6, __qtablewidgetitem28)
        self.interventiontable.setObjectName(u"interventiontable")

        self.horizontalLayout_8.addWidget(self.interventiontable)


        self.horizontalLayout_7.addWidget(self.groupBox_5)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 181))
        self.frame_8.setMaximumSize(QSize(16777215, 181))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.groupBox_6 = QGroupBox(self.frame_8)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.caotable = QTableWidget(self.groupBox_6)
        if (self.caotable.columnCount() < 1):
            self.caotable.setColumnCount(1)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.caotable.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        if (self.caotable.rowCount() < 4):
            self.caotable.setRowCount(4)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.caotable.setVerticalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.caotable.setVerticalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.caotable.setVerticalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.caotable.setVerticalHeaderItem(3, __qtablewidgetitem33)
        self.caotable.setObjectName(u"caotable")

        self.horizontalLayout_10.addWidget(self.caotable)


        self.horizontalLayout_9.addWidget(self.groupBox_6)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_12.addWidget(self.scrollArea)

        self.slideframe = QFrame(self.frame)
        self.slideframe.setObjectName(u"slideframe")
        self.slideframe.setMaximumSize(QSize(0, 16777215))
        self.slideframe.setFrameShape(QFrame.StyledPanel)
        self.slideframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.slideframe)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.frame_11 = QFrame(self.slideframe)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.toolBarWidget = QFrame(self.frame_11)
        self.toolBarWidget.setObjectName(u"toolBarWidget")
        self.toolBarWidget.setFrameShape(QFrame.StyledPanel)
        self.toolBarWidget.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.toolBarWidget)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_14.setSpacing(1)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(1, 1, 1, 1)
        self.btnundo = QPushButton(self.frame_12)
        self.btnundo.setObjectName(u"btnundo")
        icon = QIcon()
        icon.addFile(u":/images/images/edit-undo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnundo.setIcon(icon)

        self.horizontalLayout_14.addWidget(self.btnundo)

        self.btnredo = QPushButton(self.frame_12)
        self.btnredo.setObjectName(u"btnredo")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/edit-redo-symbolic.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnredo.setIcon(icon1)

        self.horizontalLayout_14.addWidget(self.btnredo)

        self.btncut = QPushButton(self.frame_12)
        self.btncut.setObjectName(u"btncut")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/edit-cut.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btncut.setIcon(icon2)

        self.horizontalLayout_14.addWidget(self.btncut)

        self.btncopy = QPushButton(self.frame_12)
        self.btncopy.setObjectName(u"btncopy")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/edit-copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btncopy.setIcon(icon3)

        self.horizontalLayout_14.addWidget(self.btncopy)

        self.btnpaste = QPushButton(self.frame_12)
        self.btnpaste.setObjectName(u"btnpaste")
        icon4 = QIcon()
        icon4.addFile(u":/images/images/edit-paste.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnpaste.setIcon(icon4)

        self.horizontalLayout_14.addWidget(self.btnpaste)

        self.btnbold = QPushButton(self.frame_12)
        self.btnbold.setObjectName(u"btnbold")
        icon5 = QIcon()
        icon5.addFile(u":/images/images/format-text-bold.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnbold.setIcon(icon5)
        self.btnbold.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.btnbold)

        self.btnitalic = QPushButton(self.frame_12)
        self.btnitalic.setObjectName(u"btnitalic")
        icon6 = QIcon()
        icon6.addFile(u":/images/images/format-text-italic.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnitalic.setIcon(icon6)
        self.btnitalic.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.btnitalic)

        self.btnunderline = QPushButton(self.frame_12)
        self.btnunderline.setObjectName(u"btnunderline")
        icon7 = QIcon()
        icon7.addFile(u":/images/images/format-text-underline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnunderline.setIcon(icon7)
        self.btnunderline.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.btnunderline)

        self.btnleft = QPushButton(self.frame_12)
        self.btnleft.setObjectName(u"btnleft")
        icon8 = QIcon()
        icon8.addFile(u":/images/images/textleft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnleft.setIcon(icon8)
        self.btnleft.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.btnleft)

        self.btncenter = QPushButton(self.frame_12)
        self.btncenter.setObjectName(u"btncenter")
        icon9 = QIcon()
        icon9.addFile(u":/images/images/textcenter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btncenter.setIcon(icon9)
        self.btncenter.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.btncenter)

        self.btnright = QPushButton(self.frame_12)
        self.btnright.setObjectName(u"btnright")
        icon10 = QIcon()
        icon10.addFile(u":/images/images/textright.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnright.setIcon(icon10)
        self.btnright.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.btnright)

        self.btnjustify = QPushButton(self.frame_12)
        self.btnjustify.setObjectName(u"btnjustify")
        icon11 = QIcon()
        icon11.addFile(u":/images/images/textjustify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnjustify.setIcon(icon11)
        self.btnjustify.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.btnjustify)

        self.btnindent = QPushButton(self.frame_12)
        self.btnindent.setObjectName(u"btnindent")
        icon12 = QIcon()
        icon12.addFile(u":/images/images/format-indent-more.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnindent.setIcon(icon12)

        self.horizontalLayout_14.addWidget(self.btnindent)

        self.btnunindent = QPushButton(self.frame_12)
        self.btnunindent.setObjectName(u"btnunindent")
        icon13 = QIcon()
        icon13.addFile(u":/images/images/format-indent-less.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnunindent.setIcon(icon13)

        self.horizontalLayout_14.addWidget(self.btnunindent)

        self.btncolor = QPushButton(self.frame_12)
        self.btncolor.setObjectName(u"btncolor")
        icon14 = QIcon()
        icon14.addFile(u":/images/images/color-picker.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btncolor.setIcon(icon14)

        self.horizontalLayout_14.addWidget(self.btncolor)

        self.btnundercolor = QPushButton(self.frame_12)
        self.btnundercolor.setObjectName(u"btnundercolor")
        icon15 = QIcon()
        icon15.addFile(u":/images/images/textundercolor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnundercolor.setIcon(icon15)

        self.horizontalLayout_14.addWidget(self.btnundercolor)

        self.toolBarLayout = QFrame(self.frame_12)
        self.toolBarLayout.setObjectName(u"toolBarLayout")
        self.toolBarLayout.setFrameShape(QFrame.StyledPanel)
        self.toolBarLayout.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.toolBarLayout)


        self.verticalLayout_7.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(1, 1, 1, 1)
        self.combostyle = QComboBox(self.frame_13)
        self.combostyle.setObjectName(u"combostyle")
        self.combostyle.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_13.addWidget(self.combostyle)

        self.fontComboBox = QFontComboBox(self.frame_13)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.horizontalLayout_13.addWidget(self.fontComboBox, 0, Qt.AlignLeft)

        self.fontSize = QComboBox(self.frame_13)
        self.fontSize.setObjectName(u"fontSize")
        self.fontSize.setMaximumSize(QSize(50, 16777215))
        self.fontSize.setEditable(True)

        self.horizontalLayout_13.addWidget(self.fontSize, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addWidget(self.frame_13)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.textEdit = QTextEdit(self.slideframe)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)


        self.horizontalLayout_12.addWidget(self.slideframe)


        self.verticalLayout.addWidget(self.frame)

        self.frame_9 = QFrame(Recapitulatif)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.sauvegarder = QPushButton(self.frame_9)
        self.sauvegarder.setObjectName(u"sauvegarder")
        icon16 = QIcon()
        icon16.addFile(u":/images/images/document-save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sauvegarder.setIcon(icon16)

        self.horizontalLayout_11.addWidget(self.sauvegarder)

        self.imprimer = QPushButton(self.frame_9)
        self.imprimer.setObjectName(u"imprimer")
        icon17 = QIcon()
        icon17.addFile(u":/images/images/document-print.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.imprimer.setIcon(icon17)
        self.imprimer.setCheckable(False)

        self.horizontalLayout_11.addWidget(self.imprimer)

        self.modifier = QPushButton(self.frame_9)
        self.modifier.setObjectName(u"modifier")

        self.horizontalLayout_11.addWidget(self.modifier)


        self.verticalLayout.addWidget(self.frame_9)


        self.retranslateUi(Recapitulatif)

        QMetaObject.connectSlotsByName(Recapitulatif)
    # setupUi

    def retranslateUi(self, Recapitulatif):
        Recapitulatif.setWindowTitle(QCoreApplication.translate("Recapitulatif", u"Form", None))
        self.label.setText(QCoreApplication.translate("Recapitulatif", u"Recapitulatif Des Consulation", None))
        self.groupBox.setTitle(QCoreApplication.translate("Recapitulatif", u"SEX", None))
        ___qtablewidgetitem = self.sextable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Recapitulatif", u"EFFECTIF", None));
        ___qtablewidgetitem1 = self.sextable.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Recapitulatif", u"Masculin", None));
        ___qtablewidgetitem2 = self.sextable.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Recapitulatif", u"Feminin", None));
        self.groupBox_2.setTitle(QCoreApplication.translate("Recapitulatif", u"AGE", None))
        ___qtablewidgetitem3 = self.agetable.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Recapitulatif", u"EFFECTIF", None));
        ___qtablewidgetitem4 = self.agetable.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Recapitulatif", u"0-5", None));
        ___qtablewidgetitem5 = self.agetable.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Recapitulatif", u"6-17", None));
        ___qtablewidgetitem6 = self.agetable.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Recapitulatif", u"18-35", None));
        ___qtablewidgetitem7 = self.agetable.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Recapitulatif", u"36-45", None));
        ___qtablewidgetitem8 = self.agetable.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Recapitulatif", u"+45", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("Recapitulatif", u"Activite Professionnelle", None))
        ___qtablewidgetitem9 = self.professiontable.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Recapitulatif", u"EFFECTIF", None));
        ___qtablewidgetitem10 = self.professiontable.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Recapitulatif", u"Cultivateur/Cultivatrice ", None));
        ___qtablewidgetitem11 = self.professiontable.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Recapitulatif", u"\u00c9l\u00e8ve", None));
        ___qtablewidgetitem12 = self.professiontable.verticalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Recapitulatif", u"Fonctionnaire", None));
        ___qtablewidgetitem13 = self.professiontable.verticalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Recapitulatif", u"Commercant(s)", None));
        ___qtablewidgetitem14 = self.professiontable.verticalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Recapitulatif", u"Menag\u00e8re", None));
        ___qtablewidgetitem15 = self.professiontable.verticalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Recapitulatif", u"Autres", None));
        self.groupBox_4.setTitle(QCoreApplication.translate("Recapitulatif", u"Lieu de Residence", None))
        ___qtablewidgetitem16 = self.residencetable.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Recapitulatif", u"EFFECTIF", None));
        ___qtablewidgetitem17 = self.residencetable.verticalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Recapitulatif", u"Tonga", None));
        ___qtablewidgetitem18 = self.residencetable.verticalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Recapitulatif", u"Douala", None));
        ___qtablewidgetitem19 = self.residencetable.verticalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Recapitulatif", u"Yaound\u00e9", None));
        ___qtablewidgetitem20 = self.residencetable.verticalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Recapitulatif", u"Autre", None));
        self.groupBox_5.setTitle(QCoreApplication.translate("Recapitulatif", u"Nature De L'intervention", None))
        ___qtablewidgetitem21 = self.interventiontable.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Recapitulatif", u"EFFECTIF (N\u00b0 PATIENTS)", None));
        ___qtablewidgetitem22 = self.interventiontable.verticalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Recapitulatif", u"D\u00e9tartrage", None));
        ___qtablewidgetitem23 = self.interventiontable.verticalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Recapitulatif", u"Extraction", None));
        ___qtablewidgetitem24 = self.interventiontable.verticalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Recapitulatif", u"Soins Conservateurs", None));
        ___qtablewidgetitem25 = self.interventiontable.verticalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Recapitulatif", u"R\u00e9f\u00e9rence + ordonnance", None));
        ___qtablewidgetitem26 = self.interventiontable.verticalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Recapitulatif", u"Ordonnance", None));
        ___qtablewidgetitem27 = self.interventiontable.verticalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Recapitulatif", u"Conseil (IHBD)", None));
        ___qtablewidgetitem28 = self.interventiontable.verticalHeaderItem(6)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Recapitulatif", u"Decapuchonnage", None));
        self.groupBox_6.setTitle(QCoreApplication.translate("Recapitulatif", u"INDICE CAO", None))
        ___qtablewidgetitem29 = self.caotable.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Recapitulatif", u"EFFECTIF", None));
        ___qtablewidgetitem30 = self.caotable.verticalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Recapitulatif", u"C", None));
        ___qtablewidgetitem31 = self.caotable.verticalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Recapitulatif", u"A", None));
        ___qtablewidgetitem32 = self.caotable.verticalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Recapitulatif", u"O", None));
        ___qtablewidgetitem33 = self.caotable.verticalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Recapitulatif", u"AUTRES", None));
#if QT_CONFIG(tooltip)
        self.btnundo.setToolTip(QCoreApplication.translate("Recapitulatif", u"Undo", None))
#endif // QT_CONFIG(tooltip)
        self.btnundo.setText("")
#if QT_CONFIG(tooltip)
        self.btnredo.setToolTip(QCoreApplication.translate("Recapitulatif", u"Redo", None))
#endif // QT_CONFIG(tooltip)
        self.btnredo.setText("")
#if QT_CONFIG(tooltip)
        self.btncut.setToolTip(QCoreApplication.translate("Recapitulatif", u"Cut", None))
#endif // QT_CONFIG(tooltip)
        self.btncut.setText("")
#if QT_CONFIG(tooltip)
        self.btncopy.setToolTip(QCoreApplication.translate("Recapitulatif", u"copy", None))
#endif // QT_CONFIG(tooltip)
        self.btncopy.setText("")
#if QT_CONFIG(tooltip)
        self.btnpaste.setToolTip(QCoreApplication.translate("Recapitulatif", u"paste", None))
#endif // QT_CONFIG(tooltip)
        self.btnpaste.setText("")
#if QT_CONFIG(tooltip)
        self.btnbold.setToolTip(QCoreApplication.translate("Recapitulatif", u"bold", None))
#endif // QT_CONFIG(tooltip)
        self.btnbold.setText("")
#if QT_CONFIG(shortcut)
        self.btnbold.setShortcut(QCoreApplication.translate("Recapitulatif", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btnitalic.setToolTip(QCoreApplication.translate("Recapitulatif", u"italic", None))
#endif // QT_CONFIG(tooltip)
        self.btnitalic.setText("")
#if QT_CONFIG(shortcut)
        self.btnitalic.setShortcut(QCoreApplication.translate("Recapitulatif", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btnunderline.setToolTip(QCoreApplication.translate("Recapitulatif", u"underline", None))
#endif // QT_CONFIG(tooltip)
        self.btnunderline.setText("")
#if QT_CONFIG(shortcut)
        self.btnunderline.setShortcut(QCoreApplication.translate("Recapitulatif", u"Ctrl+U", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btnleft.setToolTip(QCoreApplication.translate("Recapitulatif", u"Left", None))
#endif // QT_CONFIG(tooltip)
        self.btnleft.setText("")
#if QT_CONFIG(shortcut)
        self.btnleft.setShortcut(QCoreApplication.translate("Recapitulatif", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btncenter.setToolTip(QCoreApplication.translate("Recapitulatif", u"center", None))
#endif // QT_CONFIG(tooltip)
        self.btncenter.setText("")
#if QT_CONFIG(tooltip)
        self.btnright.setToolTip(QCoreApplication.translate("Recapitulatif", u"right", None))
#endif // QT_CONFIG(tooltip)
        self.btnright.setText("")
#if QT_CONFIG(shortcut)
        self.btnright.setShortcut("")
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btnjustify.setToolTip(QCoreApplication.translate("Recapitulatif", u"justify", None))
#endif // QT_CONFIG(tooltip)
        self.btnjustify.setText("")
#if QT_CONFIG(tooltip)
        self.btnindent.setToolTip(QCoreApplication.translate("Recapitulatif", u"indent", None))
#endif // QT_CONFIG(tooltip)
        self.btnindent.setText("")
#if QT_CONFIG(tooltip)
        self.btnunindent.setToolTip(QCoreApplication.translate("Recapitulatif", u"Unindent", None))
#endif // QT_CONFIG(tooltip)
        self.btnunindent.setText("")
#if QT_CONFIG(tooltip)
        self.btncolor.setToolTip(QCoreApplication.translate("Recapitulatif", u"color", None))
#endif // QT_CONFIG(tooltip)
        self.btncolor.setText("")
#if QT_CONFIG(tooltip)
        self.btnundercolor.setToolTip(QCoreApplication.translate("Recapitulatif", u"Underline color", None))
#endif // QT_CONFIG(tooltip)
        self.btnundercolor.setText("")
        self.sauvegarder.setText(QCoreApplication.translate("Recapitulatif", u"Sauvegarder", None))
        self.imprimer.setText(QCoreApplication.translate("Recapitulatif", u"Imprimer le Recapitulatif", None))
        self.modifier.setText(QCoreApplication.translate("Recapitulatif", u"Modifier Le Recapitulatif", None))
    # retranslateUi

