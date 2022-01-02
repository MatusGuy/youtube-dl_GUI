# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newmain.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(733, 915)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(650, 715))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        MainWindow.setFont(font)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.MainWidget = QtWidgets.QWidget(MainWindow)
        self.MainWidget.setObjectName("MainWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.MainWidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.DownloadInfo = QtWidgets.QTableWidget(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DownloadInfo.sizePolicy().hasHeightForWidth())
        self.DownloadInfo.setSizePolicy(sizePolicy)
        self.DownloadInfo.setMinimumSize(QtCore.QSize(0, 340))
        self.DownloadInfo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.DownloadInfo.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.DownloadInfo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.DownloadInfo.setDragDropOverwriteMode(False)
        self.DownloadInfo.setObjectName("DownloadInfo")
        self.DownloadInfo.setColumnCount(5)
        self.DownloadInfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.DownloadInfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DownloadInfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.DownloadInfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.DownloadInfo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.DownloadInfo.setHorizontalHeaderItem(4, item)
        self.gridLayout_2.addWidget(self.DownloadInfo, 2, 0, 1, 1)
        self.DownloadWidget = QtWidgets.QWidget(self.MainWidget)
        self.DownloadWidget.setMinimumSize(QtCore.QSize(0, 80))
        self.DownloadWidget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.DownloadWidget.setObjectName("DownloadWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.DownloadWidget)
        self.horizontalLayout.setContentsMargins(10, 10, 13, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DownloadButton = QtWidgets.QCommandLinkButton(self.DownloadWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DownloadButton.setFont(font)
        self.DownloadButton.setObjectName("DownloadButton")
        self.horizontalLayout.addWidget(self.DownloadButton)
        self.GlobalProgressBar = QtWidgets.QProgressBar(self.DownloadWidget)
        self.GlobalProgressBar.setProperty("value", 0)
        self.GlobalProgressBar.setObjectName("GlobalProgressBar")
        self.horizontalLayout.addWidget(self.GlobalProgressBar)
        self.gridLayout_2.addWidget(self.DownloadWidget, 3, 0, 1, 1)
        self.BeforeDownload = QtWidgets.QTabWidget(self.MainWidget)
        self.BeforeDownload.setMinimumSize(QtCore.QSize(0, 150))
        self.BeforeDownload.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BeforeDownload.setFont(font)
        self.BeforeDownload.setObjectName("BeforeDownload")
        self.InputTab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(8)
        self.InputTab.setFont(font)
        self.InputTab.setObjectName("InputTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.InputTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.UrlLabel = QtWidgets.QLabel(self.InputTab)
        self.UrlLabel.setObjectName("UrlLabel")
        self.gridLayout_4.addWidget(self.UrlLabel, 0, 0, 1, 1)
        self.UrlInput = QtWidgets.QLineEdit(self.InputTab)
        self.UrlInput.setObjectName("UrlInput")
        self.gridLayout_4.addWidget(self.UrlInput, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        self.BeforeDownload.addTab(self.InputTab, "")
        self.ExportTab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ExportTab.setFont(font)
        self.ExportTab.setObjectName("ExportTab")
        self.formLayout = QtWidgets.QFormLayout(self.ExportTab)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setObjectName("formLayout")
        self.VideoOption = QtWidgets.QRadioButton(self.ExportTab)
        self.VideoOption.setObjectName("VideoOption")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.VideoOption)
        self.AudioOption = QtWidgets.QRadioButton(self.ExportTab)
        self.AudioOption.setObjectName("AudioOption")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.AudioOption)
        self.MetadataOption = QtWidgets.QCheckBox(self.ExportTab)
        self.MetadataOption.setObjectName("MetadataOption")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.MetadataOption)
        self.CoverArtOption = QtWidgets.QCheckBox(self.ExportTab)
        self.CoverArtOption.setObjectName("CoverArtOption")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.CoverArtOption)
        self.BeforeDownload.addTab(self.ExportTab, "")
        self.OutputTab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(8)
        self.OutputTab.setFont(font)
        self.OutputTab.setObjectName("OutputTab")
        self.Tab_OnTop = QtWidgets.QGridLayout(self.OutputTab)
        self.Tab_OnTop.setContentsMargins(13, 12, -1, -1)
        self.Tab_OnTop.setObjectName("Tab_OnTop")
        self._line0 = QtWidgets.QFrame(self.OutputTab)
        self._line0.setFrameShape(QtWidgets.QFrame.HLine)
        self._line0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self._line0.setObjectName("_line0")
        self.Tab_OnTop.addWidget(self._line0, 2, 0, 1, 5)
        self.RangeLabel = QtWidgets.QLabel(self.OutputTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RangeLabel.sizePolicy().hasHeightForWidth())
        self.RangeLabel.setSizePolicy(sizePolicy)
        self.RangeLabel.setObjectName("RangeLabel")
        self.Tab_OnTop.addWidget(self.RangeLabel, 4, 0, 1, 1)
        self.TemplateInput = QtWidgets.QLineEdit(self.OutputTab)
        self.TemplateInput.setObjectName("TemplateInput")
        self.Tab_OnTop.addWidget(self.TemplateInput, 5, 1, 1, 4)
        self.DestinationInput = QtWidgets.QLineEdit(self.OutputTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DestinationInput.sizePolicy().hasHeightForWidth())
        self.DestinationInput.setSizePolicy(sizePolicy)
        self.DestinationInput.setObjectName("DestinationInput")
        self.Tab_OnTop.addWidget(self.DestinationInput, 0, 1, 1, 3)
        self.RangeInput = QtWidgets.QLineEdit(self.OutputTab)
        self.RangeInput.setObjectName("RangeInput")
        self.Tab_OnTop.addWidget(self.RangeInput, 4, 1, 1, 4)
        self.DestinationLabel = QtWidgets.QLabel(self.OutputTab)
        self.DestinationLabel.setObjectName("DestinationLabel")
        self.Tab_OnTop.addWidget(self.DestinationLabel, 0, 0, 1, 1)
        self.TemplateLabel = QtWidgets.QLabel(self.OutputTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TemplateLabel.sizePolicy().hasHeightForWidth())
        self.TemplateLabel.setSizePolicy(sizePolicy)
        self.TemplateLabel.setObjectName("TemplateLabel")
        self.Tab_OnTop.addWidget(self.TemplateLabel, 5, 0, 1, 1)
        self.DestinationButton = QtWidgets.QToolButton(self.OutputTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DestinationButton.sizePolicy().hasHeightForWidth())
        self.DestinationButton.setSizePolicy(sizePolicy)
        self.DestinationButton.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DestinationButton.setIcon(icon)
        self.DestinationButton.setObjectName("DestinationButton")
        self.Tab_OnTop.addWidget(self.DestinationButton, 0, 4, 2, 1)
        self.BeforeDownload.addTab(self.OutputTab, "")
        self.gridLayout_2.addWidget(self.BeforeDownload, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.MainWidget)
        self.MenuBar = QtWidgets.QMenuBar(MainWindow)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 733, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MenuBar.sizePolicy().hasHeightForWidth())
        self.MenuBar.setSizePolicy(sizePolicy)
        self.MenuBar.setMinimumSize(QtCore.QSize(5, 0))
        self.MenuBar.setDefaultUp(False)
        self.MenuBar.setNativeMenuBar(True)
        self.MenuBar.setObjectName("MenuBar")
        self.Help = QtWidgets.QMenu(self.MenuBar)
        self.Help.setObjectName("Help")
        self.Preferences = QtWidgets.QMenu(self.MenuBar)
        self.Preferences.setObjectName("Preferences")
        self.Theme = QtWidgets.QMenu(self.Preferences)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Theme.sizePolicy().hasHeightForWidth())
        self.Theme.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../assets/theme.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Theme.setIcon(icon1)
        self.Theme.setObjectName("Theme")
        self.View = QtWidgets.QMenu(self.MenuBar)
        self.View.setObjectName("View")
        MainWindow.setMenuBar(self.MenuBar)
        self.StatusBar = QtWidgets.QStatusBar(MainWindow)
        self.StatusBar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.StatusBar.setObjectName("StatusBar")
        MainWindow.setStatusBar(self.StatusBar)
        self.Console = QtWidgets.QDockWidget(MainWindow)
        self.Console.setMinimumSize(QtCore.QSize(113, 142))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.Console.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../assets/consoleIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Console.setWindowIcon(icon2)
        self.Console.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.Console.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.TopDockWidgetArea)
        self.Console.setObjectName("Console")
        self.ConsoleWidget = QtWidgets.QWidget()
        self.ConsoleWidget.setObjectName("ConsoleWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.ConsoleWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.ConsoleText = QtWidgets.QPlainTextEdit(self.ConsoleWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ConsoleText.setFont(font)
        self.ConsoleText.setStyleSheet("background-color: rgb(12, 12, 12);\n"
"selection-color: rgb(12, 12, 12);\n"
"selection-background-color: rgb(243, 243, 243);\n"
"color: rgba(243, 243, 243, 243);")
        self.ConsoleText.setLineWidth(0)
        self.ConsoleText.setUndoRedoEnabled(False)
        self.ConsoleText.setReadOnly(True)
        self.ConsoleText.setPlainText("")
        self.ConsoleText.setObjectName("ConsoleText")
        self.gridLayout.addWidget(self.ConsoleText, 0, 0, 1, 1)
        self.Console.setWidget(self.ConsoleWidget)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.Console)
        self.About = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../assets/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.About.setIcon(icon3)
        self.About.setObjectName("About")
        self.Light = QtWidgets.QAction(MainWindow)
        self.Light.setCheckable(True)
        self.Light.setObjectName("Light")
        self.Dark = QtWidgets.QAction(MainWindow)
        self.Dark.setCheckable(True)
        self.Dark.setObjectName("Dark")
        self.actionConsole_output = QtWidgets.QAction(MainWindow)
        self.actionConsole_output.setCheckable(True)
        self.actionConsole_output.setChecked(True)
        self.actionConsole_output.setIcon(icon2)
        self.actionConsole_output.setObjectName("actionConsole_output")
        self.ConsoleOption = QtWidgets.QAction(MainWindow)
        self.ConsoleOption.setCheckable(True)
        self.ConsoleOption.setIcon(icon2)
        self.ConsoleOption.setObjectName("ConsoleOption")
        self.Help.addAction(self.About)
        self.Theme.addAction(self.Light)
        self.Theme.addAction(self.Dark)
        self.Preferences.addAction(self.Theme.menuAction())
        self.Preferences.addSeparator()
        self.View.addAction(self.ConsoleOption)
        self.MenuBar.addAction(self.Preferences.menuAction())
        self.MenuBar.addAction(self.View.menuAction())
        self.MenuBar.addAction(self.Help.menuAction())

        self.retranslateUi(MainWindow)
        self.BeforeDownload.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.DownloadInfo, self.DownloadButton)
        MainWindow.setTabOrder(self.DownloadButton, self.ConsoleText)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "youtube-dl GUI"))
        self.DownloadInfo.setStatusTip(_translate("MainWindow", "Download status for each queued song"))
        item = self.DownloadInfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.DownloadInfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Progress"))
        item = self.DownloadInfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ETA"))
        item = self.DownloadInfo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Speed"))
        item = self.DownloadInfo.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "File size"))
        self.DownloadButton.setStatusTip(_translate("MainWindow", "Finally, download"))
        self.DownloadButton.setText(_translate("MainWindow", "Start\n"
"downloading!"))
        self.UrlLabel.setText(_translate("MainWindow", "YouTube URL"))
        self.BeforeDownload.setTabText(self.BeforeDownload.indexOf(self.InputTab), _translate("MainWindow", "Input"))
        self.VideoOption.setText(_translate("MainWindow", "Video + audio"))
        self.AudioOption.setText(_translate("MainWindow", "Audio-only"))
        self.MetadataOption.setText(_translate("MainWindow", "Export metadata"))
        self.CoverArtOption.setText(_translate("MainWindow", "Export thumbnail as cover art"))
        self.BeforeDownload.setTabText(self.BeforeDownload.indexOf(self.ExportTab), _translate("MainWindow", "Export settings"))
        self.RangeLabel.setText(_translate("MainWindow", "Download range"))
        self.DestinationLabel.setText(_translate("MainWindow", "Destination"))
        self.TemplateLabel.setText(_translate("MainWindow", "Output template"))
        self.DestinationButton.setText(_translate("MainWindow", "..."))
        self.BeforeDownload.setTabText(self.BeforeDownload.indexOf(self.OutputTab), _translate("MainWindow", "Output"))
        self.Help.setTitle(_translate("MainWindow", "Help"))
        self.Preferences.setTitle(_translate("MainWindow", "Preferences"))
        self.Theme.setTitle(_translate("MainWindow", "Theme"))
        self.View.setTitle(_translate("MainWindow", "View"))
        self.Console.setWindowTitle(_translate("MainWindow", "Console output"))
        self.About.setText(_translate("MainWindow", "About"))
        self.Light.setText(_translate("MainWindow", "Light"))
        self.Dark.setText(_translate("MainWindow", "Dark"))
        self.actionConsole_output.setText(_translate("MainWindow", "Console output"))
        self.ConsoleOption.setText(_translate("MainWindow", "Console output"))
