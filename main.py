import sys,os
from pathlib import Path
from typing import Optional
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import youtubedl_gui_class as MainUi
import downloader as dl

class Program(MainUi.Ui_MainWindow):
    window = None
    url = ""
    output = ""
    audioOnly = False
    downloader = dl.Downloader()
    showConsole = False

    def setupUi(self, MainWindow):
        self.window = MainWindow

        resp=super().setupUi(MainWindow)

        self.VideoOption.setChecked(True)

        self.ViewConsole.setStyleSheet("QCheckBox::indicator:checked"
                                       "{"
                                       "border-image : url(assets/openedArrow.png);"
                                       "}"
                                       "QCheckBox::indicator:unchecked"
                                       "{"
                                       "border-image : url(assets/closedArrow.png);"
                                       "}")

        #MainWindow.setWindowIcon(QtGui.QIcon().addPixmap(QtGui.QPixmap("./assets/window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off))

        self.UrlTextBox.setText("https://www.youtube.com/watch?v=jNQXAC9IVRw")
        self.DestinationInput.setText(str(Path.home())+"\MyVideo.mp4")
        self.output = self.DestinationInput.text()

        self.DestinationButton.pressed.connect(self.SetDirectory)
        self.DownloadButton.pressed.connect(self.Download)
        self.ViewConsole.toggled.connect(self.ToggleConsole)

        #self.Downloader = dl.Downloader(".\\youtube-dl\\")

        self.downloader = dl.Downloader(".\\youtube-dl\\",self.ConsoleAddLine,self.Downloaded_Ended)

        return resp
    
    def ConsoleAddLine(self,text):
        self.DownloadProgress.setEnabled(True)

        if type(text)==bytes:
            txt=text.decode("ASCII")
        else:
            txt=text
        #print (txt)
        self.ConsoleWidget.appendPlainText(txt)

        if "%" in txt:
            cut1 = txt.split("] ")[1]
            cut2 = cut1.split("%")[0]
            result = cut2.replace(" ","0")

            self.DownloadProgress.setValue(int(float(result)))

    def ToggleConsole(self):
        self.showConsole = not self.showConsole
        if self.showConsole:
            self.window.resize(531, 607)
        else:
            self.window.resize(531, 345)


    
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
        self.DownloadButton.setEnabled(True)
        self.DownloadButton.setEnabled(False)
        self.MainWidget.update()
        self.url = self.UrlTextBox.text()

        Config={
            "URL":self.url,
            "AUDIO_ONLY":self.audioOnly,
            "OUTPUT":self.output,
        }
        #print(str(Config))
        #self.ExecuteDownload(Config)
        self.ConsoleWidget.setPlainText("")
        self.DownloadProgress.setValue(0)
        self.downloader.StartDownload(Config)


    def Downloaded_Ended(self,errorcode):
        self.DownloadProgress.setEnabled(False)
        self.DownloadButton.setEnabled(True)

        self.ConsoleAddLine("Download complete")

        msg = QMessageBox()
        msg.setIconPixmap(QtGui.QPixmap("./assets/window.png"))

        if errorcode!=0:
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Download failed!")
            msg.setInformativeText("Check \"View details\" for info regarding this issue.")
            msg.setWindowTitle("youtube-dl GUI")
            msg.setStandardButtons(QMessageBox.Ok)
        else:
            msg.setIcon(QMessageBox.Information)
            msg.setText("Download successful!")
            msg.setWindowTitle("youtube-dl GUI")
            msg.setStandardButtons(QMessageBox.Ok)

        msg.exec_()


def window():
    app = QApplication(sys.argv)
    window = QMainWindow()

    hellowindow = Program()
    hellowindow.setupUi(window)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()