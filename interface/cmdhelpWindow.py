import sys,subprocess

sys.path.insert(1,'.')

from PyQt5.QtGui import QIcon
from interface.cmdHelpUi import Ui_Cmd as ui
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt

from dist import pydist as pd

class CmdHelpDialog(ui,QDialog):
    def __init__(self,windowTitle:str="youtube-dl command line help") -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(windowTitle)
        self.setWindowIcon(QIcon(pd.__PyDist__._WorkDir+"assets/ytdl.png"))
        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)
        #self.setModal(False)

    def GetHelp(self,cmd):
        self.Text.setPlainText(self.ExecCmd(cmd))
        self.exec_()

    @staticmethod
    def ExecCmd(cmd) -> str:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags|=subprocess.STARTF_USESHOWWINDOW
        process = subprocess.Popen(cmd,
            startupinfo=startupinfo,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE
        )
        data = process.stdout.read()
        process.stdout.close()
        return data.decode("utf-8")