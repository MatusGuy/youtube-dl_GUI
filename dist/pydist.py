import sys,os
import ctypes as cty
from win32api import GetFileVersionInfo, LOWORD, HIWORD

class PyDist():

    def __init__(self):
        self._ExecDir=sys.argv[0][:sys.argv[0].rfind('\\')+1]
        self._isBundle=getattr(sys, 'frozen', False)
        self._isSupDllLoaded=False
        self._pydist_dll=None

        #print (#self._ExecDir)
        #print (self._isBundle)

        if self._isBundle:
            # we are running in a bundle
            self._WorkDir = sys._MEIPASS+"\\"
        else:
            # we are running in a normal Python environment
            self._WorkDir= os.getcwd()+"\\"

        #print (self._WorkDir)
        

        dllname = 'pydist.dll'
        self.dllpaths = [self._ExecDir+dllname, self._WorkDir+'dist\\'+dllname, self._WorkDir+dllname]

        if self._isBundle:
            self.remove_if_old(self.dllpaths[0],self.dllpaths[1])
            self.remove_if_old(self.dllpaths[0],self.dllpaths[2])
            self.PrepareDist()

        #print (self._isSupDllLoaded)
            
        #print (F"Bundle: {self._isBundle}")
        #print (f"---> Working dir[{self._WorkDir}] vvvvvvvvvv ")
        #print (f"---> Executable dir[{self._ExecDir}] ^^^^^^^^^^ ")

    def PrepareDist(self):
        self._isSupDllLoaded=self._LoadSupportDll(self.dllpaths)
        
        if self._isSupDllLoaded:
            self.PrepareDllFuncs(self._pydist_dll)

    def _LoadSupportDll(self,dllpaths):
        load_success=False
        for dllname in dllpaths:
            #print (f"DLL Name: [{dllname}]")
            os.add_dll_directory(self._WorkDir)
            try:
                self._pydist_dll = cty.WinDLL(dllname)
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                #print(f"Unable to find the dll. [{template.format(type(ex).__name__, ex.args)}]")
                continue
            else:
                #print(f"DLL Handle: [{self._pydist_dll}][{dllname}]")
                load_success=True
                break

        return load_success
    
    def PrepareDllFuncs(self, pydist_dll):
        if not pydist_dll:
            return
        try:
            dll_about_proto = cty.WINFUNCTYPE(cty.c_int)
            dll_about_params = None
            self.dll_about = dll_about_proto(("About", pydist_dll), dll_about_params)

            dll_GetAppVersion_proto = cty.WINFUNCTYPE(cty.c_char_p)
            dll_GetAppVersion_params = None
            self.dll_GetAppVersion = dll_GetAppVersion_proto(("GetAppVersion", pydist_dll), dll_GetAppVersion_params)

            dll_GetExecutable_proto = cty.WINFUNCTYPE(cty.c_char_p)
            dll_GetExecutable_params = None
            self.dll_GetExecutable = dll_GetExecutable_proto(("GetExecutable", pydist_dll), dll_GetExecutable_params)
        except Exception:
            pass

    @staticmethod
    def get_version_number(filename):
        try:
            info = GetFileVersionInfo (filename, "\\")
            ms = info['FileVersionMS']
            ls = info['FileVersionLS']
            return [HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)]
        except:
            return [0,0,0,0]

    @staticmethod
    def version_compare(ver1,ver2):
        ver1=(ver1+[0,0,0,0])[:4]
        ver2=(ver2+[0,0,0,0])[:4]
        for v1,v2 in zip(ver1,ver2):
            if v1>v2:
                return 1
            if v1<v2:
                return -1
        return 0
    
    @staticmethod
    def remove_file(filename):
        try:
            os.remove(filename)
            return True
        except Exception:
            return False

    def remove_if_old(self, filename, comparefile):
        filever=self.get_version_number(filename)
        if self.version_compare(filever,[0,0,0,0])==0:
            return False
        compver=self.get_version_number(comparefile)
        if self.version_compare(filever,compver)>=0:
            return False
        return self.remove_file(filename)
        

    def About(self):
        if not self._isSupDllLoaded:
            return
        self.dll_about()
        return
    
    def GetAppVersion(self):
        if not self._isSupDllLoaded:
            return None
        resp=str(self.dll_GetAppVersion().decode('ascii'))
        return resp
    
    def GetExecutable(self):
        if not self._isSupDllLoaded:
            return None
        resp=str(self.dll_GetExecutable().decode('ascii'))
        return resp
try:
    __PyDist__=PyDist()
except:
    __PyDist__=None