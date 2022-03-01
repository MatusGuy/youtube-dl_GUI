import sys
sys.path.insert(1,'.')

from interface.addswitches_simpleUi import Ui_AdditionalSwitches as ui

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from dist import pydist as pd

class AdditionalSwitchesDialog(ui):
    gui = ui
    dialog = QDialog

    resp = str

    def __init__(self,savedswitches="",windowicon=""):
        self.dialog = QDialog(flags = Qt.WindowType.WindowCloseButtonHint)
        super().setupUi(self.dialog)
        
        self.dialog.setWindowIcon(QIcon(windowicon))
        self.TextEdit.setPlainText(savedswitches)
        self.HelpMenu.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/help_index.png"))

        self.OkButton.pressed.connect(self.Close)
    
    def Open(self):
        self.dialog.open()
    
    def Close(self):
        self.dialog.close()
    
    def Execute(self) -> str:
        self.dialog.exec_()
        return self.Get()
    
    def Set(self,value:str):
        return self.TextEdit.setPlainText(value)
    def Get(self) -> str:
        return self.TextEdit.toPlainText().replace("\r"," ").replace("\n"," ")