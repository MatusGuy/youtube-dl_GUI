# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mateus\Documents\python\youtubedl_GUI_pyqt\youtubedl_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 395)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(531, 395))
        MainWindow.setMaximumSize(QtCore.QSize(531, 395))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\mateus\\Documents\\python\\youtubedl_GUI_pyqt\\assets/ytdl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.MainWidget = QtWidgets.QWidget(MainWindow)
        self.MainWidget.setObjectName("MainWidget")
        self.InputGroup = QtWidgets.QGroupBox(self.MainWidget)
        self.InputGroup.setGeometry(QtCore.QRect(10, 10, 511, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.InputGroup.setFont(font)
        self.InputGroup.setCheckable(False)
        self.InputGroup.setObjectName("InputGroup")
        self.UrlLabel = QtWidgets.QLabel(self.InputGroup)
        self.UrlLabel.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.UrlLabel.setObjectName("UrlLabel")
        self.UrlTextBox = QtWidgets.QLineEdit(self.InputGroup)
        self.UrlTextBox.setGeometry(QtCore.QRect(90, 30, 411, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.UrlTextBox.setFont(font)
        self.UrlTextBox.setWhatsThis("")
        self.UrlTextBox.setInputMask("")
        self.UrlTextBox.setText("")
        self.UrlTextBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.UrlTextBox.setObjectName("UrlTextBox")
        self.ConfigGroup = QtWidgets.QGroupBox(self.MainWidget)
        self.ConfigGroup.setGeometry(QtCore.QRect(10, 90, 511, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.ConfigGroup.setFont(font)
        self.ConfigGroup.setFlat(False)
        self.ConfigGroup.setObjectName("ConfigGroup")
        self.MediaType = QtWidgets.QWidget(self.ConfigGroup)
        self.MediaType.setGeometry(QtCore.QRect(10, 20, 491, 41))
        self.MediaType.setObjectName("MediaType")
        self.AudioOption = QtWidgets.QRadioButton(self.MediaType)
        self.AudioOption.setGeometry(QtCore.QRect(180, 10, 91, 21))
        self.AudioOption.setObjectName("AudioOption")
        self.VideoOption = QtWidgets.QRadioButton(self.MediaType)
        self.VideoOption.setGeometry(QtCore.QRect(60, 10, 111, 20))
        self.VideoOption.setObjectName("VideoOption")
        self.Label = QtWidgets.QLabel(self.MediaType)
        self.Label.setGeometry(QtCore.QRect(10, 10, 41, 21))
        self.Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Label.setObjectName("Label")
        self.OutputGroup = QtWidgets.QGroupBox(self.MainWidget)
        self.OutputGroup.setGeometry(QtCore.QRect(10, 170, 511, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.OutputGroup.setFont(font)
        self.OutputGroup.setObjectName("OutputGroup")
        self.DestinationButton = QtWidgets.QPushButton(self.OutputGroup)
        self.DestinationButton.setGeometry(QtCore.QRect(80, 30, 41, 21))
        self.DestinationButton.setObjectName("DestinationButton")
        self.DestinationLabel = QtWidgets.QLabel(self.OutputGroup)
        self.DestinationLabel.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.DestinationLabel.setObjectName("DestinationLabel")
        self.DestinationInput = QtWidgets.QLineEdit(self.OutputGroup)
        self.DestinationInput.setGeometry(QtCore.QRect(130, 30, 371, 21))
        self.DestinationInput.setReadOnly(True)
        self.DestinationInput.setObjectName("DestinationInput")
        self.ConsoleWidget = QtWidgets.QPlainTextEdit(self.MainWidget)
        self.ConsoleWidget.setEnabled(True)
        self.ConsoleWidget.setGeometry(QtCore.QRect(10, 380, 511, 241))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.ConsoleWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.ConsoleWidget.setFont(font)
        self.ConsoleWidget.setReadOnly(True)
        self.ConsoleWidget.setPlainText("")
        self.ConsoleWidget.setObjectName("ConsoleWidget")
        self.ViewConsole = QtWidgets.QCheckBox(self.MainWidget)
        self.ViewConsole.setGeometry(QtCore.QRect(10, 340, 131, 20))
        self.ViewConsole.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ViewConsole.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ViewConsole.setObjectName("ViewConsole")
        self.ConsoleSeperation = QtWidgets.QFrame(self.MainWidget)
        self.ConsoleSeperation.setGeometry(QtCore.QRect(10, 320, 511, 16))
        self.ConsoleSeperation.setFrameShape(QtWidgets.QFrame.HLine)
        self.ConsoleSeperation.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ConsoleSeperation.setObjectName("ConsoleSeperation")
        self.widget = QtWidgets.QWidget(self.MainWidget)
        self.widget.setGeometry(QtCore.QRect(10, 250, 511, 71))
        self.widget.setObjectName("widget")
        self.DownloadButton = QtWidgets.QCommandLinkButton(self.widget)
        self.DownloadButton.setGeometry(QtCore.QRect(0, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.DownloadButton.setFont(font)
        self.DownloadButton.setObjectName("DownloadButton")
        self.DownloadProgress = QtWidgets.QProgressBar(self.widget)
        self.DownloadProgress.setEnabled(False)
        self.DownloadProgress.setGeometry(QtCore.QRect(130, 20, 371, 21))
        self.DownloadProgress.setProperty("value", 0)
        self.DownloadProgress.setObjectName("DownloadProgress")
        self.FileSizeLabel = QtWidgets.QLabel(self.widget)
        self.FileSizeLabel.setEnabled(False)
        self.FileSizeLabel.setGeometry(QtCore.QRect(350, 50, 151, 21))
        self.FileSizeLabel.setObjectName("FileSizeLabel")
        self.DownloadSpeedLabel = QtWidgets.QLabel(self.widget)
        self.DownloadSpeedLabel.setEnabled(False)
        self.DownloadSpeedLabel.setGeometry(QtCore.QRect(220, 50, 121, 21))
        self.DownloadSpeedLabel.setObjectName("DownloadSpeedLabel")
        self.DwInfoSeperation = QtWidgets.QFrame(self.widget)
        self.DwInfoSeperation.setGeometry(QtCore.QRect(200, 50, 20, 21))
        self.DwInfoSeperation.setFrameShape(QtWidgets.QFrame.VLine)
        self.DwInfoSeperation.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.DwInfoSeperation.setObjectName("DwInfoSeperation")
        self.ETALabel = QtWidgets.QLabel(self.widget)
        self.ETALabel.setEnabled(False)
        self.ETALabel.setGeometry(QtCore.QRect(130, 50, 71, 21))
        self.ETALabel.setObjectName("ETALabel")
        self.DwInfoSeperation_2 = QtWidgets.QFrame(self.widget)
        self.DwInfoSeperation_2.setGeometry(QtCore.QRect(330, 50, 20, 21))
        self.DwInfoSeperation_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.DwInfoSeperation_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.DwInfoSeperation_2.setObjectName("DwInfoSeperation_2")
        MainWindow.setCentralWidget(self.MainWidget)
        self.MenuBar = QtWidgets.QMenuBar(MainWindow)
        self.MenuBar.setEnabled(True)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 531, 26))
        self.MenuBar.setObjectName("MenuBar")
        self.Help = QtWidgets.QMenu(self.MenuBar)
        self.Help.setObjectName("Help")
        MainWindow.setMenuBar(self.MenuBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionContacts = QtWidgets.QAction(MainWindow)
        self.actionContacts.setObjectName("actionContacts")
        self.actionContact = QtWidgets.QAction(MainWindow)
        self.actionContact.setObjectName("actionContact")
        self.actionContact_2 = QtWidgets.QAction(MainWindow)
        self.actionContact_2.setObjectName("actionContact_2")
        self.About = QtWidgets.QAction(MainWindow)
        self.About.setObjectName("About")
        self.actionLinks = QtWidgets.QAction(MainWindow)
        self.actionLinks.setObjectName("actionLinks")
        self.actionTutorials = QtWidgets.QAction(MainWindow)
        self.actionTutorials.setObjectName("actionTutorials")
        self.actionDownload_CMD_version = QtWidgets.QAction(MainWindow)
        self.actionDownload_CMD_version.setObjectName("actionDownload_CMD_version")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.AboutMenu = QtWidgets.QAction(MainWindow)
        self.AboutMenu.setObjectName("AboutMenu")
        self.Tutorials = QtWidgets.QAction(MainWindow)
        self.Tutorials.setObjectName("Tutorials")
        self.Downloads = QtWidgets.QAction(MainWindow)
        self.Downloads.setObjectName("Downloads")
        self.Docs = QtWidgets.QAction(MainWindow)
        self.Docs.setObjectName("Docs")
        self.Links = QtWidgets.QAction(MainWindow)
        self.Links.setObjectName("Links")
        self.Help.addAction(self.AboutMenu)
        self.MenuBar.addAction(self.Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "youtube-dl GUI"))
        self.InputGroup.setTitle(_translate("MainWindow", "Input"))
        self.UrlLabel.setText(_translate("MainWindow", "Youtube URL"))
        self.UrlTextBox.setToolTip(_translate("MainWindow", "Insert the YouTube video/playlist/channel you want to download from."))
        self.ConfigGroup.setTitle(_translate("MainWindow", "Configuration"))
        self.AudioOption.setToolTip(_translate("MainWindow", "Option to download audio-only. Ideal for music"))
        self.AudioOption.setText(_translate("MainWindow", "Audio-only"))
        self.VideoOption.setToolTip(_translate("MainWindow", "Option to download video and audio"))
        self.VideoOption.setText(_translate("MainWindow", "Video + audio"))
        self.Label.setText(_translate("MainWindow", "Export"))
        self.OutputGroup.setTitle(_translate("MainWindow", "Output"))
        self.DestinationButton.setToolTip(_translate("MainWindow", "Select the output\'s destination"))
        self.DestinationButton.setText(_translate("MainWindow", "Select"))
        self.DestinationLabel.setText(_translate("MainWindow", "Destination"))
        self.DestinationInput.setToolTip(_translate("MainWindow", "Copy the output path you selected"))
        self.ViewConsole.setToolTip(_translate("MainWindow", "Click to toggle background console output view"))
        self.ViewConsole.setText(_translate("MainWindow", "Console output"))
        self.DownloadButton.setToolTip(_translate("MainWindow", "Finally, download!"))
        self.DownloadButton.setText(_translate("MainWindow", "Download!"))
        self.FileSizeLabel.setText(_translate("MainWindow", "Total file size:"))
        self.DownloadSpeedLabel.setText(_translate("MainWindow", "Speed:"))
        self.ETALabel.setText(_translate("MainWindow", "ETA:"))
        self.Help.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionContacts.setText(_translate("MainWindow", "Contact"))
        self.actionContact.setText(_translate("MainWindow", "Contact"))
        self.actionContact_2.setText(_translate("MainWindow", "Contact"))
        self.About.setText(_translate("MainWindow", "About"))
        self.actionLinks.setText(_translate("MainWindow", "Links"))
        self.actionTutorials.setText(_translate("MainWindow", "Tutorials"))
        self.actionDownload_CMD_version.setText(_translate("MainWindow", "Downloads"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.AboutMenu.setText(_translate("MainWindow", "About"))
        self.Tutorials.setText(_translate("MainWindow", "Tutorials"))
        self.Downloads.setText(_translate("MainWindow", "Downloads"))
        self.Docs.setText(_translate("MainWindow", "Documentation"))
        self.Links.setText(_translate("MainWindow", "Support links"))
