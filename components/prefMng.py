import json,sys,os
sys.path.insert(1,'.')

from dist import pydist as pd

class PreferencesManager(object):

    settings=None
    default_data={  "version": "1.2.0",
                    "isDarkTheme": False,
                    "savedConfig": {
                        "url": "https://www.youtube.com/watch?v=jNQXAC9IVRw",
                        "audioOnly": False,
                        "template": "%(title)s",
                        "range": "",
                        "destination": ".mp4"
                    },
                    "additionalSwitches": ""
                }

    filename=None
    isPendingChanges=False

    ErrorNum=0
    ErrorMsg=""

    def __init__(self,filename):
        self.filename=filename
        self.UpgradeSettings()

    def _setError(self,code,msg):
        self.ErrorNum=code
        self.ErrorMsg=msg

    def _MergeSettings(self,new,curr):
        data={}
        for nk in new:
            if nk in curr:
                if type(new[nk])==type(curr[nk]):
                    if type(new[nk])==dict:
                        data[nk]=self._MergeSettings(new[nk],curr[nk])
                    else:
                        data[nk]=curr[nk]
            else:
                data[nk]=new[nk]
        return data
        
        
    def UpgradeSettings(self):
        defdata=self.default_data
        data=self.ReadJSON(self.filename,False)
        if data==None:
            self.settings=self.default_data 
            self._setError(2,"No setting file found. No settings re-use needed.")
            return

        if "version" in data and defdata["version"]==data["version"]:
            self.settings=data  
            self._setError(0,"No Setting upgrade needed.")
            return

        newdata=self._MergeSettings(defdata,data)
        newdata["version"]=defdata["version"]

        self.WriteJSON(self.filename,newdata)
        self.settings=newdata
        return newdata


    def ReadJSON(self,filename=None,useDefault=True):
        if filename==None: filename=self.filename
        try:
            with open(self.filename) as outfile:
                try:
                    self.settings=json.load(outfile)
                    self._setError(0,"Load OK")
                except Exception as ex:
                    self._setError(1,f"Unable to load json. {ex}")
                    print(ex)
                    if useDefault: self.settings=self.default_data
                    else: self.settings=None
                outfile.close()
        except Exception as ex:
            if useDefault: self.settings=self.default_data
            else: self.settings=None

            self._setError(1,f"Fail to load setting! Default data ({ex})")
        return self.settings

    def WriteJSON(self,filename,data):
        try:
            with open(filename, "w") as outfile:
                json.dump(data,outfile,indent=4,default=str)
                outfile.close()
                self.isPendingChanges=False
        except Exception as ex:
            pass

    def SetSetting(self,settingList:list,value,data={}):
        resp=False
        if len(data)==0: data=self.settings
        for setting in settingList:
            if setting in data:
                if settingList[-1:][0]==setting:
                    if data[setting]==value: 
                        resp=False
                    else:
                        data[setting]=value
                        resp=True
                else:
                    resp=self.SetSetting(settingList[1:],value,data=data[setting])
            else:
                resp=False
        self.isPendingChanges=self.isPendingChanges or resp
        return resp


        
    