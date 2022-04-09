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
    audio = bool

    def __init__(self,savedswitches="",windowicon=""):
        self.dialog = QDialog(flags = Qt.WindowType.WindowCloseButtonHint)
        super().setupUi(self.dialog)
        
        self.dialog.setWindowIcon(QIcon(windowicon))
        self.TextEdit.setPlainText(savedswitches)
        self.HelpMenu.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/help_index.png"))

        self.OkButton.pressed.connect(self.Close)

    def _SetAudio(self,audio:bool):
        self.audio = audio
    
    def Open(self):
        self.dialog.open()
    
    def Close(self):
        self.dialog.close()
    
    def Execute(self) -> str:
        self.dialog.exec_()
        return self.Get()
    
    def Set(self,value:str):
        """Changes additional switches depending if global, video, or audio is chosen"""

        if self.GlobalOption.isChecked():
            self.TextEdit.setPlainText(value)
        else:
            if self.audio:
                self.AudioTextEdit.setPlainText(value)
            else:
                self.VideoTextEdit.setPlainText(value)
    def SetGlobal(self,value:str):
        self.TextEdit.setPlainText(value)
    def SetVideo(self,value:str):
        self.VideoTextEdit.setPlainText(value)
    def SetAudio(self,value:str):
        self.AudioTextEdit.setPlainText(value)
    
    def _Get(self) -> str:
        return self.TextEdit.toPlainText().replace("\r"," ").replace("\n"," ")
    def Get(self):
        """Returns additional switches depending if global, video, or audio is chosen"""
        
        if self.GlobalOption.isChecked():
            resp = self.TextEdit.toPlainText()
        else:
            if self.audio:
                resp = self.AudioTextEdit.toPlainText()
            else:
                resp = self.VideoTextEdit.toPlainText()
        
        return resp
    def GetGlobal(self):
        return self.TextEdit.toPlainText()
    def GetVideo(self):
        return self.VideoTextEdit.toPlainText()
    def GetAudio(self):
        return self.AudioTextEdit.toPlainText()