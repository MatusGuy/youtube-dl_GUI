import sys,os,webbrowser,ctypes
from pathlib import Path
from PyQt5 import QtGui
from PyQt5.QtGui import QColor,QIcon,QPalette,QPixmap
from PyQt5.QtCore import Qt,QObject,QEvent
from PyQt5.QtWidgets import *
import interface.mainUi as MainUi
from dist import pydist as pd
import py_mysplash as psh

from components import downloader as dl, versionChecker as vc, prefMng as pm

from interface import aboutWindow as aw, addswitchesDialog as ad, cmdhelpWindow as ch

#from settingsGuis.themePrompt_class import Ui_ChangeTheme as ThemesGui

currSjson = pd.__PyDist__._ExecDir+"settings.json"
newSjson = pd.__PyDist__._WorkDir+"settings.json"

class Program(MainUi.Ui_MainWindow,QObject):
    window = QMainWindow
    app = QApplication

    downloader = dl.Downloader
    versionChecker = vc.VersionChecker
    prefMng = pm.PreferencesManager

    aboutWindow = aw.AboutDialog
    addswitchesDialog = ad.AdditionalSwitchesDialog

    showConsole = False

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

    ignoredNewVersion = False

    def SetIcons(self):
        self.window.setWindowIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/ytdl.png")))

        self.ThemeMenu.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/theme.png")))
        self.AdditionalSwitches.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/plus.png")))

        self.ConsoleOption.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/console.png")))

        self.CommandHelpMenu.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/question.png")))
        self.Support.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/support.png")))
        self.About.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/about.png")))

        self.DownloadButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/miniArrow.png"))

        self.DestinationButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/folder.png"))

        #print(pd.__PyDist__._WorkDir)
    
    def SetupStatusBar(self):
        self.StatusBar.showMessage("Ready")
        self.StatusBar.addPermanentWidget(QLabel("In preperation"))

    def eventFilter(self, obj:QObject, event:QEvent):
        if obj is self.ConsoleDock and event.type() == QEvent.Type.Close: self.ConsoleOption.setChecked(False)
        return super().eventFilter(obj, event)

    def setupUi(self, MainWindow:QMainWindow, app:QApplication):

        self.app = app
        self.app.setStyle("Fusion")

        self.window = MainWindow

        resp=super().setupUi(MainWindow)

        self.SetIcons()
        self.SetupStatusBar()

        self.window.resize(0,390)
        self.ConsoleDock.close()

        self.VideoOption.setChecked(True)

        self.prefMng = pm.PreferencesManager(currSjson)
        
        self.isDarkTheme = self.prefMng.settings["isDarkTheme"]

        self.UrlTextBox.setText(self.prefMng.settings["savedConfig"]["url"])

        self.AudioOption.setChecked(self.prefMng.settings["savedConfig"]["audioOnly"])
        self.TemplateInput.setText(self.prefMng.settings["savedConfig"]["template"])
        self.RangeInput.setText(self.prefMng.settings["savedConfig"]["range"])

        self.DestinationInput.setText(self.prefMng.settings["savedConfig"]["destination"])

        if self.isDarkTheme:
            self.ToDarkTheme()
        else:
            self.ToLightTheme()

        #self.Downloader = dl.Downloader(".\\youtube-dl\\")

        self.downloader = dl.Downloader(pd.__PyDist__._WorkDir+"youtube-dl\\",self.ConsoleAddLine,self.Downloaded_Ended)
        
        self.aboutWindow = aw.AboutDialog(
            version=pd.__PyDist__.GetAppVersion(),
            aboutGif=pd.__PyDist__._WorkDir+"assets/ytdl.gif",
            windowIcon=pd.__PyDist__._WorkDir+"assets/ytdl.png"
        )
        self.About.triggered.connect(self.aboutWindow.Execute)
        self.Support.triggered.connect(lambda: webbrowser.open_new_tab("https://github.com/MatusGuy/youtube-dl_GUI/issues"))

        self.LightOption.triggered.connect(self.ToLightTheme)
        self.DarkOption.triggered.connect(self.ToDarkTheme)

        self.addswitchesDialog = ad.AdditionalSwitchesDialog(self.prefMng.settings["additionalSwitches"],pd.__PyDist__._WorkDir+"assets/ytdl.png")
        self.AdditionalSwitches.triggered.connect(lambda: self.prefMng.SetSetting(["additionalSwitches"],self.addswitchesDialog.Execute()))

        self.youtube_dlHelp.triggered.connect(lambda: ch.CmdHelpDialog().GetHelp(pd.__PyDist__._WorkDir+"youtube-dl\\youtube-dl.exe --help"))
        self.ffmpegHelp.triggered.connect(lambda: ch.CmdHelpDialog("ffmpeg command line help").GetHelp(pd.__PyDist__._WorkDir+"youtube-dl\\ffmpeg.exe --help"))


        self.ConsoleDock.installEventFilter(self)
        self.ConsoleOption.triggered.connect(lambda: self.ConsoleDock.setHidden(not self.ConsoleOption.isChecked()))

        self.UrlTextBox.editingFinished.connect(lambda: self.prefMng.SetSetting(["savedConfig","url"],self.UrlTextBox.text()))
        self.DestinationInput.editingFinished.connect(lambda: self.prefMng.SetSetting(["savedConfig","destination"],self.DestinationInput.text()))

        self.AudioOption.toggled.connect(lambda: self.prefMng.SetSetting(["savedConfig","audioOnly"],self.AudioOption.isChecked()))
        self.TemplateInput.editingFinished.connect(lambda: self.prefMng.SetSetting(["savedConfig","template"],self.TemplateInput.text()))
        self.RangeInput.editingFinished.connect(lambda: self.prefMng.SetSetting(["savedConfig","range"],self.RangeInput.text()))

        self.DestinationButton.pressed.connect(self.SetOutput)
        self.DownloadButton.pressed.connect(self.Download)

        if pd.__PyDist__._isBundle: app.aboutToQuit.connect(lambda: self.prefMng.WriteJSON(self.prefMng.filename,self.prefMng.settings))

        self.versionChecker = vc.VersionChecker(self.AlertVersion,60000)
        self.versionChecker.StartChecking()

        return resp
    
    def AlertVersion(self,NewVer="",OldVer=""):
        #print("version check")

        if self.downloader.IsDownloading(): return

        versionMsg = QMessageBox()
        versionMsg.setIcon(QMessageBox.Icon.Information)
        versionMsg.setWindowTitle("youtube-dl GUI")
        versionMsg.setText("There's a new version of youtube-dl GUI available.\nRestart the application to apply it.\n\nClose the application?")
        versionMsg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        versionMsg.setWindowIcon(QIcon(pd.__PyDist__._WorkDir+'assets/ytdl.png'))
        versionMsg.setModal(True)

        def OpenConfirmation(button:QAbstractButton):
            #print(f"open confirmation\nsaid yes: {button.text() == 'Yes'}\nbutton text: {button.text()}")
            if button.text() == "&Yes":
                self.window.close()
            else:
                self.versionChecker.StopChecking()
                versionMsg.close()
        
        versionMsg.buttonClicked.connect(OpenConfirmation)

        versionMsg.exec_()
            
    def SaveTheme(self,dark):
        self.DarkOption.setChecked(dark)
        self.LightOption.setChecked(not dark)
        self.isDarkTheme = self.DarkOption.isChecked()

        self.prefMng.SetSetting(["isDarkTheme"],dark)
    
    def ToLightTheme(self):
        self.app.setPalette(QPalette())
        self.window.setPalette(QPalette())
        self.SaveTheme(False)
    
    def ToDarkTheme(self):
        self.app.setPalette(self.darkTheme)
        self.window.setPalette(self.darkTheme)
        self.SaveTheme(True)

    def ConsoleAddLine(self,text):
        self.DownloadProgress.setEnabled(True)

        if type(text)==bytes:
            txt=text.decode("ASCII")
        else:
            txt=text
        self.ConsoleTextBox.appendPlainText(txt)

        uppered = txt.upper()
        #print(uppered)

        if "%" in uppered and "[DOWNLOAD] " in uppered:
            cut1 = txt.split("] ")[1]
            cut2 = cut1.split("% ")
            result = cut2[0].replace(" ","0")

            self.DownloadProgress.setValue(int(float(result)))
            #self.StatusDownloadProgress.setValue(int(float(result)))

            if not os.path.exists(self.DestinationInput.text()):
                if "100%" in uppered:
                    self.SpeedLabel.setText("Speed: ")
                    self.ETALabel.setText("ETA: ")
                else:
                    otherInfo = cut2[1].split(" ")
                    fileSize = otherInfo[1]
                    dwSpeed = otherInfo[3]
                    eta = otherInfo[5]

                    self.FileSizeLabel.setText("Total file size: "+fileSize)
                    self.SpeedLabel.setText("Speed: "+dwSpeed)
                    self.ETALabel.setText("ETA: "+eta)
        
        if "[DOWNLOAD] DOWNLOADING VIDEO" in uppered and "OF" in uppered:
            cut1 = txt.split(" ")
            self.currentFilePos = cut1[3]
            self.listLength = cut1[5]
        
        """
        if "[DOWNLOAD] DESTINATION: " in uppered:
            prefixRemoval1 = txt.removeprefix("[download] Destination: ")
            cut1 = prefixRemoval1.split("\\")
            currentFile = cut1[len(cut1)-1]

            self.CurrentFile.setText("Current: "+currentFile.removesuffix("(tmp)"))
            self.FilesLabel.setText(f"Files: {self.currentFilePos}/{self.listLength}")
        """
        
        if "ERROR: " in uppered:
            if "YOUTUBE-DL.EXE: ":
                self.error = txt.removeprefix("youtube-dl.EXE: error: ").capitalize()
            else:
                self.error = txt.removeprefix("ERROR: ").capitalize()
            #print(self.error)

    def DisableDownloadGui(self,disable):
        self.FileSizeLabel.setEnabled(not disable)
        self.SpeedLabel.setEnabled(not disable)
        self.ETALabel.setEnabled(not disable)
        self.DownloadProgress.setEnabled(not disable)
        #self.DownloadButton.setEnabled(disable)
        #self.CurrentFile.setEnabled(not disable)
        #self.FilesLabel.setEnabled(not disable)

        if disable:
            self.DownloadProgress.setValue(0)
            self.FileSizeLabel.setText("Total file size: ")
            self.SpeedLabel.setText("Speed: ")
            self.ETALabel.setText("ETA: ")
            #self.FilesLabel.setText("Files: ")
            #self.CurrentFile.setText("Current: ")
    
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
                "EXTRA":self.addswitchesDialog.TextEdit.toPlainText().replace("\n"," "),
            }
            ##print(str(Config))
            #self.ExecuteDownload(Config)
            self.ConsoleTextBox.setPlainText("")
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
                #print (wresult)
                if len(wresult): os.system("explorer "+wresult)

        msg.buttonClicked.connect(OpenDownloaded)
        
        msg.exec_()

        self.DisableDownloadGui(True)

def window():
    app = QApplication(sys.argv)

    window = QMainWindow()

    program = Program()
    program.setupUi(window,app)

    #QtCore.QTimer.singleShot(250, HideSplash)
    psh.Splash_loadcomplete(2000)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

    window()