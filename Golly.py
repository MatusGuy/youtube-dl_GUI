from sys import argv as args, exit
from PyQt5.QtWidgets import QMessageBox, QApplication, QAbstractButton

class joke(object):
    def main(self,app:QApplication):
        print("Main window component test: start")

        msg = QMessageBox(
            QMessageBox.Icon.Warning,
            "Careful! (hopefully)",
            """Welcome to the wonderful youtube-dl GUI (((((((me))))))).
If you're smart, you would've put me in a specific folder.
If you aren't smart, good luck finding the settings.json file I hid in the middle of your downloads folder if you wanted to reposition me to another folder...
Sos man."""
        )

        msg.addButton("Gosh golly!", QMessageBox.ButtonRole.YesRole)
        msg.addButton("Phew.", QMessageBox.ButtonRole.YesRole)

        msg.show()

        app.exec_()

        print("Main window component test: complete")

if __name__ == "__main__":
    app = QApplication(args)
    
    theApp= joke()
    exit(theApp.main(app))