# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addswitches_simple.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdditionalSwitches(object):
    def setupUi(self, AdditionalSwitches):
        AdditionalSwitches.setObjectName("AdditionalSwitches")
        AdditionalSwitches.setWindowModality(QtCore.Qt.ApplicationModal)
        AdditionalSwitches.resize(468, 294)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/ytdl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AdditionalSwitches.setWindowIcon(icon)
        AdditionalSwitches.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        AdditionalSwitches.setSizeGripEnabled(True)
        AdditionalSwitches.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(AdditionalSwitches)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OkButton = QtWidgets.QPushButton(AdditionalSwitches)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OkButton.sizePolicy().hasHeightForWidth())
        self.OkButton.setSizePolicy(sizePolicy)
        self.OkButton.setObjectName("OkButton")
        self.gridLayout_2.addWidget(self.OkButton, 1, 3, 1, 1)
        self.GroupBox = QtWidgets.QGroupBox(AdditionalSwitches)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.GroupBox.sizePolicy().hasHeightForWidth())
        self.GroupBox.setSizePolicy(sizePolicy)
        self.GroupBox.setObjectName("GroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.GroupBox)
        self.gridLayout.setContentsMargins(-1, 11, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.TextEdit = QtWidgets.QPlainTextEdit(self.GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.TextEdit.sizePolicy().hasHeightForWidth())
        self.TextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.TextEdit.setFont(font)
        self.TextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.TextEdit.setPlainText("")
        self.TextEdit.setObjectName("TextEdit")
        self.gridLayout.addWidget(self.TextEdit, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.GroupBox, 0, 0, 1, 4)
        self.HelpMenu = QtWidgets.QToolButton(AdditionalSwitches)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HelpMenu.sizePolicy().hasHeightForWidth())
        self.HelpMenu.setSizePolicy(sizePolicy)
        self.HelpMenu.setMinimumSize(QtCore.QSize(0, 0))
        self.HelpMenu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../assets/help_index.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HelpMenu.setIcon(icon1)
        self.HelpMenu.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.HelpMenu.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.HelpMenu.setObjectName("HelpMenu")
        self.gridLayout_2.addWidget(self.HelpMenu, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 2)

        self.retranslateUi(AdditionalSwitches)
        QtCore.QMetaObject.connectSlotsByName(AdditionalSwitches)

    def retranslateUi(self, AdditionalSwitches):
        _translate = QtCore.QCoreApplication.translate
        AdditionalSwitches.setWindowTitle(_translate("AdditionalSwitches", "Additional switches"))
        self.OkButton.setText(_translate("AdditionalSwitches", "OK"))
        self.GroupBox.setTitle(_translate("AdditionalSwitches", "Additional youtube-dl command line switches"))
        self.HelpMenu.setText(_translate("AdditionalSwitches", "Help"))
