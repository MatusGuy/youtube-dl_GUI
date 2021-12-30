import json,sys,os
sys.path.insert(1,'.')



class PreferencesManager(object):

    data=None
    default_data={  "version": "1.1.0",
                    "isDarkTheme": False,
                    "savedConfig": {
                        "url": "https://www.youtube.com/watch?v=jNQXAC9IVRw",
                        "audioOnly": False,
                        "template": "%(title)s",
                        "range": "",
                        "destination": ".mp4"
                    }
                }
    filename=None
    defaultfilename=None

    ErrorNum=0
    ErrorMsg=""

    def _setError(self,code,msg):
        self.ErrorNum=code
        self.ErrorMsg=msg

    def __init__(self,filename, defaultfile=None):
        self.filename=filename
        self.defaultfilename=defaultfile

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
            self._setError(2,"No setting file found. No settings re-use needed.")
            return

        if "version" in data and defdata["version"]==data["version"]: 
            self._setError(0,"No Setting upgrade needed.")
            return

        newdata=self._MergeSettings(defdata,data)
        newdata["version"]=defdata["version"]

        self.WriteJSON(self.filename,newdata)
        self.data=newdata
        return newdata


    def ReadJSON(self,filename=None,useDefault=True):
        if filename==None: filename=self.filename
        try:
            with open(self.filename) as outfile:
                try:
                    self.data=json.load(outfile)
                    self._setError(0,"Load OK")
                except ValueError as e:
                    raise Exception('Invalid json: {}'.format(e)) from None
                outfile.close()
        except Exception as ex:
            if useDefault: self.data=self.default_data
            else: self.data=None

            self._setError(1,f"Fail to load setting! Default data ({ex})")
        return self.data

    def WriteJSON(self,filename,data):
        with open(filename, "w") as outfile:
            json.dump(data,outfile,indent=4,default=str)
            outfile.close()
        
    