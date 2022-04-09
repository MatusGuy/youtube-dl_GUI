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
        """Changes audio/video additional switches"""

        if self.audio:
            self.SetAudio(value)
        else:
            self.SetVideo(value)
    def SetGlobal(self,value:str):
        self.TextEdit.setPlainText(value)
    def SetVideo(self,value:str):
        self.VideoTextEdit.setPlainText(value)
    def SetAudio(self,value:str):
        self.AudioTextEdit.setPlainText(value)

    def Get(self) -> str:
        """Returns global + audio/video additional switches"""
        
        resp = self.GetGlobal()+" "

        if self.audio:
            resp += self.GetAudio()
        else:
            resp += self.GetVideo()
        
        return resp
    def GetGlobal(self) -> str:
        return self.TextEdit.toPlainText()
    def GetVideo(self) -> str:
        return self.VideoTextEdit.toPlainText()
    def GetAudio(self) -> str:
        return self.AudioTextEdit.toPlainText()