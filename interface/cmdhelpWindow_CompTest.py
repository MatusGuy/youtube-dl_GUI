import sys
sys.path.insert(1,'.')

from cmdhelpWindow import CmdHelpDialog
from PyQt5 import QtWidgets,QtCore

from dist import pydist as pd

class CH_CompTest(QtCore.QObject):
    dialog = CmdHelpDialog

    def __init__(self) -> None:
        super().__init__()

    def main(self):
        print("About window component test: start")
        
        self.dialog = CmdHelpDialog()
        
        cmd = f'{pd.__PyDist__._WorkDir}youtube-dl\\ffmpeg.exe --help'
        print("cmd: "+cmd)
        self.dialog.installEventFilter(self)
        self.dialog.GetHelp(cmd)
    
    def eventFilter(self, obj:QtCore.QObject, event:QtCore.QEvent):
        if obj is self.dialog and event.type() == QtCore.QEvent.Type.Close: print(f"About window component test: complete")
        return super().eventFilter(obj, event)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
        
    theApp= CH_CompTest()
    sys.exit(theApp.main())