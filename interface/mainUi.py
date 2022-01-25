# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 512)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/ytdl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QToolButton:hover,.QPushButton:hover{\n"
"        background-color: rgb(0, 120, 215)\n"
"}\n"
"\n"
"QDockWidget {\n"
"        background-color: rgb(205, 205, 205);\n"
"        color: rgb(0, 0, 0)\n"
"}")
        self.MainWidget = QtWidgets.QWidget(MainWindow)
        self.MainWidget.setStyleSheet("")
        self.MainWidget.setObjectName("MainWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.MainWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.OutputGroup = QtWidgets.QGroupBox(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OutputGroup.sizePolicy().hasHeightForWidth())
        self.OutputGroup.setSizePolicy(sizePolicy)
        self.OutputGroup.setMaximumSize(QtCore.QSize(16777215, 70))
        self.OutputGroup.setObjectName("OutputGroup")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.OutputGroup)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.DestinationInput = QtWidgets.QLineEdit(self.OutputGroup)
        self.DestinationInput.setObjectName("DestinationInput")
        self.gridLayout_4.addWidget(self.DestinationInput, 0, 2, 1, 1)
        self.DestinationLabel = QtWidgets.QLabel(self.OutputGroup)
        self.DestinationLabel.setObjectName("DestinationLabel")
        self.gridLayout_4.addWidget(self.DestinationLabel, 0, 0, 1, 1)
        self.DestinationButton = QtWidgets.QToolButton(self.OutputGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.DestinationButton.sizePolicy().hasHeightForWidth())
        self.DestinationButton.setSizePolicy(sizePolicy)
        self.DestinationButton.setMinimumSize(QtCore.QSize(24, 26))
        self.DestinationButton.setMaximumSize(QtCore.QSize(24, 25))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../assets/folder_yellow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DestinationButton.setIcon(icon1)
        self.DestinationButton.setObjectName("DestinationButton")
        self.gridLayout_4.addWidget(self.DestinationButton, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.OutputGroup, 2, 0, 1, 1)
        self.ConfigGroup = QtWidgets.QGroupBox(self.MainWidget)
        self.ConfigGroup.setMaximumSize(QtCore.QSize(16777215, 100))
        self.ConfigGroup.setObjectName("ConfigGroup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.ConfigGroup)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.MediaType = QtWidgets.QWidget(self.ConfigGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MediaType.sizePolicy().hasHeightForWidth())
        self.MediaType.setSizePolicy(sizePolicy)
        self.MediaType.setObjectName("MediaType")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.MediaType)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.ExportLabel = QtWidgets.QLabel(self.MediaType)
        self.ExportLabel.setObjectName("ExportLabel")
        self.gridLayout_8.addWidget(self.ExportLabel, 0, 0, 1, 1)
        self.VideoOption = QtWidgets.QRadioButton(self.MediaType)
        self.VideoOption.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.VideoOption.setChecked(True)
        self.VideoOption.setObjectName("VideoOption")
        self.gridLayout_8.addWidget(self.VideoOption, 0, 1, 1, 1)
        self.AudioOption = QtWidgets.QRadioButton(self.MediaType)
        self.AudioOption.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.AudioOption.setObjectName("AudioOption")
        self.gridLayout_8.addWidget(self.AudioOption, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.MediaType, 0, 0, 1, 1)
        self.sep1 = QtWidgets.QFrame(self.ConfigGroup)
        self.sep1.setFrameShape(QtWidgets.QFrame.VLine)
        self.sep1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sep1.setObjectName("sep1")
        self.gridLayout_2.addWidget(self.sep1, 0, 1, 1, 1)
        self.ConfigOutput = QtWidgets.QWidget(self.ConfigGroup)
        self.ConfigOutput.setObjectName("ConfigOutput")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ConfigOutput)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.TemplateLabel = QtWidgets.QLabel(self.ConfigOutput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TemplateLabel.sizePolicy().hasHeightForWidth())
        self.TemplateLabel.setSizePolicy(sizePolicy)
        self.TemplateLabel.setObjectName("TemplateLabel")
        self.gridLayout_3.addWidget(self.TemplateLabel, 0, 0, 1, 1)
        self.RangeLabel = QtWidgets.QLabel(self.ConfigOutput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RangeLabel.sizePolicy().hasHeightForWidth())
        self.RangeLabel.setSizePolicy(sizePolicy)
        self.RangeLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.RangeLabel.setObjectName("RangeLabel")
        self.gridLayout_3.addWidget(self.RangeLabel, 1, 0, 1, 1)
        self.RangeInput = QtWidgets.QLineEdit(self.ConfigOutput)
        self.RangeInput.setMinimumSize(QtCore.QSize(100, 0))
        self.RangeInput.setMaximumSize(QtCore.QSize(100, 16777215))
        self.RangeInput.setObjectName("RangeInput")
        self.gridLayout_3.addWidget(self.RangeInput, 1, 1, 1, 3)
        self.TemplateInput = QtWidgets.QLineEdit(self.ConfigOutput)
        self.TemplateInput.setObjectName("TemplateInput")
        self.gridLayout_3.addWidget(self.TemplateInput, 0, 1, 1, 3)
        self.gridLayout_2.addWidget(self.ConfigOutput, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.ConfigGroup, 1, 0, 1, 1)
        self.InputGroup = QtWidgets.QGroupBox(self.MainWidget)
        self.InputGroup.setMaximumSize(QtCore.QSize(16777215, 70))
        self.InputGroup.setObjectName("InputGroup")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.InputGroup)
        self.gridLayout_5.setContentsMargins(-1, 11, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.UrlLabel = QtWidgets.QLabel(self.InputGroup)
        self.UrlLabel.setObjectName("UrlLabel")
        self.gridLayout_5.addWidget(self.UrlLabel, 0, 0, 1, 1)
        self.UrlTextBox = QtWidgets.QLineEdit(self.InputGroup)
        self.UrlTextBox.setObjectName("UrlTextBox")
        self.gridLayout_5.addWidget(self.UrlTextBox, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.InputGroup, 0, 0, 1, 1)
        self.DownloadWidget = QtWidgets.QWidget(self.MainWidget)
        self.DownloadWidget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.DownloadWidget.setObjectName("DownloadWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.DownloadWidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.DownloadButton = QtWidgets.QCommandLinkButton(self.DownloadWidget)
        self.DownloadButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DownloadButton.sizePolicy().hasHeightForWidth())
        self.DownloadButton.setSizePolicy(sizePolicy)
        self.DownloadButton.setMinimumSize(QtCore.QSize(0, 60))
        self.DownloadButton.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.DownloadButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../assets/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DownloadButton.setIcon(icon2)
        self.DownloadButton.setObjectName("DownloadButton")
        self.gridLayout_6.addWidget(self.DownloadButton, 0, 0, 1, 1)
        self.DownloadProgress = QtWidgets.QProgressBar(self.DownloadWidget)
        self.DownloadProgress.setProperty("value", 0)
        self.DownloadProgress.setObjectName("DownloadProgress")
        self.gridLayout_6.addWidget(self.DownloadProgress, 0, 1, 1, 1)
        self.DownloadInfo = QtWidgets.QWidget(self.DownloadWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.DownloadInfo.sizePolicy().hasHeightForWidth())
        self.DownloadInfo.setSizePolicy(sizePolicy)
        self.DownloadInfo.setObjectName("DownloadInfo")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.DownloadInfo)
        self.gridLayout_7.setContentsMargins(0, 0, 10, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.sep2 = QtWidgets.QFrame(self.DownloadInfo)
        self.sep2.setFrameShape(QtWidgets.QFrame.VLine)
        self.sep2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sep2.setObjectName("sep2")
        self.gridLayout_7.addWidget(self.sep2, 0, 2, 1, 1)
        self.SpeedLabel = QtWidgets.QLabel(self.DownloadInfo)
        self.SpeedLabel.setMinimumSize(QtCore.QSize(90, 0))
        self.SpeedLabel.setObjectName("SpeedLabel")
        self.gridLayout_7.addWidget(self.SpeedLabel, 0, 3, 1, 1)
        self.sep3 = QtWidgets.QFrame(self.DownloadInfo)
        self.sep3.setFrameShape(QtWidgets.QFrame.VLine)
        self.sep3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sep3.setObjectName("sep3")
        self.gridLayout_7.addWidget(self.sep3, 0, 5, 1, 1)
        self.ETALabel = QtWidgets.QLabel(self.DownloadInfo)
        self.ETALabel.setMinimumSize(QtCore.QSize(90, 0))
        self.ETALabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ETALabel.setObjectName("ETALabel")
        self.gridLayout_7.addWidget(self.ETALabel, 0, 0, 1, 1)
        self.FileSizeLabel = QtWidgets.QLabel(self.DownloadInfo)
        self.FileSizeLabel.setMinimumSize(QtCore.QSize(90, 0))
        self.FileSizeLabel.setObjectName("FileSizeLabel")
        self.gridLayout_7.addWidget(self.FileSizeLabel, 0, 6, 1, 1)
        self.gridLayout_6.addWidget(self.DownloadInfo, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.DownloadWidget, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.MainWidget)
        self.MenuBar = QtWidgets.QMenuBar(MainWindow)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 986, 21))
        self.MenuBar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.MenuBar.setObjectName("MenuBar")
        self.Preferences = QtWidgets.QMenu(self.MenuBar)
        self.Preferences.setObjectName("Preferences")
        self.ViewMenu = QtWidgets.QMenu(self.MenuBar)
        self.ViewMenu.setObjectName("ViewMenu")
        self.Theme = QtWidgets.QMenu(self.ViewMenu)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../assets/kcoloredit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Theme.setIcon(icon3)
        self.Theme.setObjectName("Theme")
        self.Help = QtWidgets.QMenu(self.MenuBar)
        self.Help.setObjectName("Help")
        self.CommandHelpMenu = QtWidgets.QMenu(self.Help)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../assets/help_index.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CommandHelpMenu.setIcon(icon4)
        self.CommandHelpMenu.setObjectName("CommandHelpMenu")
        MainWindow.setMenuBar(self.MenuBar)
        self.StatusBar = QtWidgets.QStatusBar(MainWindow)
        self.StatusBar.setObjectName("StatusBar")
        MainWindow.setStatusBar(self.StatusBar)
        self.ConsoleDock = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ConsoleDock.sizePolicy().hasHeightForWidth())
        self.ConsoleDock.setSizePolicy(sizePolicy)
        self.ConsoleDock.setFloating(False)
        self.ConsoleDock.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.ConsoleDock.setObjectName("ConsoleDock")
        self.ConsoleWidget = QtWidgets.QWidget()
        self.ConsoleWidget.setObjectName("ConsoleWidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.ConsoleWidget)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.ConsoleTextBox = QtWidgets.QPlainTextEdit(self.ConsoleWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.ConsoleTextBox.sizePolicy().hasHeightForWidth())
        self.ConsoleTextBox.setSizePolicy(sizePolicy)
        self.ConsoleTextBox.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.ConsoleTextBox.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"color: rgb(204, 204, 204);\n"
"selection-color: rgb(12, 12, 12);\n"
"selection-background-color: rgb(204, 204, 204);\n"
"font: 9pt \"Consolas\";")
        self.ConsoleTextBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ConsoleTextBox.setReadOnly(True)
        self.ConsoleTextBox.setObjectName("ConsoleTextBox")
        self.gridLayout_9.addWidget(self.ConsoleTextBox, 0, 0, 1, 1)
        self.ConsoleDock.setWidget(self.ConsoleWidget)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.ConsoleDock)
        self.DwItems = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.DwItems.sizePolicy().hasHeightForWidth())
        self.DwItems.setSizePolicy(sizePolicy)
        self.DwItems.setMinimumSize(QtCore.QSize(350, 91))
        self.DwItems.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.DwItems.setObjectName("DwItems")
        self.DwItemsListWidget = QtWidgets.QWidget()
        self.DwItemsListWidget.setObjectName("DwItemsListWidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.DwItemsListWidget)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.DwItemsList = QtWidgets.QTableWidget(self.DwItemsListWidget)
        self.DwItemsList.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DwItemsList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.DwItemsList.setObjectName("DwItemsList")
        self.DwItemsList.setColumnCount(4)
        self.DwItemsList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.DwItemsList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DwItemsList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.DwItemsList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.DwItemsList.setHorizontalHeaderItem(3, item)
        self.DwItemsList.horizontalHeader().setDefaultSectionSize(120)
        self.gridLayout_10.addWidget(self.DwItemsList, 0, 0, 1, 1)
        self.DwItems.setWidget(self.DwItemsListWidget)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.DwItems)
        self.About = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../assets/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.About.setIcon(icon5)
        self.About.setObjectName("About")
        self.AdditionalSwitches = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../assets/edit_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AdditionalSwitches.setIcon(icon6)
        self.AdditionalSwitches.setObjectName("AdditionalSwitches")
        self.ConsoleOption = QtWidgets.QAction(MainWindow)
        self.ConsoleOption.setCheckable(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../assets/terminal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ConsoleOption.setIcon(icon7)
        self.ConsoleOption.setObjectName("ConsoleOption")
        self.youtube_dlHelp = QtWidgets.QAction(MainWindow)
        self.youtube_dlHelp.setIcon(icon)
        self.youtube_dlHelp.setObjectName("youtube_dlHelp")
        self.ffmpegHelp = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../assets/ffmpeg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ffmpegHelp.setIcon(icon8)
        self.ffmpegHelp.setObjectName("ffmpegHelp")
        self.Support = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../assets/susehelpcenter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Support.setIcon(icon9)
        self.Support.setObjectName("Support")
        self.LightOption = QtWidgets.QAction(MainWindow)
        self.LightOption.setCheckable(True)
        self.LightOption.setChecked(True)
        self.LightOption.setObjectName("LightOption")
        self.DarkOption = QtWidgets.QAction(MainWindow)
        self.DarkOption.setCheckable(True)
        self.DarkOption.setObjectName("DarkOption")
        self.DownloadedItems = QtWidgets.QAction(MainWindow)
        self.DownloadedItems.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../assets/view_text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DownloadedItems.setIcon(icon10)
        self.DownloadedItems.setObjectName("DownloadedItems")
        self.Preferences.addAction(self.AdditionalSwitches)
        self.Theme.addAction(self.LightOption)
        self.Theme.addAction(self.DarkOption)
        self.ViewMenu.addAction(self.ConsoleOption)
        self.ViewMenu.addAction(self.DownloadedItems)
        self.ViewMenu.addSeparator()
        self.ViewMenu.addAction(self.Theme.menuAction())
        self.CommandHelpMenu.addAction(self.youtube_dlHelp)
        self.CommandHelpMenu.addAction(self.ffmpegHelp)
        self.Help.addAction(self.CommandHelpMenu.menuAction())
        self.Help.addAction(self.Support)
        self.Help.addSeparator()
        self.Help.addAction(self.About)
        self.MenuBar.addAction(self.Preferences.menuAction())
        self.MenuBar.addAction(self.ViewMenu.menuAction())
        self.MenuBar.addAction(self.Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.UrlTextBox, self.VideoOption)
        MainWindow.setTabOrder(self.VideoOption, self.AudioOption)
        MainWindow.setTabOrder(self.AudioOption, self.TemplateInput)
        MainWindow.setTabOrder(self.TemplateInput, self.RangeInput)
        MainWindow.setTabOrder(self.RangeInput, self.DestinationButton)
        MainWindow.setTabOrder(self.DestinationButton, self.DestinationInput)
        MainWindow.setTabOrder(self.DestinationInput, self.DownloadButton)
        MainWindow.setTabOrder(self.DownloadButton, self.ConsoleTextBox)
        MainWindow.setTabOrder(self.ConsoleTextBox, self.DwItemsList)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "youtube-dl GUI"))
        self.OutputGroup.setTitle(_translate("MainWindow", "Output"))
        self.DestinationInput.setToolTip(_translate("MainWindow", "The path to your final file"))
        self.DestinationLabel.setText(_translate("MainWindow", "Destination"))
        self.DestinationButton.setToolTip(_translate("MainWindow", "Select the file\'s destination"))
        self.DestinationButton.setText(_translate("MainWindow", "..."))
        self.ConfigGroup.setTitle(_translate("MainWindow", "Configuration"))
        self.ExportLabel.setText(_translate("MainWindow", "Export as..."))
        self.VideoOption.setToolTip(_translate("MainWindow", "Download video and audio"))
        self.VideoOption.setText(_translate("MainWindow", "Video + Audio"))
        self.AudioOption.setToolTip(_translate("MainWindow", "Download audio only, ideal for music or sound effects"))
        self.AudioOption.setText(_translate("MainWindow", "Audio-only"))
        self.TemplateLabel.setText(_translate("MainWindow", "Output template"))
        self.RangeLabel.setText(_translate("MainWindow", "Download range"))
        self.RangeInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select the range for download. </p><p>- <span style=\" font-weight:600;\">\'\' </span>Leaving it empty downloads all items.</p><p>- <span style=\" font-weight:600;\">m-n </span>Download from specified range.</p><p><span style=\" font-weight:600;\">- 1,2,..n </span>Download selected items.</p><p>- <span style=\" font-weight:600;\">x,m-n,y,z</span> Download specific items and from range.</p></body></html>"))
        self.TemplateInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>Append information to the end of your chosen output.</p><p>- <span style=\" font-weight:600;\">%(title)s</span> - video title</p><p>- <span style=\" font-weight:600;\">%(alt_title)s</span> - alternative video title</p><p>- <span style=\" font-weight:600;\">%(id)s</span> - video id</p><p>- <span style=\" font-weight:600;\">%(creator)s</span> - video creator</p><p>- <span style=\" font-weight:600;\">%(playlist_title)s</span> - playlist title</p><p>- <span style=\" font-weight:600;\">%(playlist_index)s</span> - video position in the playlist</p><p><span style=\" font-style:italic;\">Need the full list? Look for youtube-dl\'s README.md file at GitHub.</span></p></body></html>"))
        self.InputGroup.setTitle(_translate("MainWindow", "Input"))
        self.UrlLabel.setText(_translate("MainWindow", "YouTube URL"))
        self.UrlTextBox.setToolTip(_translate("MainWindow", "Input URL for your youtube video, playlist, or channel"))
        self.DownloadButton.setToolTip(_translate("MainWindow", "Finally, download!"))
        self.DownloadButton.setText(_translate("MainWindow", "Start\n"
"download!"))
        self.SpeedLabel.setText(_translate("MainWindow", "Speed:"))
        self.ETALabel.setText(_translate("MainWindow", "ETA:"))
        self.FileSizeLabel.setText(_translate("MainWindow", "File size:"))
        self.Preferences.setTitle(_translate("MainWindow", "Preferences"))
        self.ViewMenu.setTitle(_translate("MainWindow", "View"))
        self.Theme.setTitle(_translate("MainWindow", "Theme"))
        self.Help.setTitle(_translate("MainWindow", "Help"))
        self.CommandHelpMenu.setTitle(_translate("MainWindow", "Cmd line help"))
        self.ConsoleDock.setWindowTitle(_translate("MainWindow", "Console output"))
        self.DwItems.setWindowTitle(_translate("MainWindow", "Downloaded items"))
        item = self.DwItemsList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Video"))
        item = self.DwItemsList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size"))
        item = self.DwItemsList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Total time"))
        item = self.DwItemsList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Destination"))
        self.About.setText(_translate("MainWindow", "About"))
        self.About.setShortcut(_translate("MainWindow", "F1"))
        self.AdditionalSwitches.setText(_translate("MainWindow", "Additional switches"))
        self.AdditionalSwitches.setToolTip(_translate("MainWindow", "Additional switches"))
        self.ConsoleOption.setText(_translate("MainWindow", "Console output"))
        self.ConsoleOption.setToolTip(_translate("MainWindow", "Console output"))
        self.ConsoleOption.setShortcut(_translate("MainWindow", "F12"))
        self.youtube_dlHelp.setText(_translate("MainWindow", "youtube-dl"))
        self.youtube_dlHelp.setShortcut(_translate("MainWindow", "Shift+F1"))
        self.ffmpegHelp.setText(_translate("MainWindow", "ffmpeg"))
        self.ffmpegHelp.setShortcut(_translate("MainWindow", "Alt+Shift+F1"))
        self.Support.setText(_translate("MainWindow", "Support"))
        self.Support.setShortcut(_translate("MainWindow", "Alt+F1"))
        self.LightOption.setText(_translate("MainWindow", "Light"))
        self.DarkOption.setText(_translate("MainWindow", "Dark"))
        self.DownloadedItems.setText(_translate("MainWindow", "Downloaded items"))
