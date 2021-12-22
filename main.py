import builtins
from json import decoder
import sys,os,json
from os import close, curdir, fdopen
from pathlib import Path
from typing import Optional
from PyQt5 import QtGui
from PyQt5.QtGui import QColor,QPalette
from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtWidgets import *
import youtubedl_gui_class as MainUi
import downloader as dl
import youtubedl_about_class as aboutWnd

#from settingsGuis.themePrompt_class import Ui_ChangeTheme as ThemesGui

sjson = "settings.json"

class Program(MainUi.Ui_MainWindow):
    window = None
    app = None

    url = ""
    output = ""
    audioOnly = False
    downloader = dl.Downloader()
    showConsole = False
    
    aboutDialog=None
    aboutGui=None

    videos=0

    bigWindowHeight = 717
    smallWindowHeight = 436

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

    def setupUi(self, MainWindow, app):
        self.app = app
        self.app.setStyle("Fusion")

        self.window = MainWindow

        resp=super().setupUi(MainWindow)

        self.VideoOption.setChecked(True)

        currentSettings,file = self.GetJSON(sjson)
        self.isDarkTheme = currentSettings["isDarkTheme"]
        file.close()

        if self.isDarkTheme:
            self.ToDarkTheme()
        else:
            self.ToLightTheme()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/ytdl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.window.setWindowIcon(icon)

        self.UrlTextBox.setText("https://www.youtube.com/watch?v=jNQXAC9IVRw")
        self.DestinationInput.setText(str(Path.home())+"\MyVideo.mp4")
        self.output = self.DestinationInput.text()

        self.DestinationButton.pressed.connect(self.SetDirectory)
        self.DownloadButton.pressed.connect(self.Download)
        self.ViewConsole.toggled.connect(self.ToggleConsole)

        #self.Downloader = dl.Downloader(".\\youtube-dl\\")

        self.downloader = dl.Downloader(".\\youtube-dl\\",self.ConsoleAddLine,self.Downloaded_Ended)

        self.aboutGui = aboutWnd.Ui_About()
        self.aboutDialog = QDialog(self.window,Qt.WindowType.WindowCloseButtonHint)
        self.aboutGui.setupUi(self.aboutDialog)
        self.aboutDialog.setModal(True)
        self.aboutGui.OKbt.pressed.connect(self.aboutDialog.close)
        
        self.AboutMenu.triggered.connect(self.aboutDialog.exec_)

        self.LightOption.triggered.connect(self.ToLightTheme)
        self.DarkOption.triggered.connect(self.ToDarkTheme)

        return resp
    
    def GetJSON(self,file,closeFile=True):
        with open(file) as j:
            try:
                return json.load(j),j
            except ValueError as e:
                if closeFile: j.close()
                raise Exception('Invalid json: {}'.format(e)) from None

    def SetJSON(self,file,data,closeFile=True):
        with open(file, "w") as outfile:
            json.dump(data,outfile)

    def SaveTheme(self,dark):
        self.DarkOption.setChecked(dark)
        self.LightOption.setChecked(not dark)
        self.isDarkTheme = self.DarkOption.isChecked()

        currentSettings,file = self.GetJSON(sjson)
        currentSettings["isDarkTheme"] = self.isDarkTheme
        self.SetJSON(sjson, currentSettings)
        file.close()
    
    def ToLightTheme(self):
        self.app.setPalette(QPalette())
        self.window.setPalette(QPalette())
        self.ViewConsole.setStyleSheet("QCheckBox::indicator:checked"
                                       "{"
                                       "border-image : url(assets/openedArrow.png);"
                                       "}"
                                       "QCheckBox::indicator:unchecked"
                                       "{"
                                       "border-image : url(assets/closedArrow.png);"
                                       "}")
        self.SaveTheme(False)
    
    def ToDarkTheme(self):
        self.app.setPalette(self.darkTheme)
        self.window.setPalette(self.darkTheme)
        self.ViewConsole.setStyleSheet("QCheckBox::indicator:checked"
                                       "{"
                                       "border-image : url(assets/openedArrowDark.png);"
                                       "}"
                                       "QCheckBox::indicator:unchecked"
                                       "{"
                                       "border-image : url(assets/closedArrowDark.png);"
                                       "}")
        self.SaveTheme(True)

    def ConsoleAddLine(self,text):
        self.DownloadProgress.setEnabled(True)

        if type(text)==bytes:
            txt=text.decode("ASCII")
        else:
            txt=text
        #print (txt)
        self.ConsoleWidget.appendPlainText(txt)

        if "%" in txt and "[download] " in txt:
            cut1 = txt.split("] ")[1]
            cut2 = cut1.split("% ")
            result = cut2[0].replace(" ","0")

            self.DownloadProgress.setValue(int(float(result)))

            if not os.path.exists(self.output):
                if "100%" in txt:
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
        
        if "[download] Downloading" in txt and "of" in txt and "/playlist?" in self.url:
            cut = txt.split(" ")
            currentFilePos = cut[3]
            listLength = cut[5]

            self.FilesLabel.setText(f"Files: {currentFilePos}/{listLength}")
        
        if "[download] Destination: " in txt and "/playlist?" in self.url:
            currentFile = txt.removeprefix("[download] Destination: ")
            self.CurrentFile.setText("Current: \n"+currentFile)

    def ToggleConsole(self):
        self.showConsole = not self.showConsole
        if self.showConsole:
            self.window.setMinimumHeight(self.bigWindowHeight)
            self.window.setMaximumHeight(self.bigWindowHeight)
            self.window.resize(531, self.bigWindowHeight)
        else:
            self.window.setMinimumHeight(self.smallWindowHeight)
            self.window.setMaximumHeight(self.smallWindowHeight)
            self.window.resize(531, self.smallWindowHeight)

    def DisableDownloadGui(self,disable):
        self.FileSizeLabel.setEnabled(not disable)
        self.DownloadSpeedLabel.setEnabled(not disable)
        self.ETALabel.setEnabled(not disable)
        self.DownloadProgress.setEnabled(not disable)
        self.DownloadButton.setEnabled(disable)
        self.CurrentFile.setEnabled(not disable)
        self.FilesLabel.setEnabled(not disable)

        if disable:
            self.DownloadProgress.setValue(0)
            self.FileSizeLabel.setText("Total file size: ")
            self.DownloadSpeedLabel.setText("Speed: ")
            self.ETALabel.setText("ETA: ")
            self.FilesLabel.setText("Files: ")
            self.CurrentFile.setText("Current: ")
    
    def SetDirectory(self):
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

        self.DestinationInput.setText(filename[0] if len(filename[0]) else self.output)
        self.output = self.DestinationInput.text()
        print(self.output)

    def Download(self):
        self.DisableDownloadGui(False)
        self.MainWidget.update()
        self.url = self.UrlTextBox.text()

        Config={
            "URL":self.url,
            "AUDIO_ONLY":self.audioOnly,
            "OUTPUT":self.output,
            "PLAYLIST":"/playlist?" in self.url,
        }
        #print(str(Config))
        #self.ExecuteDownload(Config)
        self.ConsoleWidget.setPlainText("")
        self.downloader.StartDownload(Config)


    def Downloaded_Ended(self,errorcode):
        self.DownloadProgress.setEnabled(False)
        self.DownloadButton.setEnabled(True)

        self.ConsoleAddLine("Download complete")

        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('assets/ytdl.png'))

        if errorcode!=0:
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Finished downloading unsuccessfully!")
            msg.setInformativeText("Check \"Console output\" for detail regarding this issue.")
            msg.setWindowTitle("youtube-dl GUI")
            msg.setStandardButtons(QMessageBox.Ok)
        else:
            msg.setIcon(QMessageBox.Information)
            msg.setText("Finished downloading successfully!")
            msg.setWindowTitle("youtube-dl GUI")
            msg.setStandardButtons(QMessageBox.Ok)
        
        msg.exec()

        self.DisableDownloadGui(True)

def window():
    app = QApplication(sys.argv)

    window = QMainWindow()

    hellowindow = Program()
    hellowindow.setupUi(window,app)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()