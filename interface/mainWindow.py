import sys,os
sys.path.insert(1,'.')

from webbrowser import open_new_tab as OpenURL
from pathlib import Path

from interface.mainUi import Ui_MainWindow as ui

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QLabel, QFileDialog, QTableWidgetItem, QDockWidget
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QColor
from PyQt5.QtCore import QObject, Qt, QEvent

from dist import pydist as pd

from interface.aboutWindow import AboutDialog as aw
from interface.addswitchesDialog import AdditionalSwitchesDialog as ad
from interface.cmdhelpWindow import CmdHelpDialog as ch
from components.prefMng import PreferencesManager as pm

class MainWindow(ui,QObject):
    window = QMainWindow
    app = QApplication

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

    aboutDialog = aw
    addSwitchesDialog = ad

    prefMng = None

    isDarkTheme = False

    def eventFilter(self, a0:QObject, a1:QEvent) -> bool:
        if a0 is self.ConsoleDock and a1.type() == QEvent.Type.Close: self.ConsoleOption.setChecked(False)
        if a0 is self.DwItems and a1.type() == QEvent.Type.Close: self.DownloadedItems.setChecked(False)
        return super().eventFilter(a0, a1)

    def __init__(self,window:QMainWindow,app:QApplication,version:str="0.0.0.0",prefMng:pm=None):
        self.window = window
        self.app = app
        self.app.setStyle("Fusion")
        self.prefMng = prefMng

        super().setupUi(window)
        super().__init__()

        #self.MainWidget.setStyleSheet("")

        self.aboutDialog = aw(version)
        self.addSwitchesDialog = ad(windowicon=pd.__PyDist__._WorkDir+"assets/ytdl.png")
        self.LoadSettings()

        self.InitIcons()
        self.InitStatusBar()
        self.DisableDownloadGui(True)

        self.CloseConsole()
        self.ConsoleDock.installEventFilter(self)
        self.ConsoleOption.triggered.connect(lambda: self.SetConsoleOpen(self.ConsoleOption.isChecked()))

        self.CloseDwItems()
        self.DwItems.installEventFilter(self)
        self.DownloadedItems.toggled.connect(lambda: self.SetDwItemsOpen(self.DownloadedItems.isChecked()))

        self.LightOption.triggered.connect(self.ToLightTheme)
        self.DarkOption.triggered.connect(self.ToDarkTheme)

        self.DestinationButton.pressed.connect(lambda: self.SetOutput(self.DestinationSelectPrompt()))

        self.About.triggered.connect(self.OpenAboutDialog)
        self.Support.triggered.connect(self.OpenGitHubIssues)
        self.AdditionalSwitches.triggered.connect(self.OpenAdditionalSwitchesDialog)

        self.youtube_dlHelp.triggered.connect(self.YtdlGetHelp)
        self.ffmpegHelp.triggered.connect(self.FfmpegGetHelp)

        self.app.aboutToQuit.connect(self.OnAppQuit)
    
    def LoadSettings(self):
        settings = self.prefMng.settings
        self.SetURL(settings["savedConfig"]["url"])
        self.SetAudioOnly(settings["savedConfig"]["audioOnly"])
        self.SetTemplate(settings["savedConfig"]["template"])
        self.SetRange(settings["savedConfig"]["range"])

        self.SetOutput(settings["savedConfig"]["destination"])
        if settings["savedConfig"]["destination"] == "<DEFAULT>":
            self.SetOutput(str(Path.home())+"\\.mp4")

        if settings["isDarkTheme"]:
            self.ToDarkTheme()
        else:
            self.ToLightTheme()
        
        self.SetAdditionalSwitches(settings["additionalSwitches"])
    
    def OpenConsole(self): self.ConsoleDock.show()
    def CloseConsole(self): self.ConsoleDock.close()
    def SetConsoleOpen(self,open:bool):
        if open: self.OpenConsole()
        else: self.CloseConsole()
    def SetConsole(self,text:str): self.ConsoleTextBox.setPlainText(text)
    def AppendConsole(self,text:str): self.ConsoleTextBox.appendPlainText(text)
    def ClearConsole(self): self.ConsoleTextBox.clear()
    def GetConsole(self) -> str: return self.ConsoleTextBox.toPlainText()

    def OpenDwItems(self): self.DwItems.show()
    def CloseDwItems(self): self.DwItems.close()
    def SetDwItemsOpen(self,open:bool):
        if open: self.OpenDwItems()
        else: self.CloseDwItems()
    def AddDwItemsRow(self,pos:int): self.DwItemsList.insertRow(pos)
    def ListToDwList(self,dwList:list):
        self.DwItemsList.setRowCount(0)
        for item in dwList:
            index = dwList.index(item)
            self.AddDwItemsRow(index)
            self.DwItemsList.setItem(index,0,QTableWidgetItem(item["FILENAME"]))
            self.DwItemsList.setItem(index,1,QTableWidgetItem(item["SIZE"]))
            self.DwItemsList.setItem(index,2,QTableWidgetItem(item["TOTAL_TIME"]))
            self.DwItemsList.setItem(index,3,QTableWidgetItem(item["DESTINATION"]))

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
        self.window.setWindowIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/ytdl.png")))
        self.Theme.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/kcoloredit.png")))
        self.AdditionalSwitches.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/edit_add.png")))
        self.ConsoleOption.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/terminal.png")))
        self.DownloadedItems.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/view_text.png"))
        self.CommandHelpMenu.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/help_index.png")))
        self.Support.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/susehelpcenter.png")))
        self.About.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/info.png")))
        self.DownloadButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/forward.png"))
        self.DestinationButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/folder_yellow.png"))
        self.youtube_dlHelp.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/ytdl.png"))
        self.ffmpegHelp.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/ffmpeg.png"))
    
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

    def SetTemplate(self,template:str): self.TemplateInput.setText(template), self.ChangeSetting(["savedConfig","template"],self.GetTemplate())
    def GetTemplate(self) -> str: return self.TemplateInput.text()
    
    def SetRange(self,range:str): self.RangeInput.setText(range), self.ChangeSetting(["savedConfig","range"],self.GetRange())
    def GetRange(self) -> str: return self.RangeInput.text()
    
    def SetAudioOnly(self,audioOnly:bool): self.AudioOption.setChecked(audioOnly), self.ChangeSetting(["savedConfig","audioOnly"],self.GetAudioOnly())
    def GetAudioOnly(self) -> bool: return self.AudioOption.isChecked()

    def SetProgress(self,value:int): self.DownloadProgress.setValue(value)
    def GetProgress(self) -> int: return self.DownloadProgress.value()

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
            self.FileSizeLabel.setText("Total file size: ")
            self.SpeedLabel.setText("Speed: ")
            self.ETALabel.setText("ETA: ")
            self.sbDwCurrLabel.setText("")
            self.sbDwFilesLabel.setText("\t")

    def DownloadIcon(self): self.DownloadButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/forward.png"))
    def CancelIcon(self): self.DownloadButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/stop.png"))

    def SetDownloadCallback(self,callback): self.DownloadButton.pressed.connect(callback)

    def DownloadButtonState(self):
        self.SetDownloadText("Start\ndownload!")
        self.DownloadIcon()
        self.DownloadButton.setToolTip("Finally, download!")
    def CancelButtonState(self):
        self.SetDownloadText("Cancel\ndownload!")
        self.CancelIcon()
        self.DownloadButton.setToolTip("Cancel download!")

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
        self.window.setPalette(self.lightTheme)
        self.app.setStyle("Fusion") 
        self.SaveTheme(False)
    
    def ToDarkTheme(self):
        self.app.setPalette(self.darkTheme)
        self.window.setPalette(self.darkTheme)
        self.app.setStyle("Fusion")
        self.SaveTheme(True)
    
    def DownloadEndDialog(self,errorcode:int,error:str=""):
        msg = QMessageBox()
        msg.setWindowIcon(QIcon(pd.__PyDist__._WorkDir+'assets/ytdl.png'))
        msg.setWindowTitle("youtube-dl GUI")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)

        if errorcode==1 and error:
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Finished downloading unsuccessfully!")
            msg.setStyleSheet('''
                QTextEdit{
                    font: 12px "Consolas";
                    selection-background-color: rgb(3,96,209);
                    selection-color: rgb(217,217,217)
                }
            ''')
            msg.setDetailedText(str(error))
        elif errorcode==1:
            msg.setIcon(QMessageBox.Information)
            msg.setText("Canceled by user!")
        else:
            msg.setText("Finished downloading successfully!")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Open | QMessageBox.StandardButton.Ok)
        
        result = msg.exec_()

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

        return str(filename[0])
        
    def ChangeSetting(self,setting:list,value):
        if self.prefMng and pd.__PyDist__._isBundle:
            self.prefMng.SetSetting(setting,value)
        
    def OnAppQuit(self):
        self.ChangeSetting(["savedConfig","url"],self.GetURL())
        self.ChangeSetting(["savedConfig","audioOnly"],self.GetAudioOnly())
        self.ChangeSetting(["savedConfig","template"],self.GetTemplate())
        self.ChangeSetting(["savedConfig","range"],self.GetRange())
        self.ChangeSetting(["savedConfig","destination"],self.GetOutput())

        self.ChangeSetting(["isDarkTheme"],self.DarkOption.isChecked())
        self.ChangeSetting(["additionalSwitches"],self.GetAdditionalSwitches())

        self.ChangeSetting([""])

        self.prefMng.WriteJSON(self.prefMng.filename,self.prefMng.settings)
    
    def ChangeAppStyleSheet(self,sheet:str):
        self.app.setStyleSheet('''
            QToolButton::pressed,.QPushButton::pressed{
                background-color: rgb(49, 144, 204)
            }        
        '''+sheet)