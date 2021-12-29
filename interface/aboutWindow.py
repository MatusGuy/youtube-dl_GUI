import sys
sys.path.insert(1,'.')

from interface.aboutUi import Ui_About as ui

from PyQt5 import QtWidgets, QtGui, QtCore

from dist import pydist as pd

class AboutDialog():
    aboutDialog = QtWidgets.QDialog
    aboutGui = ui

    def __init__(self,version=None,aboutGif=pd.__PyDist__._WorkDir+"assets/ytdl.gif",windowIcon=None):
        self.aboutGui = ui()
        self.aboutDialog = QtWidgets.QDialog(flags = QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.aboutGui.setupUi(self.aboutDialog)
        gif = QtGui.QMovie(aboutGif)
        
        version="0.0.0.0" if not version else version
        self.aboutGui.Version.setText("(x64) Version "+version)

        self.aboutGui.IconGif.setMovie(gif)
        gif.start()
        self.aboutDialog.setModal(True)
        self.aboutDialog.setWindowIcon(QtGui.QIcon(windowIcon if windowIcon else pd.__PyDist__._WorkDir+"assets/ytdl.png"))
        self.aboutGui.OKbt.pressed.connect(self.aboutDialog.close)
    
    def Open(self):
        self.aboutDialog.open()
    
    def Close(self):
        self.aboutDialog.close()
    
    def Execute(self):
        self.aboutDialog.exec_()