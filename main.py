from copy import error
import sys,os,ctypes
from webbrowser import open_new_tab as OpenURL
from pathlib import Path
from PyQt5 import QtGui
from PyQt5.QtGui import QColor,QIcon,QPalette,QPixmap
from PyQt5.QtCore import Qt,QObject,QEvent
from PyQt5.QtWidgets import *
import interface.mainUi as MainUi
from dist import pydist as pd
import py_mysplash as psh

from components import downloader as dl, versionChecker as vc, prefMng as pm

from interface import (
    aboutWindow as aw,
    addswitchesDialog as ad,
    cmdhelpWindow as ch,
    mainWindow as mw
)

#from settingsGuis.themePrompt_class import Ui_ChangeTheme as ThemesGui

currSjson = pd.__PyDist__._ExecDir+"settings.json"
newSjson = pd.__PyDist__._WorkDir+"settings.json"

class Program(mw.MainWindow,QObject):
    window = QMainWindow
    app = QApplication

    downloader = dl.Downloader
    versionChecker = vc.VersionChecker
    prefMng = pm.PreferencesManager

    aboutWindow = aw.AboutDialog
    addswitchesDialog = ad.AdditionalSwitchesDialog

    showConsole = False

    videos=0

    console_height=89

    darkTheme = palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)

    isDarkTheme = False

    error = ""

    ignoredNewVersion = False

    def setupUi(self, MainWindow:QMainWindow, app:QApplication):
        self.app = app
        self.app.setStyle("Fusion")

        self.window = MainWindow

        self.prefMng = pm.PreferencesManager(currSjson)
        resp=super().__init__(
            window=self.window,
            app=self.app,
            version=pd.__PyDist__.GetAppVersion(),
            prefMng=self.prefMng
        )

        #self.Downloader = dl.Downloader(".\\youtube-dl\\")

        self.downloader = dl.Downloader(pd.__PyDist__._WorkDir+"youtube-dl\\",self.AppendConsole,self.Downloaded_Ended,self.DistributeDWInfo)

        self.SetDownloadCallback(self.DownloadCallback)

        self.versionChecker = vc.VersionChecker(self.AlertVersion,60000)
        self.versionChecker.StartChecking()

        return resp
    
    def AlertVersion(self):
        #print("version check")

        if self.downloader.IsDownloading(): return

        versionMsg = QMessageBox()
        versionMsg.setIcon(QMessageBox.Icon.Information)
        versionMsg.setWindowTitle("youtube-dl GUI")
        versionMsg.setText("There's a new version of youtube-dl GUI available.\nRestart the application to apply it.\n\nClose the application?")
        versionMsg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        versionMsg.setWindowIcon(QIcon(pd.__PyDist__._WorkDir+'assets/ytdl.png'))
        versionMsg.setModal(True)

        def OpenConfirmation(button:QAbstractButton):
            #print(f"open confirmation\nsaid yes: {button.text() == 'Yes'}\nbutton text: {button.text()}")
            if button.text() == "&Yes":
                self.window.close()
            else:
                self.versionChecker.StopChecking()
                versionMsg.close()
        
        versionMsg.buttonClicked.connect(OpenConfirmation)

        versionMsg.exec_()
    
    def DownloadCallback(self):
        if self.downloader.IsDownloading():
            self.downloader.CancelDownload()
            self.AppendConsole("Cancelled download!")
            self.DownloadButtonState()
            self.DisableDownloadGui(True)
            self.ShowStatusMessage("Cancelled download")
        else:
            self.ClearConsole()
            self.CancelButtonState()
            self.AppendConsole("Starting download...")
            self.ShowStatusMessage("Starting download")
            self.DisableDownloadGui(False)

            Config={
                "URL":self.GetURL(),
                "AUDIO_ONLY":self.GetAudioOnly(),
                "OUTPUT":self.GetOutput(),
                "TEMPLATE":self.GetTemplate(),
                "RANGE":self.GetRange(),
                "EXTRA":self.GetAdditionalSwitches(),
            }
            self.downloader.StartDownload(Config)

    def DistributeDWInfo(self,updatecode,info:dict):
        self.ShowStatusMessage("Processing: "+info["CURR"]["PROCESS"])
        self.SetDownloadInfo(
            eta=info["CURR"]["ETA"],
            speed=info["CURR"]["SPEED"],
            size=info["CURR"]["FILE_SIZE"],
            progress=info["CURR"]["PROGRESS"],
            current=info["CURR"]["FILE_NAME"],
            files=f'{info["CURR"]["FILE_NUM"]}/{info["TOTAL_FILES"]}'
        )
        self.error = info["ERROR"]

    def Downloaded_Ended(self,errorcode):
        self.ShowStatusMessage("Download ended",200000)
        self.AppendConsole("Download process ended")
        self.DownloadEndDialog(errorcode,self.error)
        self.DownloadButtonState()

def window():
    app = QApplication(sys.argv)

    window = QMainWindow()

    program = Program(
        window=window,
        app=app,
        version=pd.__PyDist__.GetAppVersion(),
        prefMng=pm.PreferencesManager(currSjson))
    program.setupUi(window,app)

    #QtCore.QTimer.singleShot(250, HideSplash)
    psh.Splash_loadcomplete(2000)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

    window()