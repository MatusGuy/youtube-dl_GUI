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
        AdditionalSwitches.setWindowModality(QtCore.Qt.WindowModal)
        AdditionalSwitches.resize(424, 254)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/ytdl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AdditionalSwitches.setWindowIcon(icon)
        AdditionalSwitches.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.verticalLayout = QtWidgets.QVBoxLayout(AdditionalSwitches)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.TextEdit.setPlainText("")
        self.TextEdit.setObjectName("TextEdit")
        self.gridLayout.addWidget(self.TextEdit, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.GroupBox)

        self.retranslateUi(AdditionalSwitches)
        QtCore.QMetaObject.connectSlotsByName(AdditionalSwitches)

    def retranslateUi(self, AdditionalSwitches):
        _translate = QtCore.QCoreApplication.translate
        AdditionalSwitches.setWindowTitle(_translate("AdditionalSwitches", "Additional switches"))
        self.GroupBox.setTitle(_translate("AdditionalSwitches", "Additional switches"))
