import sys
sys.path.insert(1,'.')

from PyQt5 import QtWidgets

import addswitchesDialog as ad

class AW_CompTest(object):
    dialog = ad.AdditionalSwitchesDialog

    def main(self):
        print("About window component test: start")
        
        self.dialog = ad.AdditionalSwitchesDialog()

        print(f"About window component test: complete ({str(self.dialog.Execute())})")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    
    theApp= AW_CompTest()
    sys.exit(theApp.main())