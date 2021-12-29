import sys,os
sys.path.insert(1,'.')

from PyQt5.QtWidgets import QApplication, QMainWindow

import versionChecker as vc

class Vc_CompTest(object):
    versionChecker = None

    def __init__(self,window):
        self.versionChecker = vc.VersionChecker(window,1000) #check every second just for testing
    
    def main(self,app):
        print ("VersionChecker Component Test Begin")

        self.versionChecker.StartChecking()
        resp=app.exec_()
        self.versionChecker.StopChecking()

        print ("VersionChecker Component Test End")
        return resp


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    vcheck=Vc_CompTest(window)
    sys.exit(vcheck.main(app))