import sys

from PyQt5 import QtWidgets

import aboutWindow as aw

class AW_CompTest(object):
    dialog = aw.AboutDialog

    def main(self):
        print("About window component test: start")
        
        self.dialog = aw.AboutDialog()
        self.dialog.Execute()

        print("About window component test: complete")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    
    theApp= AW_CompTest()
    sys.exit(theApp.main())