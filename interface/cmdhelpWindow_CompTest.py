import sys
sys.path.insert(1,'.')
from cmdhelpWindow import CmdHelpDialog
from PyQt5 import QtWidgets

from dist import pydist as pd

class AW_CompTest(object):
    dialog = CmdHelpDialog

    def main(self):
        print("About window component test: start")
        
        self.dialog = CmdHelpDialog()
        
        cmd = f'{pd.__PyDist__._WorkDir}youtube-dl\\ffmpeg.exe --help'
        print("cmd: "+cmd)
        self.dialog.GetHelp(cmd)

        print(f"About window component test: complete")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    
    theApp= AW_CompTest()
    sys.exit(theApp.main())