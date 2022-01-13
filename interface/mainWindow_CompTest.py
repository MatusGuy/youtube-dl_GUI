import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import MainWindow as mw
from dist import pydist as pd

class MW_CompTest(object):
    ui = mw

    def main(self,window:QMainWindow,app:QApplication):
        print("About window component test: start")
        
        self.ui = mw(window,app)

        self.ui.SetDownloadCallback(self.DownloadCallback)

        window.show()
        app.exec_()



        print("About window component test: complete")
    
    def DownloadCallback(self):
        self.ui.ActivateCancelIcon()
        self.ui.DownloadEndDialog(0)
        self.ui.ActivateDownloadIcon

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = QMainWindow()
    
    theApp= MW_CompTest()
    sys.exit(theApp.main(window,app))