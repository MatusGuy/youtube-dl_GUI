from json import decoder
import sys,os,json
from os import close, curdir, error, fdopen
import ctypes
from pathlib import Path
from typing import Optional, Set
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QColor,QIcon,QPalette,QMovie,QPixmap
from PyQt5.QtCore import QRect, Qt,pyqtSlot
from PyQt5.QtWidgets import *
import youtubedl_gui_class as MainUi
import downloader as dl
import youtubedl_about_class as aboutWnd
from dist import pydist as pd

#from settingsGuis.themePrompt_class import Ui_ChangeTheme as ThemesGui

currSjson = pd.__PyDist__._ExecDir+"settings.json"
newSjson = pd.__PyDist__._WorkDir+"settings.json"

def GetJSON(file,closeFile=True):
        with open(file) as j:
            try:
                return json.load(j),j
            except ValueError as e:
                if closeFile: j.close()
                raise Exception('Invalid json: {}'.format(e)) from None

def SetJSON(file,data,closeFile=True):
    with open(file, "w") as outfile:
        json.dump(data,outfile,indent=4, default=str)

class Program(MainUi.Ui_MainWindow):
    window = None
    app = None

    downloader = dl.Downloader()
    showConsole = False
    
    aboutDialog=None
    aboutGui=None

    videos=0

    console_height=89

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

    isDarkTheme = False

    error = ""

    def setupUi(self, MainWindow, app):
        self.app = app
        self.app.setStyle("Fusion")

        self.window = MainWindow

        resp=super().setupUi(MainWindow)

        self.window.resize(0,390)
        self.ConsoleOutput.setHidden(not self.showConsole)

        self.VideoOption.setChecked(True)

        self.DownloadButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/miniArrow.png"))        

        currentSettings,file = GetJSON(currSjson)
        self.isDarkTheme = currentSettings["isDarkTheme"]

        savedConfig = currentSettings["savedConfig"]

        self.UrlTextBox.setText(savedConfig["url"])

        self.AudioOption.setChecked(savedConfig["audioOnly"])
        self.TemplateInput.setText(savedConfig["template"])
        self.RangeInput.setText(savedConfig["range"])

        self.DestinationInput.setText(savedConfig["destination"])

        file.close()

        if self.isDarkTheme:
            self.ToDarkTheme()
        else:
            self.ToLightTheme()

        self.window.setWindowIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/ytdl.png")))

        self.AboutMenu.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/about.png")))
        self.ThemeMenu.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/theme.png")))

        self.DestinationButton.pressed.connect(self.SetOutput)
        self.DownloadButton.pressed.connect(self.Download)
        self.ViewConsole.toggled.connect(self.ToggleConsole)

        #self.Downloader = dl.Downloader(".\\youtube-dl\\")

        self.downloader = dl.Downloader(pd.__PyDist__._WorkDir+".\\youtube-dl\\",self.ConsoleAddLine,self.Downloaded_Ended)

        self.aboutGui = aboutWnd.Ui_About()
        self.aboutDialog = QDialog(self.window,Qt.WindowType.WindowCloseButtonHint)
        self.aboutGui.setupUi(self.aboutDialog)
        gif = QMovie(pd.__PyDist__._WorkDir+"assets/ytdl.gif")
        
        version=pd.__PyDist__.GetAppVersion()
        version="0.0.0.0" if not version else version
        self.aboutGui.Version.setText("Version "+version)

        self.aboutGui.IconGif.setMovie(gif)
        gif.start()
        self.aboutDialog.setModal(True)
        self.aboutGui.OKbt.pressed.connect(self.aboutDialog.close)
        
        self.AboutMenu.triggered.connect(self.aboutDialog.exec_)

        self.LightOption.triggered.connect(self.ToLightTheme)
        self.DarkOption.triggered.connect(self.ToDarkTheme)

        self.UrlTextBox.editingFinished.connect(self.OnUrlEdit)
        self.DestinationInput.editingFinished.connect(self.OnOutputEdit)

        self.AudioOption.toggled.connect(self.OnMediaTypeTriggered)
        self.TemplateInput.editingFinished.connect(self.OnTemplateEdit)
        self.RangeInput.editingFinished.connect(self.OnRangeEdit)

        return resp

    def SaveTheme(self,dark):
        self.DarkOption.setChecked(dark)
        self.LightOption.setChecked(not dark)
        self.isDarkTheme = self.DarkOption.isChecked()

        currentSettings,file = GetJSON(currSjson)
        currentSettings["isDarkTheme"] = self.isDarkTheme
        SetJSON(currSjson, currentSettings)
        file.close()
    
    def ToLightTheme(self):
        self.app.setPalette(QPalette())
        self.window.setPalette(QPalette())
        imgpath=pd.__PyDist__._WorkDir.replace("\\","/")
        self.ViewConsole.setStyleSheet("QCheckBox::indicator:checked{border-image : url("+imgpath+"assets/openedArrow.png);}QCheckBox::indicator:unchecked{border-image : url("+imgpath+"assets/closedArrow.png);}")
        self.SaveTheme(False)
    
    def ToDarkTheme(self):
        self.app.setPalette(self.darkTheme)
        self.window.setPalette(self.darkTheme)
        imgpath=pd.__PyDist__._WorkDir.replace("\\","/")
        self.ViewConsole.setStyleSheet("QCheckBox::indicator:checked"
                                       "{border-image : url("+imgpath+"assets/openedArrowDark.png);}"
                                       "QCheckBox::indicator:unchecked"
                                       "{border-image : url("+imgpath+"assets/closedArrowDark.png);}")
        self.SaveTheme(True)

    def ConsoleAddLine(self,text):
        self.DownloadProgress.setEnabled(True)

        if type(text)==bytes:
            txt=text.decode("ASCII")
        else:
            txt=text
        self.ConsoleOutput.appendPlainText(txt)

        uppered = txt.upper()
        #print(uppered)

        if "%" in uppered and "[DOWNLOAD] " in uppered:
            cut1 = txt.split("] ")[1]
            cut2 = cut1.split("% ")
            result = cut2[0].replace(" ","0")

            self.DownloadProgress.setValue(int(float(result)))

            if not os.path.exists(self.DestinationInput.text()):
                if "100%" in uppered:
                    self.DownloadSpeedLabel.setText("Speed: ")
                    self.ETALabel.setText("ETA: ")
                else:
                    otherInfo = cut2[1].split(" ")
                    fileSize = otherInfo[1]
                    dwSpeed = otherInfo[3]
                    eta = otherInfo[5]

                    self.FileSizeLabel.setText("Total file size: "+fileSize)
                    self.DownloadSpeedLabel.setText("Speed: "+dwSpeed)
                    self.ETALabel.setText("ETA: "+eta)
        
        if "[DOWNLOAD] DOWNLOADING VIDEO" in uppered and "OF" in uppered:
            cut1 = txt.split(" ")
            self.currentFilePos = cut1[3]
            self.listLength = cut1[5]
        

        if "[DOWNLOAD] DESTINATION: " in uppered:
            prefixRemoval1 = txt.removeprefix("[download] Destination: ")
            cut1 = prefixRemoval1.split("\\")
            currentFile = cut1[len(cut1)-1]

            self.CurrentFile.setText("Current: "+currentFile)
            self.FilesLabel.setText(f"Files: {self.currentFilePos}/{self.listLength}")
        
        if "ERROR: " in uppered:
            if "YOUTUBE-DL.EXE: ":
                self.error = txt.removeprefix("youtube-dl.EXE: error: ").capitalize()
            else:
                self.error = txt.removeprefix("ERROR: ").capitalize()
            #print(self.error)
    
    def OnUrlEdit(self,closeFile=True):
        currentSettings,file = GetJSON(currSjson)
        currentSettings["savedConfig"]["url"] = self.UrlTextBox.text()
        SetJSON(currSjson,currentSettings)
        if closeFile: file.close()
    
    def OnOutputEdit(self,closeFile=True):
        currentSettings,file = GetJSON(currSjson)
        currentSettings["savedConfig"]["destination"] = self.DestinationInput.text()
        SetJSON(currSjson,currentSettings)
        if closeFile: file.close()
    
    def OnMediaTypeTriggered(self,closeFile=True):
        currentSettings,file = GetJSON(currSjson)
        currentSettings["savedConfig"]["audioOnly"] = self.AudioOption.isChecked()
        SetJSON(currSjson,currentSettings)
        if closeFile: file.close()
    
    def OnTemplateEdit(self,closeFile=True):
        currentSettings,file = GetJSON(currSjson)
        currentSettings["savedConfig"]["template"] = self.TemplateInput.text()
        SetJSON(currSjson,currentSettings)
        if closeFile: file.close()

    def OnRangeEdit(self,closeFile=True):
        currentSettings,file = GetJSON(currSjson)
        currentSettings["savedConfig"]["range"] = self.RangeInput.text()
        SetJSON(currSjson,currentSettings)
        if closeFile: file.close()
    
    def ToggleConsole(self):
        X,Y,WW,WH=self.window.geometry().getRect()
        #print(f"MAIN WINDOW :({X},{Y}..{WW},{WH})")
        
        if self.showConsole:
            CX,CY,CW,CH =self.ConsoleOutput.geometry().getRect()
            self.console_height=CH 
            #print(f"CONSOLE:({CX},{CY}..{CW},{CH})")
        
        self.showConsole = not self.showConsole
        if self.showConsole:
            self.window.resize(WW,WH+self.console_height)
        else:
            self.window.resize(WW,WH-self.console_height)
        
        self.ConsoleOutput.setHidden(not self.showConsole)

    def DisableDownloadGui(self,disable):
        self.FileSizeLabel.setEnabled(not disable)
        self.DownloadSpeedLabel.setEnabled(not disable)
        self.ETALabel.setEnabled(not disable)
        self.DownloadProgress.setEnabled(not disable)
        #self.DownloadButton.setEnabled(disable)
        self.CurrentFile.setEnabled(not disable)
        self.FilesLabel.setEnabled(not disable)

        if disable:
            self.DownloadProgress.setValue(0)
            self.FileSizeLabel.setText("Total file size: ")
            self.DownloadSpeedLabel.setText("Speed: ")
            self.ETALabel.setText("ETA: ")
            self.FilesLabel.setText("Files: ")
            self.CurrentFile.setText("Current: ")
    
    def SetOutput(self):
        self.FilePrompt = QFileDialog()
        filenameFilter = ""
        self.audioOnly = self.AudioOption.isChecked()
        if not self.audioOnly:
            filenameFilter = "Video (*.mp4 *.3gp *.aac *.flv *.m4a *.webm)"
        else:
            filenameFilter = "Audio (*.mp3 *.wav *.ogg *.aac *.flac *.m4a *.opus)"
        
        defaultpath=str(Path.home()) if len(self.DestinationInput.text())==0 else self.DestinationInput.text()

        filename = self.FilePrompt.getSaveFileName(
            parent=self.DestinationButton,
            caption="Select output file...",
            directory=defaultpath,
            filter=filenameFilter,
        )

        self.DestinationInput.setText(filename[0] if len(filename[0]) else self.DestinationInput.text())

    def Download(self):
        if self.downloader.IsDownloading():
            #print ("Cancel!!!??!?")
            self.downloader.CancelDownload()
        else:
            self.DisableDownloadGui(False)

            self.DownloadButton.setText("Cancel\ndownload")
            self.DownloadButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/miniCross.png"))
            self.DownloadButton.setToolTip("Stop downloading!")

            self.MainWidget.update()

            Config={
                "URL":self.UrlTextBox.text(),
                "AUDIO_ONLY":self.AudioOption.isChecked(),
                "OUTPUT":self.DestinationInput.text(),
                "TEMPLATE":self.TemplateInput.text(),
                "RANGE":self.RangeInput.text(),
            }
            ##print(str(Config))
            #self.ExecuteDownload(Config)
            self.ConsoleOutput.setPlainText("")
            self.currentFilePos = 1
            self.listLength = 1
            self.downloader.StartDownload(Config)


    def Downloaded_Ended(self,errorcode):
        self.DownloadProgress.setEnabled(False)
        self.DownloadButton.setEnabled(True)

        self.ConsoleAddLine("Download process ended")

        self.DownloadButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/miniArrow.png"))
        self.DownloadButton.setText("Start\ndownload!")
        self.DownloadButton.setToolTip("Finally, download!")

        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon(pd.__PyDist__._WorkDir+'assets/ytdl.png'))
        msg.setWindowTitle("youtube-dl GUI")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)

        if errorcode!=0 and self.error != "":
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Finished downloading unsuccessfully!")
            msg.setInformativeText(str(self.error))
        elif errorcode!=0:
            msg.setIcon(QMessageBox.Information)
            msg.setText("Canceled by user!")
        else:
            msg.setText("Finished downloading successfully!")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Open | QMessageBox.StandardButton.Ok)
        
        def OpenDownloaded(button):
            if button.text() == "Open":
                rfind1 = self.output.rfind('\\')
                rfind2 = self.output.rfind('/')
                if rfind1 > rfind2:
                    result = self.output[:rfind1+1]
                else:
                    result = self.output[:rfind2+1]
                wresult=result.replace('/','\\')
                print (wresult)
                if len(wresult): os.system("explorer "+wresult)

        msg.buttonClicked.connect(OpenDownloaded)
        
        msg.exec()

        self.DisableDownloadGui(True)

def window():
    app = QApplication(sys.argv)

    window = QMainWindow()

    hellowindow = Program()
    hellowindow.setupUi(window,app)

    QtCore.QTimer.singleShot(250, HideSplash)

    window.show()
    sys.exit(app.exec_())

def HideSplash():
    try:
        import pyi_splash
        pyi_splash.close()
    except:
        pass

def prepSettings(configfile,newConfigFile):
    #print (f"IS EXECUTABLE: {pd.__PyDist__._isBundle}")
    #print (f"Exec Path: {pd.__PyDist__._ExecDir}")
    #print (f"Temp Path: {pd.__PyDist__._WorkDir}")

    newJsonData,newJsonFile = GetJSON(newConfigFile)

    if pd.__PyDist__._isBundle:
        if os.path.exists(configfile):
            currJsonData,currJsonFile = GetJSON(configfile)

            if currJsonData["version"] != newJsonData["version"]:
                for key in newJsonData:
                    if key in currJsonData.keys():
                        newJsonData[key] = currJsonData[key]
            
            SetJSON(configfile, newJsonData)
            currJsonFile.close()
        
        os.system(f"copy {pd.__PyDist__._WorkDir}\\settings.json {pd.__PyDist__._ExecDir} /Y ")
    
    newJsonFile.close()

if __name__ == '__main__':
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

    if (pd.__PyDist__._isBundle): prepSettings(currSjson,newSjson)

    window()