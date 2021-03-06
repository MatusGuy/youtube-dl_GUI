import sys
sys.path.insert(1,".")
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor
from mainWindow import MainWindow as mw
from components.prefMng import PreferencesManager as pm
from dist import pydist as pd
from os import getcwd as cwd

class MW_CompTest(QObject):

    def main(self,window:QMainWindow,app:QApplication):
        self.window = window

        print(f"Main window component test ({cwd()}): start")
        
        self.ui = mw(self.window,app,prefMng=pm("testSettings.json"))

        self.ui.SetDownloadCallback(self.DownloadCallback)

        #self.window.installEventFilter(self)
        #self.window.show()

        self.ui.SetProgressColour(QColor(177, 150, 62))

        self.ui.SetURL("http://test.site.me")
        self.ui.SetAudioOnly(False)
        self.ui.SetOutput("C:\\")

        self.ui.SetProgress(50)
        self.ui.SetDownloadInfo("12m00s","2 Mbps","100Mb",current="c:\long path for a file name where it will be placed\you know.mp3")

        self.ui.ClearStatusMessage()
        self.ui.ShowStatusMessage("message")

        self.ui.ListToDwList([{
                "FILENAME": "filename",
                "SIZE": "size",
                "TOTAL_TIME": "time",
                "DESTINATION": "dest",
                "STARTED": "started"
            }])

        app.exec_()

        print("Main window component test: complete")
    
    def DownloadCallback(self):
        print ("DownloadCallBack")

        self.ui.ClearConsole()

        self.ui.CancelIcon()
        self.ui.SetDownloadText("Cancel\ndownload!")
        self.ui.OperatingTaskbarOverlay()

        self.ui.AppendConsole("Start downloading...")
        self.ui.ShowStatusMessage("Operating: test")

        self.ui.SetProgress(100)
        self.ui.AppendConsole("Download ended.")
        self.ui.DownloadEndDialog(1,"errormessage goes here")
        self.ui.ClearTaskbarOverlay()

        self.ui.AppendConsole("lots\nof\ntext\nbeing\nsent\nat\nthis\nvery\nmoment\n.\nisn't\nthat\namazing\n?\n!\n?\n\n\nno\n,\nyou're\nnot\nfunny\n,\nmat")

        self.ui.ClearStatusMessage()
        self.ui.SetDownloadText("Start\ndownload!")
        self.ui.DownloadIcon()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    
    theApp= MW_CompTest()
    sys.exit(theApp.main(window,app))