import sys,os
import subprocess as sp
from PyQt5.QtCore import pyqtSignal, QThread
from pathlib import Path


class Downloader(QThread):
    downloaderPath = ""
    downloaderApp = "youtube-dl.exe"
    progress = 0
    progressbar = None

    console_callback=None
    progress_callback=None
    process_ended_callback=None

    data_ready=pyqtSignal(object)
    data_complete=pyqtSignal(object)

    download_info_default={
                    "IS_DOWNLOADING":False,
                    "TOTAL_FILES":1,
                    "CURR":{
                        "FILE_NAME":"",
                        "FILE_NUM":1,
                        "PROGRESS":0,
                        "ETA":"",
                        "FILE_SIZE":"",
                        "SPEED":"",
                        "PROCESS":""
                    },
                    "ERROR":""
                }

    download_info={}

    downloaded_files=[]

    DW_PROCESS  =1<<0 # 1     2^0 = 1
    DW_TOTALS   =1<<1 # 2     2^1 = 2
    DW_PROGRESS =1<<2 # 4     2^2 = 2*2
    DW_FILENAME =1<<3 # 8     2^3 = 2*2*2
    DW_ERROR    =1<<4 # 16    2^4 = 2*2*2*2

    exitcode=-1

    isdownloading=False
    
    _isworking=False

    def __init__(self,ytdlPath="./",console_callback=None,process_ended_callback=None,progress_callback=None):
        self.downloaderPath = ytdlPath
        self.console_callback=console_callback
        self.process_ended_callback=process_ended_callback
        self.progress_callback=progress_callback
        self.stdout = None
        self.stderr = None
        QThread.__init__(self)
        self.data_ready.connect(self.Notify)
        self.data_complete.connect(self.EndWork)
        self.Reset()

    def Reset(self):
        self.download_info=self._copy(self.download_info_default)

    def _copy(self,org):
        if type(org)==dict: dest={key:self._copy(org[key]) for key in org}
        elif type(org)==list: dest=[self._copy(value) for value in org]
        else: dest=org
        return dest
    

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
        downloader = f'"{self.downloaderPath}{self.downloaderApp}"'
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

        if len(params["RANGE"]): options += f"--playlist-items {params['RANGE']} "
        if len(params["EXTRA"]): options += f"{params['EXTRA']} "
        
        #if params["PLAYLIST"]:

        command = f'{downloader} \"{params["URL"]}\" {options}{output}'
        print(command)
        return command

    def ProcessInfo(self,text:str|bytes):
        resp=0b00000
        text.removesuffix("                 ")
        uppered = text.upper()

        # Get the current process 
        if "[" in uppered:
            removeprefix1 = text.removeprefix("[")
            self.download_info["CURR"]["PROCESS"]=removeprefix1.split("] ")[0].capitalize()
            resp|=0b00001

        # Get Current download file and Total Files
        if "[DOWNLOAD] DOWNLOADING VIDEO" in uppered and "OF" in uppered:
            cut1 = text.split(" ")
            self.download_info["CURR"]["FILE_NUM"] = cut1[3]
            self.download_info["TOTAL_FILES"]=cut1[5]
            resp|=0b00010

        # Get The download progress
        if "[DOWNLOAD] " in uppered and "%" in uppered and "AT" in uppered:
            cut1 = text.split("] ")[1]
            cut2 = cut1.split("% ")
            result = cut2[0].replace(" ","0")

            totalFiles = int(self.download_info["TOTAL_FILES"])
            fileNum = int(self.download_info["CURR"]["FILE_NUM"])
            self.download_info["CURR"]["PROGRESS"] = int( (float(result) // totalFiles) + ((100 // totalFiles) * (fileNum-1)) )

            otherInfo = cut2[1].split(" ")
            self.download_info["CURR"]["FILE_SIZE"] = otherInfo[1]
            try: self.downloaded_files[-1]["SIZE"] = otherInfo[1]
            except: pass
            self.download_info["CURR"]["SPEED"] = otherInfo[3]
            self.download_info["CURR"]["ETA"]  = otherInfo[5]
            resp|=0b00100

        # Get total time
        if "[DOWNLOAD] " in uppered and not "DESTINATION: " in uppered and "IN " in uppered:
            cut1 = text.split("in ")
            try: self.downloaded_files[-1]["TOTAL_TIME"] = cut1[-1]
            except: pass

        # Get Current Download File Name
        if "[DOWNLOAD] DESTINATION: " in uppered:
            path = text.removeprefix("[download] Destination: ")
            cut1 = path.split("\\")
            self.download_info["CURR"]["FILE_NAME"]  = cut1[len(cut1)-1].removesuffix("(tmp)")
            self.downloaded_files.append({
                "FILENAME": self.download_info["CURR"]["FILE_NAME"],
                "SIZE": "",
                "TOTAL_TIME": "",
                "DESTINATION": path.removesuffix("(tmp)")
            })
            resp|=0b01000

        # Get Possible Errors 
        if "ERROR: " in uppered:
            if "YOUTUBE-DL.EXE: " in uppered: self.download_info["ERROR"] = text.removeprefix("youtube-dl.EXE: error: ").capitalize()
            else: self.download_info["ERROR"] = text.removeprefix("ERROR: ").capitalize()
            resp|=0b10000

        return resp

    def Notify(self,text):
        if type(text)==bytes: text=text.decode("ASCII")

        updatecode=self.ProcessInfo(text)
        if updatecode and self.progress_callback:
            self.progress_callback(updatecode,self.download_info,self.downloaded_files)

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

        self.Reset()
        self.isdownloading=True
        self.start()
    
    def run(self):
        self._isworking=True
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
        self.process.terminate()