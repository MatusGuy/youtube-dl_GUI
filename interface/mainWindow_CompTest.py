import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import MainWindow as mw
from dist import pydist as pd

class MW_CompTest(object):
    ui = mw

    def main(self,window:QMainWindow,app:QApplication):
        print("Main window component test: start")
        
        self.ui = mw(window,app)

        self.ui.SetDownloadCallback(self.DownloadCallback)

        window.show()
        app.exec_()

        print("Main window component test: complete")
    
    def DownloadCallback(self):
        self.ui.CancelIcon()

        self.ui.AppendConsole("Start downloading...")

        self.ui.AppendConsole("Download ended.")
        self.ui.DownloadEndDialog(0)

        self.ui.ClearConsole()
        self.ui.DownloadIcon()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    
    theApp= MW_CompTest()
    sys.exit(theApp.main(window,app))