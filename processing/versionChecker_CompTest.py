import sys,os

from downloader import Downloader
sys.path.insert(1,'.')

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

import versionChecker as vc

class Vc_CompTest(object):
    versionChecker = None
    downloader = None

    def __init__(self,window):
        self.versionChecker = vc.VersionChecker(window,Downloader,1000) #check every second just for testing
    
    def main(self,app):
        print ("VersionChecker Component Test Begin")

        self.versionChecker._debug=True
        self.versionChecker._SetFileToCheck(".\\dist\\youtube-dl_GUI_1.exe",".\\dist\\youtube-dl_GUI_2.exe")

        self.versionChecker.StartChecking()
        resp = app.exec_()
        self.versionChecker.StopChecking()

        print ("VersionChecker Component Test End")
        return resp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    centralwidget = QWidget()
    window.setCentralWidget(centralwidget)

    vcheck=Vc_CompTest(window)

    sys.exit(vcheck.main(app))