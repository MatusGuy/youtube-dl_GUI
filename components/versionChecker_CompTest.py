import sys,os

from downloader import Downloader
sys.path.insert(1,'.')

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

import versionChecker as vc

class Vc_CompTest(object):
    versionChecker = None
    downloader = None

    def __init__(self,window):
        self.versionChecker = vc.VersionChecker(self.NewVersionAction,1000) #check every second just for testing
        self.window=window

    def NewVersionAction(self,newVer,oldVer):
        print (f"New Version Available {newVer}. Old version:{oldVer}")
        self.window.close()

    
    def main(self,app):
        print ("VersionChecker Component Test Begin")

        self.versionChecker._debug=True

        print (f"Version number: {self.versionChecker.ConvLst2Str([1,2],False)}")

        # NEW older than Bak
        #self.versionChecker._SetFileToCheck(".\\dist\\test\\youtube-dl_GUI_1_2_1_1.exe",".\\dist\\test\\youtube-dl_GUI_1_2_3_1.exe")

        # SAME VERSIONT
        #self.versionChecker._SetFileToCheck(".\\dist\\test\\youtube-dl_GUI_1_2_1_1.exe",".\\dist\\test\\youtube-dl_GUI_1_2_1_1.exe")

        # New Version
        self.versionChecker._SetFileToCheck(".\\dist\\test\\youtube-dl_GUI_1_2_3_1.exe",".\\dist\\test\\youtube-dl_GUI_1_2_1_1.exe")

        print (f"Application Version: {self.versionChecker.GetAppVersion()}")

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