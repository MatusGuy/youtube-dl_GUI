import sys,ctypes
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QObject,QEvent
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QMenu,QAction
from dist import pydist as pd
IS_BUNDLE = pd.__PyDist__._isBundle
import py_mysplash as psh
from ctypes import WinDLL
dll = WinDLL(pd.__PyDist__._WorkDir+"dist\\Microsoft.WindowsAPICodePack.Shell.dll")
print(dll._name)

from components import downloader as dl, versionChecker as vc, prefMng as pm

from interface import mainWindow as mw

#from settingsGuis.themePrompt_class import Ui_ChangeTheme as ThemesGui

currSjson = pd.__PyDist__._ExecDir+"settings.json"
newSjson = pd.__PyDist__._WorkDir+"settings.json"

class Program(mw.MainWindow,QObject):
    window = QMainWindow
    app = QApplication

    downloader = dl.Downloader
    versionChecker = vc.VersionChecker
    prefMng = pm.PreferencesManager

    showConsole = False

    videos=0

    console_height=89

    error = ""

    ignoredNewVersion = False

    def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
        if a0 is self.window:
            if a1.type() is QEvent.Type.Show: self.taskbarProgress.setVisible(True)
        return super().eventFilter(a0, a1)

    def InitTestMenus(self):
        testsMenu = QMenu("Tests/Debug",self.MenuBar)
        self.MenuBar.addMenu(testsMenu)

        versionCheckTrigger = QAction("Version alert dialog",testsMenu)
        versionCheckTrigger.triggered.connect(self.AlertVersion)
        testsMenu.addAction(versionCheckTrigger)

        action= QAction(QIcon("assets/folder_yellow.png"),"normal action",self.UrlTextBox)
        self.DownloadProgress.addAction(action)
        testsMenu.addAction(action)

    def setupUi(self, MainWindow:QMainWindow, app:QApplication):
        self.app = app
        self.app.setStyle("Fusion")

        self.window = MainWindow
        self.window.installEventFilter(self)

        self.prefMng = pm.PreferencesManager(currSjson)
        resp=super().__init__(
            window=self.window,
            app=self.app,
            version=pd.__PyDist__.GetAppVersion(),
            prefMng=self.prefMng
        )
        if not IS_BUNDLE: self.InitTestMenus()

        #self.Downloader = dl.Downloader(".\\youtube-dl\\")

        self.downloader = dl.Downloader(pd.__PyDist__._WorkDir+"youtube-dl\\",self.AppendConsoleHtml,self.Downloaded_Ended,self.DistributeDWInfo)

        self.SetDownloadCallback(self.DownloadCallback)

        self.versionChecker = vc.VersionChecker(self.AlertVersion,60000)
        self.versionChecker.StartChecking()

        return resp
    
    def AlertVersion(self):
        resp = self.AlertVersionDialog()
        if resp: self.app.quit()
    
    def DownloadCallback(self):
        if self.downloader.IsDownloading():
            self.downloader.CancelDownload()
            self.AppendConsoleHtml('<body style="color:red;">Canceled download!</body>')
            self.DownloadButtonState()
            self.DisableDownloadGui(True)
            self.ShowStatusMessage("Canceled download")
        else:
            self.ClearConsole()
            self.CancelButtonState()
            self.AppendConsoleHtml('<body style="color:aqua;">Starting download...</body>')
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

    def DistributeDWInfo(self,updatecode,info:dict,dwList:dict):
        self.ShowStatusMessage("Processing: "+info["CURR"]["PROCESS"])
        self.SetDownloadInfo(
            eta=info["CURR"]["ETA"],
            speed=info["CURR"]["SPEED"],
            size=info["CURR"]["FILE_SIZE"],
            progress=info["CURR"]["PROGRESS"],
            current=info["CURR"]["FILE_NAME"],
            files=f'{info["CURR"]["FILE_NUM"]}/{info["TOTAL_FILES"]}'
        )
        self.ListToDwList(dwList)

    def Downloaded_Ended(self,errorcode):
        self.ShowStatusMessage("Download ended",200000)
        self.AppendConsoleHtml('<body style="color:aqua;">Download process ended</body>')
        self.DownloadEndDialog(errorcode,self.downloader.download_info["ERROR"])
        self.DownloadButtonState()
        self.DisableDownloadGui(True)

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
    psh.Splash_loadcomplete(750)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

    window()