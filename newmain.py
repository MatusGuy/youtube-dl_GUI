import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QEvent, QObject
from interface.newmainUi import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QDockWidget, QMainWindow

class NewProgram(Ui_MainWindow,QMainWindow):
    window = QtWidgets.QMainWindow
    app = QtWidgets.QApplication

    def __init__(self,window:QtWidgets.QMainWindow,app:QtWidgets.QApplication) -> None:
        self.window = window
        self.app = app

        resp = super().__init__()
        self.setupUi(window)

        ##### Initialization #####

        self.app.setStyle("Fusion")

        self.Console.hide()

        self.DownloadInfo

        ####  Icons           ####

        self.window.setWindowIcon(QtGui.QIcon("assets/ytdl.png"))

        self.ConsoleOption.setIcon(QtGui.QIcon("assets/consoleIcon.png"))
        self.Theme.setIcon(QtGui.QIcon("assets/theme.png"))
        self.About.setIcon(QtGui.QIcon("assets/about.png"))

        ##### Connections    #####

        self.ConsoleOption.triggered.connect(lambda: self.Console.setHidden(not self.ConsoleOption.isChecked()))
        self.Console.installEventFilter(self)

        return resp

    def eventFilter(self, obj:QObject, event:QEvent):
        if obj is self.Console and event.type() == QEvent.Type.Close: self.ConsoleOption.setChecked(False)
        return super().eventFilter(obj, event)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    program = NewProgram(window,app)
    window.show()
    sys.exit(app.exec_())