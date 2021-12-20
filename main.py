import sys,os
from pathlib import Path
from typing import Optional
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import youtubedl_gui_class as MainUi

class Program(MainUi.Ui_MainWindow):
    url = ""
    output = ""
    audioOnly = False

    def setupUi(self, MainWindow):
        resp=super().setupUi(MainWindow)

        self.VideoOption.setChecked(True)

        #MainWindow.setWindowIcon(QtGui.QIcon().addPixmap(QtGui.QPixmap("./assets/window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off))

        self.UrlTextBox.setText("https://www.youtube.com/watch?v=jNQXAC9IVRw")
        self.DestinationInput.setText(str(Path.home())+"\MyVideo.mp4")

        self.DestinationButton.pressed.connect(self.SetDirectory)
        self.DownloadButton.pressed.connect(self.Download)

        return resp
    
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

        self.output = filename[0] if len(filename[0]) else self.output
        self.DestinationInput.setText(self.output)

    def Download(self):
        self.DownloadButton.setEnabled(False)
        self.MainWidget.update()
        self.url = self.UrlTextBox.text()

        Config={
            "URL":self.url,
            "AUDIO_ONLY":self.audioOnly,
            "OUTPUT":self.output,
        }
        #print(str(Config))
        self.ExecuteDownload(Config)
        self.DownloadButton.setEnabled(True)

        msg = QMessageBox(parent=self.DownloadButton)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Download complete!")
        msg.setWindowTitle("youtube-dl GUI")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def ExecuteDownload(self,params):
        downloader = f".\\youtube-dl\\youtube-dl.exe"
        options = ""
        tmp = ""

        def CutToExtension(pathText):
            cut1 = params["OUTPUT"].split("/")
            cut2 = cut1[len(cut1)-1].split(".")
            return cut2[len(cut2)-1]


        if params["AUDIO_ONLY"]:
            options = f"--audio-format {CutToExtension(params['OUTPUT'])} --extract-audio "
            tmp = "(tmp)"
        else:
            options = f"--format {CutToExtension(params['OUTPUT'])} "
        
        output = f'--output \"{params["OUTPUT"]}{tmp}\"'

        command = f'{downloader} \"{params["URL"]}\" {options}{output}'
        #print(command)

        os.system(command)
        


def window():
    app = QApplication(sys.argv)
    window = QMainWindow()

    hellowindow = Program()
    hellowindow.setupUi(window)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()