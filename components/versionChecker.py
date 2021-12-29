import os

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *

from dist import pydist as pd

class VersionChecker():
    timer = QtCore.QTimer()
    interval = 0

    window = None
    downloader = None

    notifyCallback = None

    _debug=False

    def __init__(self,notifyCallback,interval=60000):
        self.interval = interval

        self.notifyCallback = notifyCallback
        self._SetFileToCheck()
    
    def StartChecking(self):
        self.timer.timeout.connect(self.Check)
        self.timer.start(self.interval)
    
    def StopChecking(self):
        self.timer.stop()

    def GetAppVersion(self):
        return pd.__PyDist__.GetAppVersion()
    
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
    
    def ConvLst2Str(self,version:list,addzeros=False):
        resp=""
        cnt=0
        for v in version:
            resp+=f"{v}."
            cnt+=1
        if addzeros and cnt<=4: resp+="0."*(4-cnt)
        return resp[:-1]
    
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
        
        self.NewVer =pd.__PyDist__.get_version_number(NewApp)
        self.OldVer =pd.__PyDist__.get_version_number(OldApp)
        if self._debug: print(f"Old App:{OldApp} v:{self.OldVer}\nNew App:{NewApp} v:{self.NewVer}\n")

        #Check for a bigger version
        verCompare=pd.__PyDist__.version_compare(self.NewVer,self.OldVer)
        if verCompare==0:
            if self._debug: print (f"Same Version. No action needed.")
            return
        elif verCompare<0:
            if self._debug: print (f"Error: OldVersion is newer than newer version!!!!")
            return

        if self._debug: print (f"New Version Detected. Notify now...")

        #TODO: Notify 
        if self.notifyCallback: self.notifyCallback(self.ConvLst2Str(self.NewVer),self.ConvLst2Str(self.OldVer))


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