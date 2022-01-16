import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import MainWindow as mw
from dist import pydist as pd

class MW_CompTest(object):
    def main(self,window:QMainWindow,app:QApplication):
        print("Main window component test: start")
        
        self.ui = mw(window,app)

        self.ui.SetDownloadCallback(self.DownloadCallback)

        window.show()

        self.ui.SetURL("http://test.site.me")
        self.ui.SetAudioOnly(False)
        self.ui.SetOutput("C:\\")

        self.ui.SetProgress(50)
        self.ui.SetDownloadInfo("12m00s","2 Mbps","100Mb",current="c:\long path for a file name where it will be placed\you know.mp3")

        app.exec_()

        print("Main window component test: complete")
    
    def DownloadCallback(self):
        print ("DownloadCallBack")
        self.ui.CancelIcon()
        self.ui.SetDownloadText("Cancel\ndownload!")

        self.ui.AppendConsole("Start downloading...")
        self.ui.ShowStatusMessage("Operating: test")

        self.ui.AppendConsole("Download ended.")
        self.ui.DownloadEndDialog(1,"errormessage goes here")

        self.ui.ClearStatusMessage()
        self.ui.ClearConsole()
        self.ui.SetDownloadText("Start\ndownload!")
        self.ui.DownloadIcon()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    
    theApp= MW_CompTest()
    sys.exit(theApp.main(window,app))