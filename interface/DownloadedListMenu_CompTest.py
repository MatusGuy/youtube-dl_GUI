import sys
sys.path.insert(1,".")

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QWidget, QTableWidgetItem
from interface.DownloadedListMenu import DownloadedListMenu as dwlmenu
from dist import pydist as pd

class MW_CompTest(object):
    def main(self,window:QMainWindow,app:QApplication):
        print("Main window component test: start")

        self.widget = QWidget(window)
        window.setCentralWidget(self.widget)

        self.table = QTableWidget(self.widget)
        self.table.setFixedSize(500,500)
        self.table.setColumnCount(10)
        self.table.setRowCount(10)
        self.table.setItem(0,0,QTableWidgetItem("C:\\Users\\Mateus\\C - Me at the zoo.mp4"))
        self.table.setItem(0,2,QTableWidgetItem("Downloading"))
        self.table.setItem(1,0,QTableWidgetItem("C:\\Users\\Mateus\\D - Me not at the zoo.mp4"))
        self.table.setItem(1,2,QTableWidgetItem("not downloading"))

        self.menu = dwlmenu(self.table,app.clipboard(),self.widget)

        window.show()

        app.exec_()

        print("Main window component test: complete")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    
    theApp= MW_CompTest()
    sys.exit(theApp.main(window,app))