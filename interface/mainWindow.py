import sys,os
sys.path.insert(1,'.')

from webbrowser import open_new_tab as OpenURL
from pathlib import Path
from types import FunctionType

from interface.mainUi import Ui_MainWindow as ui

from PyQt5.QtWidgets import (QMainWindow, QApplication, QMessageBox, QLabel, QFileDialog, QTableWidgetItem,
                             QStyleFactory, QDesktopWidget, QDockWidget, QInputDialog, QAction)
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QColor
from PyQt5.QtCore import QObject, Qt, QEvent
from PyQt5.QtWinExtras import QWinTaskbarButton, QWinThumbnailToolBar, QWinThumbnailToolButton

from win10toast_click import ToastNotifier

EXCLUDE_DISABLED = False

from interface.DownloadedListMenu import DownloadedListMenu as DWLMenu

from dist import pydist as pd
WDIR = pd.__PyDist__._WorkDir

from interface.aboutWindow import AboutDialog as aw
from interface.addswitchesDialog import AdditionalSwitchesDialog as ad
from interface.cmdhelpWindow import CmdHelpDialog as ch
from components.prefMng import PreferencesManager as pm
from interface.Completers import templateCompleter

class MainWindow(ui,QObject):
    window = QMainWindow
    app = QApplication

    defaultStyleSheet = str

    lightTheme = QPalette()
    lightTheme.setColor(QPalette.ColorRole.Window, QColor(239, 239, 239, 255))
    lightTheme.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0, 255))
    lightTheme.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255, 255))
    lightTheme.setColor(QPalette.ColorRole.AlternateBase, QColor(247, 247, 247, 255))
    lightTheme.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 220, 255))
    lightTheme.setColor(QPalette.ColorRole.ToolTipText, QColor(0, 0, 0, 255))
    lightTheme.setColor(QPalette.ColorRole.Text, QColor(0, 0, 0, 255))
    lightTheme.setColor(QPalette.ColorRole.Button, QColor(239, 239, 239, 255))
    lightTheme.setColor(QPalette.ColorRole.ButtonText, QColor(0, 0, 0, 255))
    lightTheme.setColor(QPalette.ColorRole.BrightText, QColor(255, 255, 255, 255))
    lightTheme.setColor(QPalette.ColorRole.Link, QColor(0, 0, 255, 255))
    lightTheme.setColor(QPalette.ColorRole.Highlight, QColor(48, 140, 198, 255))
    lightTheme.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255, 255))
    lightTheme.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, Qt.GlobalColor.gray)
    lightTheme.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Foreground, Qt.GlobalColor.gray)

    darkTheme = QPalette()
    darkTheme.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    darkTheme.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    darkTheme.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    darkTheme.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    darkTheme.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.black)
    darkTheme.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    darkTheme.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    darkTheme.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    darkTheme.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    darkTheme.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    darkTheme.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    darkTheme.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    darkTheme.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
    darkTheme.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, QColor(25, 25, 25))
    darkTheme.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, Qt.GlobalColor.gray)
    darkTheme.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Foreground, Qt.GlobalColor.gray)

    aboutDialog = aw
    addSwitchesDialog = ad

    prefMng = None

    isDarkTheme = False

    def _ExcludeObjects(self,objs:list[QObject]):
        for obj in objs:
            obj.setParent(None)
            obj.deleteLater()


    def eventFilter(self, a0:QObject, a1:QEvent) -> bool:
        if a0 is self.window and a1.type() == QEvent.Type.Close: self.app.quit()

        if a0 is self.ConsoleDock and a1.type() == QEvent.Type.Close: self.ConsoleOption.setChecked(False)
        if a0 is self.DwItems and a1.type() == QEvent.Type.Close: self.DownloadedItems.setChecked(False)
        if a0 is self.DwGraphDock and a1.type() == QEvent.Type.Close: self.DownloadGraph.setChecked(False)
        return super().eventFilter(a0, a1)

    def __init__(self,window:QMainWindow,app:QApplication,version:str="0.0.0.0",prefMng:pm=None,whileInit:FunctionType=None):
        self.window = window
        self.app = app
        self.app.setStyle("Fusion")
        self.prefMng = prefMng

        super().setupUi(window)
        super().__init__()
        self.defaultStyleSheet = self.window.styleSheet()

        if EXCLUDE_DISABLED: self._ExcludeObjects([
            self.DwGraphDock,
            self.DownloadGraph
        ])

        self.aboutDialog = aw(version)
        self.addSwitchesDialog = ad(windowicon=pd.__PyDist__._WorkDir+"assets/ytdl.png")

        self.InitIcons()
        self.InitStatusBar()
        self.DisableDownloadGui(True)

        self.CloseConsole()
        self.ConsoleDock.installEventFilter(self)
        self.ConsoleDock.setStyle(QStyleFactory.create("WindowsVista"))
        self.ConsoleTextBox.verticalScrollBar().setStyle(QStyleFactory.create("Fusion"))

        self.ConsoleOption.toggled.connect(lambda: self.SetConsoleOpen(self.ConsoleOption.isChecked()))

        self.CloseDwItems()
        self.DwItems.installEventFilter(self)
        self.DownloadedItems.toggled.connect(lambda: self.SetDwItemsOpen(self.DownloadedItems.isChecked()))
        self.DwItems.setStyle(QStyleFactory.create("WindowsVista"))
        self.DwItemsListWidget.setStyle(QStyleFactory.create("Fusion"))
        self.DwItemsList.setColumnWidth(0,230)

        self.LoadSettings()

        DWLMenu(self.DwItemsList,self.app.clipboard(),self.DwItemsListWidget)

        self.addSwitchesDialog.HelpMenu.setMenu(self.CommandHelpMenu)
        self.addSwitchesDialog.HelpMenu.pressed.connect(self.YtdlGetHelp)

        self.LightOption.triggered.connect(self.ToLightTheme)
        self.DarkOption.triggered.connect(self.ToDarkTheme)

        self.DestinationButton.pressed.connect(lambda: self.SetOutput(self.DestinationSelectPrompt()))
        self.UrlTextBox.textEdited.connect(self.RangeInput.clear)
        self.AudioOption.toggled.connect(self.SetAudioOnly)

        self.About.triggered.connect(self.OpenAboutDialog)
        self.Support.triggered.connect(self.OpenGitHubIssues)
        self.AdditionalSwitches.triggered.connect(self.OpenAdditionalSwitchesDialog)

        self.ProxySettings.triggered.connect(self.ProxySettingsDialog)

        self.youtube_dlHelp.triggered.connect(self.YtdlGetHelp)
        self.ffmpegHelp.triggered.connect(self.FfmpegGetHelp)

        self.app.aboutToQuit.connect(self.OnAppQuit)

        self.CornerAbout = QToolButton(self.MenuBar)
        self.CornerAbout.setIcon(QIcon(WDIR+"assets/info.png"))
        self.CornerAbout.setAutoRaise(True)
        self.CornerAbout.setStyleSheet("border: transparent")
        self.CornerAbout.pressed.connect(self.About.trigger)
        self.MenuBar.setCornerWidget(self.CornerAbout)

        if whileInit!=None: whileInit()

        self.CloseDwGraph()
        self._ExcludeObjects([self.DwGraphDock])
        self.CenterWindow()
        self.window.show() ##############################
        #self.window.frameGeometry().moveCenter(QDesktopWidget().availableGeometry().center())

        self.InitWinTaskbarFeatures()

    def InitWinTaskbarFeatures(self):
        self.taskbarButton = QWinTaskbarButton(self.window)
        self.taskbarButton.setWindow(self.window.windowHandle())

        self.taskbarProgress = self.taskbarButton.progress()
        self.taskbarProgress.setMinimum(0)
        self.taskbarProgress.setMaximum(100)
        self.taskbarProgress.setValue(0)
        self.taskbarProgress.show()

        self.taskbarToolBar = QWinThumbnailToolBar(self.window)
        self.taskbarToolBar.setWindow(self.window.windowHandle())

        self.taskbarCancelButton = QWinThumbnailToolButton(self.taskbarToolBar)
        self.taskbarCancelButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/stop.png"))
        self.taskbarCancelButton.setToolTip("Stop downloading!")
        self.taskbarCancelButton.setEnabled(False)

        self.taskbarAboutButton = QWinThumbnailToolButton(self.taskbarToolBar)
        self.taskbarAboutButton.setIcon(QIcon(WDIR+"assets/info.png"))
        self.taskbarAboutButton.setToolTip("About youtube-dl GUI")
        self.taskbarAboutButton.clicked.connect(self.About.trigger)

        self.taskbarToolBar.addButton(self.taskbarCancelButton)
        self.taskbarToolBar.addButton(self.taskbarAboutButton)

    def CenterWindow(self):
        center = QDesktopWidget().availableGeometry().center()
        self.window.move(int(center.x()/2),int(center.y()/2))
    
    def LoadSettings(self):
        settings = self.prefMng.settings

        self.SetURL(settings["savedConfig"]["url"])
        self.SetAudioOnly(settings["savedConfig"]["audioOnly"])
        self.SetTemplate(settings["savedConfig"]["template"])
        self.SetRange(settings["savedConfig"]["range"])

        self.SetOutput(settings["savedConfig"]["destination"])
        if settings["savedConfig"]["destination"] == "<DEFAULT>":
            self.SetOutput(str(Path.home())+"\\.mp4")

        self.SetTemplateHistory(settings["templateHistory"])

        self.ProxySettings.setChecked(settings["proxy"][0])
        self.ProxySettings.setProperty("SERVER",settings["proxy"][1])

        self.PreferNotif.setChecked(settings["preferNotif"])

        if settings["isDarkTheme"]:
            self.ToDarkTheme()
        else:
            self.ToLightTheme()

        self.window.resize(
            settings["window"]["size"]["x"],
            settings["window"]["size"]["y"]
        )

        self.LoadDockWidget(self.ConsoleDock,"console",self.ConsoleOption)
        self.LoadDockWidget(self.DwItems,"dwList",self.DownloadedItems)
        
        self.SetAdditionalSwitches(settings["additionalSwitches"])
    
    def DockArea2Orientation(self,area:Qt.DockWidgetArea) -> Qt.Orientation|None:
        if area == Qt.DockWidgetArea.RightDockWidgetArea or area == Qt.DockWidgetArea.LeftDockWidgetArea: return Qt.Orientation.Horizontal
        if area == Qt.DockWidgetArea.TopDockWidgetArea or area == Qt.DockWidgetArea.BottomDockWidgetArea: return Qt.Orientation.Vertical
        return None
    
    def LoadDockWidget(self,dock:QDockWidget,key:str,action:QAction):
        print(dock.windowTitle())

        dockprefs = self.prefMng.settings["dockWidgetPrefs"][key]

        self.window.removeDockWidget(dock)
        self.window.addDockWidget(Qt.DockWidgetArea(dockprefs["area"]),dock)
        self.window.resizeDocks(
            [dock],
            [dockprefs["size"]["x"] if self.DockArea2Orientation(dockprefs["area"]) else dockprefs["size"]["y"]],
            self.DockArea2Orientation(dockprefs["area"])
        )

        action.setChecked(dockprefs["open"])

        dock.setProperty("SAVED_VISIBLE",dock.isVisible())
        def SaveVisibility(visible:bool):
            print(visible)
            if self.window.isVisible(): dock.setProperty("SAVED_VISIBLE",visible)
        
        dock.visibilityChanged.connect(SaveVisibility)

    def SaveDockWidget(self,dock:QDockWidget,key:str):
        print(dock.windowTitle())
        toset_dockprefs = ["dockWidgetPrefs",key]

        self.ChangeSetting(toset_dockprefs+["open"],dock.property("SAVED_VISIBLE"))
        self.ChangeSetting(toset_dockprefs+["area"],self.window.dockWidgetArea(dock))
        self.ChangeSetting(toset_dockprefs+["size","x"],dock.width())
        self.ChangeSetting(toset_dockprefs+["size","y"],dock.height())

    def ProxySettingsDialog(self):
        if self.ProxySettings.isChecked():
            server,ok = QInputDialog.getText(
                None,
                "Proxy settings",
                "Insert the proxy server below",
                text=self.GetProxy()[1]
            )
            if ok: self.ProxySettings.setProperty("SERVER",server)
            if not ok: self.ProxySettings.setChecked(False)
    def GetProxy(self) -> tuple[str,bool]:
        return (self.ProxySettings.isChecked(),self.ProxySettings.property("SERVER"))
    
    def OpenConsole(self): self.ConsoleDock.show()
    def CloseConsole(self): self.ConsoleDock.close()
    def SetConsoleOpen(self,open:bool):
        if open: self.OpenConsole()
        else: self.CloseConsole()
    def SetConsole(self,text:str): self.ConsoleTextBox.setPlainText(text)
    def AppendConsole(self,text:str): self.ConsoleTextBox.appendPlainText(text)
    def AppendConsoleHtml(self,text:str): self.ConsoleTextBox.appendHtml(text)
    def ClearConsole(self): self.ConsoleTextBox.clear()
    def GetConsole(self) -> str: return self.ConsoleTextBox.toPlainText()

    def OpenDwItems(self): self.DwItems.show()
    def CloseDwItems(self): self.DwItems.close()
    def SetDwItemsOpen(self,open:bool):
        if open: self.OpenDwItems()
        else: self.CloseDwItems()
    def AddDwItemsRow(self,pos:int):
        self.DwItemsList.insertRow(pos)
        self.DwItemsList.setRowHeight(pos,20)
    def ListToDwList(self,dwList:list):
        self.DwItemsList.setRowCount(0)
        for item in dwList:
            index = dwList.index(item)
            self.AddDwItemsRow(index)

            self.DwItemsList.setItem(index,1,QTableWidgetItem(item["DESTINATION"]))

            self.DwItemsList.setItem(index,2,QTableWidgetItem(item["SIZE"]))
            self.DwItemsList.setItem(index,3,QTableWidgetItem(item["TOTAL_TIME"]))
            self.DwItemsList.setItem(index,0,QTableWidgetItem(item["STARTED"]))
    
    def OpenDwGraph(self): self.DwGraphDock.show()
    def CloseDwGraph(self): self.DwGraphDock.close()
    def SetDwGraphOpen(self,open:bool):
        if open: self.OpenDwGraph()
        else: self.CloseDwGraph()

    def OpenAboutDialog(self): self.aboutDialog.Execute()
    def OpenGitHubIssues(self): OpenURL("https://github.com/MatusGuy/youtube-dl_GUI/issues")
    def OpenAdditionalSwitchesDialog(self) -> str:
        resp=self.addSwitchesDialog.Execute()
        self.ChangeSetting(["additionalSwitches"], resp)
        return resp
    def GetAdditionalSwitches(self) -> str: return self.addSwitchesDialog.Get()
    def SetAdditionalSwitches(self,value:str): self.addSwitchesDialog.Set(value)
    
    def YtdlGetHelp(self): ch().GetHelp(pd.__PyDist__._WorkDir+"youtube-dl\\youtube-dl.exe --help")
    def FfmpegGetHelp(self): ch("ffmpeg command line help").GetHelp(pd.__PyDist__._WorkDir+"youtube-dl\\ffmpeg.exe --help")
    
    def InitIcons(self):
        self.PreferNotif.setIcon(QIcon(WDIR+"assets/bell.png"))

    
    def InitStatusBar(self):
        self.StatusBar.showMessage("Prepare to download.")
        self.sbDwCurrLabel = QLabel("") #("Current file: My nice music 03 album.mp3")
        self.StatusBar.addPermanentWidget(self.sbDwCurrLabel)
        self.sbDwFilesLabel = QLabel("") #("\tItems: 1 / 10")
        self.StatusBar.addPermanentWidget(self.sbDwFilesLabel)

    def SetURL(self,url:str): self.UrlTextBox.setText(url), self.ChangeSetting(["savedConfig","url"],self.GetURL())
    def GetURL(self) -> str: return self.UrlTextBox.text()
    
    def SetOutput(self,output:str): self.DestinationInput.setText(output), self.ChangeSetting(["savedConfig","destination"],self.GetOutput())
    def GetOutput(self) -> str: return self.DestinationInput.text()

    def SetTemplate(self,template:str): self.TemplateInput.setCurrentText(template), self.ChangeSetting(["savedConfig","template"],self.GetTemplate())
    def GetTemplate(self) -> str: return self.TemplateInput.currentText()
    def SetTemplateHistory(self,templates:list[str]):
        self.TemplateInput.clear()
        for item in templates: self.TemplateInput.addItem(item)
    def GetTemplateHistory(self) -> list[str]: return [self.TemplateInput.itemText(i) for i in range(self.TemplateInput.count())]
    
    def SetRange(self,range:str): self.RangeInput.setText(range), self.ChangeSetting(["savedConfig","range"],self.GetRange())
    def GetRange(self) -> str: return self.RangeInput.text()
    
    def SetAudioOnly(self,audioOnly:bool):
        self.AudioOption.setChecked(audioOnly)
        if audioOnly and self.GetOutput().endswith(".mp4"):
            self.SetOutput(self.GetOutput().removesuffix("4")+"3")
        elif not audioOnly and self.GetOutput().endswith(".mp3"):
            self.SetOutput(self.GetOutput().removesuffix("3")+"4")
    def GetAudioOnly(self) -> bool: return self.AudioOption.isChecked()

    def SetProgress(self,value:int):
        self.DownloadProgress.setValue(value)
        self.taskbarProgress.setValue(value)
    def GetProgress(self) -> int: return self.DownloadProgress.value()
    def UndefinedProgress(self):
        self.DownloadProgress.setFormat(self.DownloadProgress.format().replace(
            "%p",
            str(self.DownloadProgress.value())
        ))
        self.DownloadProgress.setRange(0,0)
        self.taskbarProgress.setRange(0,0)
    def DefinedProgress(self):
        self.DownloadProgress.setFormat("%p%")
        self.DownloadProgress.setRange(0,100)
        self.taskbarProgress.setRange(0,100)
    def SetProgressColour(self,colour:QColor=QColor(57,165,234)):
        c = colour
        self.DownloadProgress.setStyleSheet(f"selection-background-color: rgb({c.red()},{c.green()},{c.blue()})")

    def SetDownloadText(self,text:str): self.DownloadButton.setText(text)
    
    def SetDownloadInfo(self,eta:str,speed:str,size:str,progress:int=-1,current:str="",files:str=""):
        self.ETALabel.setText("ETA: "+eta)
        self.SpeedLabel.setText("Speed: "+speed)
        self.FileSizeLabel.setText("File size: "+size)
        if not progress == -1: self.SetProgress(progress)
        self.sbDwCurrLabel.setText("Current file: "+current if current  else "")
        self.sbDwFilesLabel.setText("\tItems: "+files if files else "")
    def GetDownloadInfo(self) -> dict:
        resp = {}
        resp["ETA"] = self.ETALabel.text().removeprefix("ETA: ")
        resp["SPEED"] = self.SpeedLabel.text().removeprefix("Speed: ")
        resp["SIZE"] = self.FileSizeLabel.text().removeprefix("File size: ")
        resp["CURR"] = self.sbDwCurrLabel.text().removeprefix("Current file: ")
        resp["ITEMS"] = self.sbDwFilesLabel.text().removeprefix("\tItems: ")
        return resp
    
    def DisableDownloadGui(self,disable:bool):
        self.FileSizeLabel.setEnabled(not disable)
        self.SpeedLabel.setEnabled(not disable)
        self.ETALabel.setEnabled(not disable)
        self.DownloadProgress.setEnabled(not disable)
        #self.DownloadButton.setEnabled(disable)
        self.sbDwFilesLabel.setEnabled(not disable)
        self.sbDwCurrLabel.setEnabled(not disable)

        if disable:
            self.DownloadProgress.setValue(0)
            self.FileSizeLabel.setText("File size: ")
            self.SpeedLabel.setText("Speed: ")
            self.ETALabel.setText("ETA: ")
            self.sbDwCurrLabel.setText("")
            self.sbDwFilesLabel.setText("\t")

    def DownloadIcon(self): self.DownloadButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/forward.png"))
    def CancelIcon(self): self.DownloadButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/stop.png"))

    def SetDownloadCallback(self,callback): self.DownloadButton.pressed.connect(callback)

    def DownloadingTaskbarOverlay(self):
        self.taskbarButton.setOverlayIcon(QIcon(WDIR+"assets/drive-download.png"))
        self.taskbarButton.setOverlayAccessibleDescription("Downloading")
    def OperatingTaskbarOverlay(self):
        self.taskbarButton.setOverlayIcon(QIcon(WDIR+"assets/gear.png"))
        self.taskbarButton.setOverlayAccessibleDescription("Operating")
    def ClearTaskbarOverlay(self):
        self.taskbarButton.clearOverlayIcon()
        self.taskbarButton.setOverlayAccessibleDescription("")

    def DownloadButtonState(self):
        self.SetDownloadText("Start\ndownload!")
        self.DownloadIcon()
        self.DownloadButton.setToolTip("Finally, download!")
        self.taskbarCancelButton.setEnabled(False)
    def CancelButtonState(self):
        self.SetDownloadText("Cancel\ndownload!")
        self.CancelIcon()
        self.DownloadButton.setToolTip("Cancel download!")
        self.taskbarProgress.resume()
        self.taskbarCancelButton.setEnabled(True)

    def ShowStatusMessage(self,text:str,duration:int=-1):
        if not duration == -1:
            self.StatusBar.showMessage(text,duration)
        else:
            self.StatusBar.showMessage(text)
    def ClearStatusMessage(self): self.StatusBar.clearMessage()

    def SaveTheme(self,dark):
        self.DarkOption.setChecked(dark)
        self.LightOption.setChecked(not dark)
        self.isDarkTheme = self.DarkOption.isChecked()

        self.ChangeSetting(["isDarkTheme"],dark)
    
    def ToLightTheme(self):
        self.app.setPalette(self.lightTheme)
        self.RefreshStyle()
        self.RefreshStyleSheet()
        self.SaveTheme(False)
    
    def ToDarkTheme(self):
        self.app.setPalette(self.darkTheme)
        self.RefreshStyle()
        self.RefreshStyleSheet()
        self.SaveTheme(True)
    
    def RestoreWindow(self):
        self.window.activateWindow()

    def DownloadEndDialog(self,errorcode:int,error:str=""):
        msg = QMessageBox()
        msg.setWindowIcon(QIcon(WDIR+'assets/ytdl.png'))
        msg.setWindowTitle("youtube-dl GUI")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)

        if errorcode==1 and error:
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Finished downloading unsuccessfully!")
            msg.setStyleSheet('''
                QTextEdit{
                    color: red;
                    background-color: black;
                    font: 12px "Consolas";
                    selection-background-color: rgb(255,255,255);
                    selection-color: rgb(14,14,14);
                    border-radius: 4px;
                }
            ''')
            msg.setDetailedText(str(error))
            self.taskbarProgress.stop()
            self.SetProgressColour(QColor(201, 13, 13))
        elif errorcode==1:
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Canceled by user!")
            self.taskbarProgress.stop()
            self.SetProgressColour(QColor(201, 13, 13))
        else:
            msg.setText("Finished downloading successfully!")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Open | QMessageBox.StandardButton.Ok)
            self.SetProgressColour(QColor(34, 159, 17))
        
        if self.PreferNotif.isChecked():
            self.notif = ToastNotifier()
            self.notif.show_toast(
                title=msg.text(),
                msg=msg.detailedText(),
                icon_path=WDIR+"assets\\ytdl.ico",
                duration=None,
                threaded=False,
                callback_on_click=self.window.activateWindow
            )
            #self.notif.wnd_proc(self.window.winId(),"","","") # sample data, just end my notification already
        else:
        result = msg.exec_()
        self.taskbarProgress.setValue(0)
        self.SetProgressColour()

        if result == QMessageBox.StandardButton.Open:
            output = self.DestinationInput.text()
            rfind1 = output.rfind('\\')
            rfind2 = output.rfind('/')
            if rfind1 > rfind2:
                result = output[:rfind1+1]
            else:
                result = output[:rfind2+1]
            wresult=result.replace('/','\\')
            #print (wresult)
            if len(wresult): os.system("explorer "+wresult)
    
    def DestinationSelectPrompt(self) -> str:
        filenameFilter = ""
        if not self.GetAudioOnly():
            filenameFilter = "Video (*.mp4 *.3gp *.aac *.flv *.m4a *.webm)"
        else:
            filenameFilter = "Audio (*.mp3 *.wav *.ogg *.aac *.flac *.m4a *.opus)"
        
        defaultpath=str(Path.home()) if not self.GetOutput() else self.GetOutput()

        filename = QFileDialog.getSaveFileName(
            parent=self.DestinationButton,
            caption="Select output file...",
            directory=defaultpath,
            filter=filenameFilter
        )

        return str(filename[0])#.replace("/","\\")

    def AlertVersionDialog(self) -> bool:
        versionMsg = QMessageBox()
        versionMsg.setIcon(QMessageBox.Icon.Information)
        versionMsg.setWindowTitle("youtube-dl GUI")
        versionMsg.setText("There's a new version of youtube-dl GUI available.\nRestart the application to apply it.\n\nClose the application?")
        versionMsg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        versionMsg.setWindowIcon(QIcon(pd.__PyDist__._WorkDir+'assets/ytdl.png'))
        versionMsg.setModal(True)

        resp = versionMsg.exec_()
        
        return resp == QMessageBox.StandardButton.Yes # user has accepted to take the new version
        
    def ChangeSetting(self,setting:list,value):
        if self.prefMng and pd.__PyDist__._isBundle:
            self.prefMng.SetSetting(setting,value)
        
    def OnAppQuit(self):
        try:
            self.notif.wnd_proc()
            self.notif._thread.stop()
        except:
            pass

        self.ChangeSetting(["savedConfig","url"],self.GetURL())
        self.ChangeSetting(["savedConfig","audioOnly"],self.GetAudioOnly())
        self.ChangeSetting(["savedConfig","template"],self.GetTemplate())
        self.ChangeSetting(["savedConfig","range"],self.GetRange())
        self.ChangeSetting(["savedConfig","destination"],self.GetOutput())
        self.ChangeSetting(["proxy",0],self.GetProxy()[0])
        self.ChangeSetting(["proxy",1],self.GetProxy()[1])
        self.ChangeSetting(["preferNotif"],self.PreferNotif.isChecked())

        self.ChangeSetting(["templateHistory"],self.GetTemplateHistory())

        self.ChangeSetting(["isDarkTheme"],self.DarkOption.isChecked())
        self.ChangeSetting(["additionalSwitches"],self.GetAdditionalSwitches())

        self.ChangeSetting(["window","size","x"],self.window.width())
        self.ChangeSetting(["window","size","y"],self.window.height())

        self.SaveDockWidget(self.ConsoleDock,"console")
        self.SaveDockWidget(self.DwItems,"dwList")

        self.prefMng.WriteJSON(self.prefMng.filename,self.prefMng.settings)

        self._ExcludeObjects(self.window.children())

    def RefreshStyle(self): self.app.setStyle('Fusion')
    def RefreshStyleSheet(self): self.window.setStyleSheet(self.defaultStyleSheet)