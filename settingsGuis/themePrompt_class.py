# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsGuis/themePrompt.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangeTheme(object):
    def setupUi(self, ChangeTheme):
        ChangeTheme.setObjectName("ChangeTheme")
        ChangeTheme.setWindowModality(QtCore.Qt.WindowModal)
        ChangeTheme.resize(121, 141)
        ChangeTheme.setMinimumSize(QtCore.QSize(121, 141))
        ChangeTheme.setMaximumSize(QtCore.QSize(121, 141))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        ChangeTheme.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("settingsGuis\\../assets/ytdl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ChangeTheme.setWindowIcon(icon)
        self.Light = QtWidgets.QRadioButton(ChangeTheme)
        self.Light.setGeometry(QtCore.QRect(10, 60, 101, 17))
        self.Light.setObjectName("Light")
        self.Label = QtWidgets.QLabel(ChangeTheme)
        self.Label.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Label.setFont(font)
        self.Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Label.setObjectName("Label")
        self.Dark = QtWidgets.QRadioButton(ChangeTheme)
        self.Dark.setGeometry(QtCore.QRect(10, 80, 101, 17))
        self.Dark.setObjectName("Dark")
        self.Seperation = QtWidgets.QFrame(ChangeTheme)
        self.Seperation.setGeometry(QtCore.QRect(10, 40, 101, 20))
        self.Seperation.setFrameShape(QtWidgets.QFrame.HLine)
        self.Seperation.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Seperation.setObjectName("Seperation")
        self.OKBtn = QtWidgets.QPushButton(ChangeTheme)
        self.OKBtn.setGeometry(QtCore.QRect(10, 110, 41, 23))
        self.OKBtn.setObjectName("OKBtn")
        self.CancelBtn = QtWidgets.QPushButton(ChangeTheme)
        self.CancelBtn.setGeometry(QtCore.QRect(70, 110, 41, 23))
        self.CancelBtn.setObjectName("CancelBtn")

        self.retranslateUi(ChangeTheme)
        QtCore.QMetaObject.connectSlotsByName(ChangeTheme)

    def retranslateUi(self, ChangeTheme):
        _translate = QtCore.QCoreApplication.translate
        ChangeTheme.setWindowTitle(_translate("ChangeTheme", "Theme"))
        self.Light.setText(_translate("ChangeTheme", "Light"))
        self.Label.setText(_translate("ChangeTheme", "Theme"))
        self.Dark.setText(_translate("ChangeTheme", "Dark"))
        self.OKBtn.setText(_translate("ChangeTheme", "OK"))
        self.CancelBtn.setText(_translate("ChangeTheme", "Cancel"))