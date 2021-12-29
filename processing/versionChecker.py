import os

from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *

from dist import pydist as pd

from downloader import Downloader as dl
from main import window

class VersionChecker():
    timer = QtCore.QTimer()
    interval = 0

    window = None

    def __init__(self,window,interval=60000):
        self.window = window
        self.interval = interval
    
    def StartChecking(self):
        self.timer.timeout.connect(self.Check)
        self.timer.start(self.interval)
    
    def StopChecking(self):
        self.timer.stop()
    
    def Check(self):
        print ("Do the check")

    def Check1(self):
        #print("version check")

        exeapp=pd.__PyDist__.GetExecutable()
        bakapp=exeapp[:-4]+".bak" if exeapp != None else "dist/youtube-dl_GUI.bak"

        #print(bakapp)
        #print(os.path.exists(bakapp))

        if os.path.exists(bakapp) and not self.ignoredNewVersion:

            versionMsg = QMessageBox()
            versionMsg.setIcon(QMessageBox.Icon.Information)
            versionMsg.setWindowTitle("youtube-dl GUI")
            versionMsg.setText("There's a new version of youtube-dl GUI available.\nRestart the application to apply it.\n\nClose the application?")
            versionMsg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            versionMsg.setWindowIcon(QtGui.QIcon(pd.__PyDist__._WorkDir+'assets/ytdl.png'))
            versionMsg.setModal(True)

            def OpenConfirmation(button):
                #print(f"open confirmation\nsaid yes: {button.text() == 'Yes'}\nbutton text: {button.text()}")
                if button.text() == "&Yes":
                    if dl.IsDownloading():
                        confirmation = QMessageBox()
                        confirmation.setIcon(QMessageBox.Icon.Warning)
                        confirmation.setWindowTitle("youtube-dl GUI")
                        confirmation.setText("Are you sure you want to close the application?\nYou're in the middle of a download!")
                        confirmation.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                        confirmation.setWindowIcon(QtGui.QIcon(pd.__PyDist__._WorkDir+'assets/ytdl.png'))
                        confirmation.setModal(True)

                        def Buttons(confirmButton):
                            #print("buttons")
                            if confirmButton.text() == "&Yes":
                                self.window.close()
                            else:
                                confirmation.close()
                                versionMsg.close()

                        confirmation.buttonClicked.connect(Buttons)

                        confirmation.exec_()
                else:
                    self.timer.stop()
                    versionMsg.close()
            
            versionMsg.buttonClicked.connect(OpenConfirmation)

            versionMsg.exec_()