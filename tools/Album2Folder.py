from sys import path
path.insert(1,".")

import subprocess
from os import system as RunCmd,path as ospath, listdir,makedirs as mkdir

from mutagen import (
    File as MgFile,
    mp3,
    oggvorbis as ogg,
    wave as wav,
    flac
)

from PyQt5.QtCore import pyqtSignal as QSignal,QObject

class Album2Folder(QObject):
    _process = ""
    _error = ""

    currNum = 0
    totalFiles = []
    totalNum = 0
    progress = 0

    processChanged  = QSignal(str)
    progressChanged = QSignal(int)
    fileNumChanged  = QSignal(int,int)

    errored = QSignal(str)

    # Honestly, blame mutagen for the two below.
    SUPPORTED = (
        ".mp3",
        ".ogg",
        ".wav",
        ".flac"
    )

    SUPPORTED_KEYS = {
        mp3.MP3: "TALB",
        ogg.OggVorbis: "album",
        wav.WAVE: "TALB",
        flac.FLAC: "album",
    }
    
    def __init__(self): super().__init__()

    def ClearError(self): self._error = ""
    def SetError(self,error:str):
        self._error = error
        print("Album2Folder ERROR: "+self._error)
        self.errored.emit(self._error)

    def SetProcess(self,process:str):
        self._process = process
        print("Album2Folder INFO: " +self._process)
        self.processChanged.emit(self._process)
    
    def SetProgress(self,progress:int):
        self.progress = progress
        self.progressChanged.emit(self.progress)

    def AppendTotalFiles(self,value:str):
        self.totalFiles.append(value)
        self.totalNum = len(self.totalFiles)
        self.fileNumChanged.emit(self.totalNum,self.currNum)

    def SetTotalFiles(self,value:list[str]):
        self.totalFiles = value
        self.totalNum = len(self.totalFiles)
        self.fileNumChanged.emit(self.totalNum,self.currNum)

    def ResetTotalFiles(self):
        self.totalFiles = []
        self.totalNum = 0
        self.currNum = 0
        self.fileNumChanged.emit(self.totalNum,self.currNum)
    
    def SetCurrNumFiles(self,value:int):
        self.currNum = value
        self.fileNumChanged.emit(self.totalNum,self.currNum)

    def GetAlbum(self,filepath:str) -> str:
        self.SetProcess("Fetching for album in: "+filepath)
        file = MgFile(filepath)

        try:
            return str(file[self.SUPPORTED_KEYS[file.__class__]][0])
        except KeyError:
            self.SetError("Unsupported audio file format.")
            return

    def GetFilesFromDir(self,_dir:str) -> list[str]:
        self.SetProcess(f'Getting all files in directory: "{_dir}"')
        if not _dir.endswith("\\") and _dir: _dir+="\\"
        try:
            onlyfiles = [f for f in listdir(_dir) if ospath.isfile(ospath.join(_dir, f))]
            for file in onlyfiles: onlyfiles[onlyfiles.index(file)] = _dir+file
        except FileNotFoundError:
            self.SetError("Invalid path.")
        else:
            return onlyfiles

    @staticmethod
    def GetCmdResponse(cmd) -> str:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags|=subprocess.STARTF_USESHOWWINDOW
        process = subprocess.Popen(cmd,
            startupinfo=startupinfo,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE
        )
        data = process.stdout.read()
        process.stdout.close()
        return data.decode("utf-8")
    
    def Album2Folder(self,_dir:str,clearMessages:bool=True):
        dirFiles = self.GetFilesFromDir(_dir)
        if not dirFiles: return
        self.SetProcess("Applying only supported audio file filter to the operation.")
        for file in dirFiles:
            if file.endswith(self.SUPPORTED): self.AppendTotalFiles(file)

        if self.totalNum==0:
            self.SetError("Already organized.")
            return

        for filename in self.totalFiles: # for each audio file in the folder
            self.SetCurrNumFiles(self.totalFiles.index(filename)+1)
            self.SetProcess(f"Moving on to #{self.currNum+1}")

            album = self.GetAlbum(filename)
            if album:
                if not _dir.endswith("\\"): _dir+="\\"

                if not ospath.exists(_dir+album): # if the album folder doesn't exist already
                    self.SetProcess("Making the album folder: "+_dir+album+"\\")
                    mkdir(_dir+album) # make the album folder
                    
                self.SetProcess(f"Moving {filename} to album folder: "+_dir+album+"\\")
                RunCmd(f'move "{filename}" "{_dir+album}\\">NUL') # move the file to the album folder
            else:
                self.SetProcess(f"Skipping file #{self.currNum+1} ({filename}) because it's not a supported audio file.")

            self.SetProgress(int((self.currNum+1/self.totalNum)*100))
        
        if clearMessages:
            self.ClearError()
            self.SetProgress(0)
            self.ResetTotalFiles()
            self.SetProcess("")