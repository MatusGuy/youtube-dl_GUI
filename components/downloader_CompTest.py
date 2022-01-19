import sys,os
sys.path.insert(1,'.')

from PyQt5.QtWidgets import (QApplication,QMainWindow)

from components import downloader as dl

class Dl_CompTest(object):

    downloader = dl.Downloader()

    def __init__(self):
        #super().__init__()
        self.downloader = dl.Downloader(".\\youtube-dl\\",self.ConsoleAddLine,self.Downloaded_Ended, self.Download_Progress)

    def ConsoleAddLine(self,text):
        print (f"Logger New Line:\t{text}")

    def Downloaded_Ended(self,error):
        print (f"Ended. Error code:\t{error}")
        self.appwindow.close()

    def Download_Progress(self,updatecode,info):
        #print (f"Progress Update Code:\t0b{updatecode:05b} - {info}")
        #print (f"Progress Update Code:\t0b{updatecode:05b}")
        if updatecode&self.downloader.DW_PROCESS:
            print (info["CURR"]["PROCESS"],end=' -> ')
            print ("downloaded: "+str(info["DOWNLOADED_FILES"]))
        #...
        

    def main(self,app):
        print ("Downloader Component Test Begin")
        self.appwindow = QMainWindow()

        print ("Preparing Config")
        Config={
            "URL":"https://www.youtube.com/watch?v=jNQXAC9IVRw",
            "AUDIO_ONLY":True,
            "OUTPUT":"testdw.mp3",
            "TEMPLATE":"",
            "RANGE":"1-1",
            "EXTRA":"--add-metadata",
        }
        print (Config)
        print (f"Start Downloading...")

        self.downloader.StartDownload(Config)

        resp=app.exec_()

        print (f"Donwload done!")  

        print ("Downloader Component Test End")
        #os.system("del .\\testdw.mp3")
        return (resp)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    theApp= Dl_CompTest()
    sys.exit(theApp.main(app))