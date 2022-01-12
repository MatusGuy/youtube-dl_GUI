import sys,os

sys.path.insert(1,'.')

from interface.mainUi import Ui_MainWindow as ui

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QAbstractButton
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QColor
from PyQt5.QtCore import Qt

from dist import pydist as pd

from interface.aboutWindow import AboutDialog as aw
from interface.addswitchesDialog import AdditionalSwitchesDialog as ad

class MainWindow(ui):
    window = QMainWindow
    app = QApplication

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

    aboutDialog = aw
    addSwitchesDialog = ad

    def __init__(self,window:QMainWindow,app:QApplication):
        self.window = window
        self.app = app
        self.app.setStyle("Fusion")

        super().setupUi(window)
        self.SetupIcons()

        self.aboutDialog = aw()
        self.addSwitchesDialog = ad(windowicon=pd.__PyDist__._WorkDir+"assets/ytdl.png")

        self.LightOption.triggered.connect(self.ToLightTheme)
        self.DarkOption.triggered.connect(self.ToDarkTheme)

        self.About.triggered.connect(self.aboutDialog.Execute)
        self.AdditionalSwitches.triggered.connect(self.addSwitchesDialog.Execute)
    
    def SetupIcons(self):
        self.window.setWindowIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/ytdl.png")))

        self.Theme.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/kcoloredit.png")))
        self.AdditionalSwitches.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/edit_add.png")))

        self.ConsoleOption.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/terminal.png")))

        #self.CommandHelpMenu.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/question.png")))
        self.Support.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/flag.png")))
        self.About.setIcon(QIcon(QPixmap(pd.__PyDist__._WorkDir+"assets/info.png")))

        self.DownloadButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/forward.png"))

        self.DestinationButton.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/folder_yellow.png"))

        #print(pd.__PyDist__._WorkDir)
    
    def SaveTheme(self,dark,prefMng=None):
        self.DarkOption.setChecked(dark)
        self.LightOption.setChecked(not dark)
        self.isDarkTheme = self.DarkOption.isChecked()

        if prefMng: prefMng.SetSetting(["isDarkTheme"],dark)
    
    def ToLightTheme(self):
        self.app.setPalette(QPalette())
        self.window.setPalette(QPalette())
        self.SaveTheme(False)
    
    def ToDarkTheme(self):
        self.app.setPalette(self.darkTheme)
        self.window.setPalette(self.darkTheme)
        self.SaveTheme(True)
    
    def DownloadEndDialog(self,errorcode:int,error:str=""):
        msg = QMessageBox()
        msg.setWindowIcon(QIcon(pd.__PyDist__._WorkDir+'assets/ytdl.png'))
        msg.setWindowTitle("youtube-dl GUI")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)

        if errorcode!=0 and error != "":
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Finished downloading unsuccessfully!")
            msg.setInformativeText(str(error))
        elif errorcode!=0:
            msg.setIcon(QMessageBox.Information)
            msg.setText("Canceled by user!")
        else:
            msg.setText("Finished downloading successfully!")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Open | QMessageBox.StandardButton.Ok)
        
        def OpenDownloaded(button:QAbstractButton):
            if button.text() == "Open":
                output = self.DestinationInput.text()
                rfind1 = output.rfind('\\')
                rfind2 = output.rfind('/')
                if rfind1 > rfind2:
                    result = output[:rfind1+1]
                else:
                    result = output[:rfind2+1]
                wresult=result.replace('/','\\')
                #print (wresult)
                if len(wresult): os.system("explorer "+wresult)

        msg.buttonClicked.connect(OpenDownloaded)
        
        msg.exec_()