import sys
sys.path.insert(1,'.')

from interface.addswitches_simpleUi import Ui_AdditionalSwitches as uis
from interface.addswitchesUi import Ui_AdditionalSwitches as ui

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class AdditionalSwitchesDialog(uis):
    gui = uis
    dialog = QDialog

    resp = str

    def __init__(self,savedswitches="",windowicon=""):
        super().__init__()

        self.dialog = QDialog(flags = Qt.WindowType.WindowCloseButtonHint)
        self.setupUi(self.dialog)
        
        self.dialog.setWindowIcon(QIcon(windowicon))
        self.TextEdit.setPlainText(savedswitches)
    
    def Open(self):
        self.dialog.open()
    
    def Close(self):
        self.dialog.close()
    
    def Execute(self) -> str:
        self.dialog.exec_()
        return self.TextEdit.toPlainText()