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
    downloader = None

    _debug=False

    def __init__(self,window,downloader,interval=60000):
        self.window = window
        self.downloader = downloader
        self.interval = interval
        self._SetFileToCheck()
    
    def StartChecking(self):
        self.timer.timeout.connect(self.Check)
        self.timer.start(self.interval)
    
    def StopChecking(self):
        self.timer.stop()
    
    def _SetFileToCheck(self,exe=None, bak=None):
        if (exe==None):
            self.ExeApp=pd.__PyDist__.GetExecutable() if pd.__PyDist__.GetExecutable() else ""
        else:
           self.ExeApp=exe

        if bak==None:
            app=pd.__PyDist__.GetExecutable() if pd.__PyDist__.GetExecutable() != None else ".\\dist\\youtube-dl_GUI.bak"
            self.BakApp= app[:-4]+".bak"
        else:
            self.BakApp= bak

    def _GetFilesToCheck(self):
        return self.BakApp, self.ExeApp
    
    def Check(self):
        if self._debug: print("Time to check")
        
        #Get the file to compare
        OldApp, NewApp= self._GetFilesToCheck()
        if self._debug: print(f"Old APP:{OldApp}\nNew App:{NewApp}\n")

        #Check if they exist
        if not os.path.exists(OldApp):
            if self._debug: print (f"Error: OldApp: {OldApp} Not Exists!!")
            return
        if not os.path.exists(NewApp):
            if self._debug: print (f"Error: NewApp: {NewApp} Not Exists!!")
            return
        
        newver =pd.__PyDist__.get_version_number(NewApp)
        oldver =pd.__PyDist__.get_version_number(OldApp)
        if self._debug: print(f"Old APP:{OldApp} v:{oldver}\nNew App:{NewApp} v:{ newver}\n")


    def Check1(self):
        print("version check")

        exeapp=pd.__PyDist__.GetExecutable()
        bakapp=exeapp[:-4]+".bak" if exeapp != None else "dist/youtube-dl_GUI.bak"

        #print(bakapp)
        #print(os.path.exists(bakapp))

        if os.path.exists(bakapp):

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
                    if self.downloader.IsDownloading():
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
                        self.window.close()
                    
                else:
                    self.timer.stop()
                    versionMsg.close()
            
            versionMsg.buttonClicked.connect(OpenConfirmation)

            versionMsg.exec_()