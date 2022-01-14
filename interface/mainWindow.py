import sys,os
sys.path.insert(1,'.')

from webbrowser import open_new_tab as OpenURL

from interface.mainUi import Ui_MainWindow as ui

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QAbstractButton
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QColor
from PyQt5.QtCore import QObject, Qt, QEvent

from dist import pydist as pd

from interface.aboutWindow import AboutDialog as aw
from interface.addswitchesDialog import AdditionalSwitchesDialog as ad
from interface.cmdhelpWindow import CmdHelpDialog as ch

class MainWindow(ui,QObject):
    window = QMainWindow
    app = QApplication

    darkTheme = palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)

    aboutDialog = aw
    addSwitchesDialog = ad

    isDarkTheme = False

    def eventFilter(self, a0: QObject, a1: QEvent) -> bool:
        print(str(a1))
        if a0 == self.ConsoleDock and a1 == QEvent.Type.Close: self.ConsoleOption.setChecked(False)
        return super().eventFilter(a0, a1)

    def __init__(self,window:QMainWindow,app:QApplication):
        self.window = window
        self.app = app
        self.app.setStyle("Fusion")

        super().setupUi(window)
        super().__init__()

        self.InitIcons()

        self.aboutDialog = aw()
        self.addSwitchesDialog = ad(windowicon=pd.__PyDist__._WorkDir+"assets/ytdl.png")

        self.CloseConsole()
        self.ConsoleDock.installEventFilter(self)
        self.ConsoleOption.triggered.connect(lambda: self.SetConsoleOpen(self.ConsoleOption.isChecked()))

        self.LightOption.triggered.connect(self.ToLightTheme)
        self.DarkOption.triggered.connect(self.ToDarkTheme)

        self.About.triggered.connect(self.OpenAboutDialog)
        self.AdditionalSwitches.triggered.connect(self.OpenAdditionalSwitchesDialog)

        self.youtube_dlHelp.triggered.connect(self.YtdlGetHelp)
        self.ffmpegHelp.triggered.connect(self.FfmpegGetHelp)
    
    def OpenConsole(self): self.ConsoleDock.show()
    def CloseConsole(self): self.ConsoleDock.close()
    def SetConsoleOpen(self,open:bool):
        if open: self.OpenConsole()
        else: self.CloseConsole()
    def SetConsole(self,text:str): self.ConsoleTextBox.setPlainText(text)
    def AppendConsole(self,text:str): self.ConsoleTextBox.appendPlainText(text)
    def ClearConsole(self): self.ConsoleTextBox.clear()
    def GetConsole(self) -> str: return self.ConsoleTextBox.toPlainText()
    
    def OpenAboutDialog(self): self.aboutDialog.Execute()
    def OpenAdditionalSwitchesDialog(self) -> str: return self.addSwitchesDialog.Execute()
    
    def YtdlGetHelp(self): ch().GetHelp(pd.__PyDist__._WorkDir+"youtube-dl\\youtube-dl.exe --help")
    def FfmpegGetHelp(self): ch("ffmpeg command line help").GetHelp(pd.__PyDist__._WorkDir+"youtube-dl\\ffmpeg.exe --help")
    
    def InitIcons(self):
        self.window.setWindowIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/ytdl.png")))

        self.Theme.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/kcoloredit.png")))
        self.AdditionalSwitches.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/edit_add.png")))

        self.ConsoleOption.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/terminal.png")))

        self.CommandHelpMenu.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/help_index.png")))
        self.Support.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/susehelpcenter.png")))
        self.About.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/info.png")))

        self.DownloadButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/forward.png"))

        self.DestinationButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/folder_yellow.png"))

        #print(pd.__PyDist__._WorkDir)
    
    def Set(self,values:dict[str]):
        self.SetURL(values["URL"])
        self.SetOutput(values["OUTPUT"])
        self.SetAudioOnly(values["AUDIO_ONLY"])
        self.SetTemplate(values["TEMPLATE"])
        self.SetRange(values["RANGE"])
    def Get(self) -> dict[str]:
        resp = {}
        resp["URL"] = self.GetURL()
        resp["OUTPUT"] = self.GetOutput()
        resp["AUDIO_ONLY"] = self.GetAudioOnly()
        resp["TEMPLATE"] = self.GetTemplate()
        resp["RANGE"] = self.GetRange()
        return resp

    def SetURL(self,url:str): self.UrlTextBox.setText(url)
    def GetURL(self) -> str: return self.UrlTextBox.text()
    
    def SetOutput(self,output:str): self.DestinationInput.setText(output)
    def GetOutput(self) -> str: return self.DestinationInput.text()

    def SetTemplate(self,template:str): self.TemplateInput.setText(template)
    def GetTemplate(self) -> str: return self.TemplateInput.text()
    
    def SetRange(self,range:str): self.RangeInput.setText(range)
    def GetRange(self) -> str: return self.RangeInput.text()
    
    def SetAudioOnly(self,audioOnly:bool): self.AudioOption.setChecked(audioOnly)
    def GetAudioOnly(self) -> bool: return self.AudioOption.isChecked()

    def SetProgress(self,value:int): self.DownloadProgress.setValue(value)
    def GetProgress(self) -> int: return self.DownloadProgress.value()

    def SetDownloadText(self,text:str): self.DownloadButton.setText(text)
    
    def SetDownloadInfo(self,eta:str,speed:str,size:str,progress:int=-1):
        self.ETALabel.setText("ETA: "+eta)
        self.SpeedLabel.setText("Speed: "+speed)
        self.FileSizeLabel.setText("File size: "+size)
        if not progress == -1: self.SetProgress(progress)
    def GetDownloadInfo(self) -> dict:
        resp = {}
        resp["ETA"] = self.ETALabel.text().removeprefix("ETA: ")
        resp["SPEED"] = self.ETALabel.text().removeprefix("Speed: ")
        resp["SIZE"] = self.ETALabel.text().removeprefix("File size: ")
        return resp

    def DownloadIcon(self): self.DownloadButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/forward.png"))
    def CancelIcon(self): self.DownloadButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/stop.png"))

    def SetDownloadCallback(self,callback): self.DownloadButton.pressed.connect(callback)

    def SaveTheme(self,dark,prefMng=None):
        self.DarkOption.setChecked(dark)
        self.LightOption.setChecked(not dark)
        self.isDarkTheme = self.DarkOption.isChecked()

        if prefMng: prefMng.SetSetting(["isDarkTheme"],dark)
    
    def ToLightTheme(self):
        self.app.setPalette(QPalette())
        self.window.setPalette(QPalette())
        self.SaveTheme(False)
    
    def ToDarkTheme(self):
        self.app.setPalette(self.darkTheme)
        self.window.setPalette(self.darkTheme)
        self.SaveTheme(True)
    
    def DownloadEndDialog(self,errorcode:int,error:str=""):
        msg = QMessageBox()
        msg.setWindowIcon(QIcon(pd.__PyDist__._WorkDir+'assets/ytdl.png'))
        msg.setWindowTitle("youtube-dl GUI")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)

        if errorcode!=0 and error != "":
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Finished downloading unsuccessfully!")
            msg.setInformativeText(str(error))
        elif errorcode!=0:
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