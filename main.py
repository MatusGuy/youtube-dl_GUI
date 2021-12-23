from json import decoder
import sys,os,json
from os import close, curdir, fdopen
from pathlib import Path
from typing import Optional
from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QIcon,QPalette,QMovie
from PyQt5.QtCore import QRect, Qt,pyqtSlot
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


    def setupUi(self, MainWindow, app):
        self.app = app
        self.app.setStyle("Fusion")

        self.window = MainWindow

        resp=super().setupUi(MainWindow)

        self.window.resize(0,390)
        self.ConsoleOutput.setHidden(not self.showConsole)

        self.VideoOption.setChecked(True)

        self.DownloadButton.setIcon(QIcon("assets/miniArrow.png"))        

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

        self.DestinationButton.pressed.connect(self.SetOutput)
        self.DownloadButton.pressed.connect(self.Download)
        self.ViewConsole.toggled.connect(self.ToggleConsole)

        #self.Downloader = dl.Downloader(".\\youtube-dl\\")

        self.downloader = dl.Downloader(".\\youtube-dl\\",self.ConsoleAddLine,self.Downloaded_Ended)

        self.aboutGui = aboutWnd.Ui_About()
        self.aboutDialog = QDialog(self.window,Qt.WindowType.WindowCloseButtonHint)
        self.aboutGui.setupUi(self.aboutDialog)
        gif = QMovie("assets/ytdl.gif")
        self.aboutGui.IconGif.setMovie(gif)
        gif.start()
        self.aboutDialog.setModal(True)
        self.aboutGui.OKbt.pressed.connect(self.aboutDialog.close)
        
        self.AboutMenu.triggered.connect(self.aboutDialog.exec_)

        self.LightOption.triggered.connect(self.ToLightTheme)
        self.DarkOption.triggered.connect(self.ToDarkTheme)

        self.UrlTextBox.textEdited.connect(self.OnUrlEdit)
        self.DestinationInput.textEdited.connect(self.OnOutputEdit)

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
        self.ConsoleOutput.appendPlainText(txt)

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
        
        if "[download] Downloading video" in txt and "of" in txt:
            cut1 = txt.split(" ")
            self.currentFilePos = cut1[3]
            self.listLength = cut1[5]
        

        if "[download] Destination: " in txt:
            prefixRemoval1 = txt.removeprefix("[download] Destination: ")
            cut1 = prefixRemoval1.split("\\")
            currentFile = cut1[len(cut1)-1]

            self.CurrentFile.setText("Current: "+currentFile)
            self.FilesLabel.setText(f"Files: {self.currentFilePos}/{self.listLength}")
    
    def OnUrlEdit(self):
        newUrl = self.UrlTextBox.text()
        urlIsEmpty = newUrl == ""

        self.DownloadButton.setDisabled(urlIsEmpty)
    
    def OnOutputEdit(self):
        newOutput = self.DestinationInput.text()
        self.DownloadButton.setDisabled(newOutput == "")
        self.output = newOutput

    def ToggleConsole(self):

        X,Y,WW,WH=self.window.geometry().getRect()
        print(f"MAIN WINDOW :({X},{Y}..{WW},{WH})")
        
        if self.showConsole:
            CX,CY,CW,CH =self.ConsoleOutput.geometry().getRect()
            self.console_height=CH 
            print(f"CONSOLE:({CX},{CY}..{CW},{CH})")
        
        self.showConsole = not self.showConsole
        if self.showConsole:
            self.window.resize(WW,WH+self.console_height)
        else:
            self.window.resize(WW,WH-self.console_height)
        
        self.ConsoleOutput.setHidden(not self.showConsole)
    
    def resizeEvent(self,event):
        X,Y,WW,WH=self.window.geometry().getRect()
        print(f"MAIN WINDOW :({X},{Y}..{WW},{WH})")
        print(f"Event:{event}")
        QMainWindow.resizeEvent(self, event)

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

        self.DestinationInput.setText(filename[0] if len(filename[0]) else self.output)
        self.output = self.DestinationInput.text()
        print(self.output)

    def Download(self):
        if self.downloader.IsDownloading():
            print ("Cancel!!!??!?")
            self.downloader.CancelDownload()
        else:
            self.DisableDownloadGui(False)

            self.DownloadButton.setText("Cancel\ndownload")
            self.DownloadButton.setIcon(QIcon("assets/miniCross.png"))

            self.MainWidget.update()
            self.url = self.UrlTextBox.text()
            self.audioOnly = self.AudioOption.isChecked()

            Config={
                "URL":self.url,
                "AUDIO_ONLY":self.audioOnly,
                "OUTPUT":self.output,
                "TEMPLATE":self.TemplateInput.text(),
            }
            #print(str(Config))
            #self.ExecuteDownload(Config)
            self.ConsoleOutput.setPlainText("")
            self.currentFilePos = 1
            self.listLength = 1
            self.downloader.StartDownload(Config)


    def Downloaded_Ended(self,errorcode):
        self.DownloadProgress.setEnabled(False)
        self.DownloadButton.setEnabled(True)

        print("error: "+str(errorcode))

        self.ConsoleAddLine("Download process ended")

        self.DownloadButton.setIcon(QIcon("assets/miniArrow.png"))
        self.DownloadButton.setText("Start\ndownload!") 

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