from posixpath import split
import sys,os
import subprocess as sp
from PyQt5 import QtCore
from pathlib import Path


class Downloader(QtCore.QThread):
    downloaderPath = ""
    downloaderApp = "youtube-dl.exe"
    progress = 0
    progressbar = None
    console_callback=None
    process_ended_callback=None

    data_ready=QtCore.pyqtSignal(object)
    data_complete=QtCore.pyqtSignal(object)

    exitcode=-1

    isdownloading=False
    
    _isworking=False

    def __init__(self,ytdlPath="./",console_callback=None,process_ended_callback=None):
        self.downloaderPath = ytdlPath
        self.console_callback=console_callback
        self.process_ended_callback=process_ended_callback
        self.stdout = None
        self.stderr = None
        QtCore.QThread.__init__(self)
        self.data_ready.connect(self.Notify)
        self.data_complete.connect(self.EndWork)
    

    def _CutToExtension(self,pathText):
        cut1 = pathText.split("/")
        cut2 = cut1[len(cut1)-1].split(".")
        return cut2[len(cut2)-1]

    def _GetOutput(self,outName,audioOnly=False,template="(%(title)s)"):
        tmp = "" if not audioOnly else "(tmp)"
        dot=outName.rfind(".")
        name=outName[:dot]+template+outName[dot:]

        return f'--output \"{name}{tmp}\"'
    
    def _GetCommand(self,params):
        downloader = f"{self.downloaderPath}{self.downloaderApp}"
        options = ""
        tmp = ""

        if params["AUDIO_ONLY"]:
            options = f"--audio-format {self._CutToExtension(params['OUTPUT'])} --extract-audio "
            tmp = "(tmp)"
        else:
            options = f"--format {self._CutToExtension(params['OUTPUT'])} "
        
        output = self._GetOutput(
            params["OUTPUT"],
            audioOnly=params["AUDIO_ONLY"],
            template=params["TEMPLATE"]
        )

        if len(params["RANGE"]):
            options += f"--playlist-items {params['RANGE']} "
        
        #if params["PLAYLIST"]:

        command = f'{downloader} \"{params["URL"]}\" {options}{output}'
        print(command)
        return command

    def Notify(self,text):
        if self.console_callback:
            self.console_callback(text)

    def IsDownloading(self):
        return self.isdownloading        
    
    def EndWork(self,error):
       
        if self.process_ended_callback:
            self.process_ended_callback(error)
            self.isdownloading=False

    def StartDownload(self,params):
        ##print(params)

        self.command = self._GetCommand(params)
        ##print(self.command)

        self.isdownloading=True
        self.start()
        

    
    def run(self):
        self._isworking=True
        self.data_ready.emit("Start Download ...")
        self.process = sp.Popen(self.command, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
        # Poll process for new output until finished
        line=b''
        while self._isworking:
            c=self.process.stdout.read(1)
            ##print (c,end='')
            if c==b'\r': c=b'\n'
            line+=c

            if c==b'\n':
                if len(line): self.data_ready.emit(str(line[:-1],"latin-1"))
                else: break
                line=b''
            if c==b'': break


        self.process.wait()
        self._isworking=False
        self.exitcode = self.process.returncode
        self.data_complete.emit(self.exitcode)
        #self.join()
        return 

    def CancelDownload(self):
        if not self._isworking:
            return
        self._isworking=False
        self.data_ready.emit("Cancel download!!!")
        self.process.terminate()


    
    