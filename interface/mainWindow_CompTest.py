from sys import exit,argv as args
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import MainWindow as mw

class MW_CompTest(object):
    dialog = mw

    def main(self,window:QMainWindow,app:QApplication):
        print("About window component test: start")
        
        self.dialog = mw(window,app)

        window.show()
        app.exec_()

        print("About window component test: complete")

if __name__ == "__main__":
    app = QApplication(args)
    app.setStyle("Fusion")

    window = QMainWindow()
    
    theApp= MW_CompTest()
    exit(theApp.main(window,app))