import json,sys,os
sys.path.insert(1,'.')

from components import prefMng as pm

def main():
    print ("Component Test Begin")

    prefs= pm.PreferencesManager(".\\settings1.json")

    data= prefs.ReadJSON()
    print (f"Error Code:[{prefs.ErrorNum}]: {prefs.ErrorMsg}")
    print (data)

    datanew={  "version": "1.1.0",
                "isDarkTheme": False,
                "savedConfig": {
                    "url": "https://www.youtube.com/watch?v=jNQXAC9IVRw",
                    "audioOnly": False,
                    "template": "%(title)s",
                    "range": "1-20",
                    "destination": ".mp4"
                }
            }
    
    datacurr={"version": "1.0.0",
            "isDarkTheme": False,
            "savedConfig": {
                "url": "https://www.youtube.com/watch?v=jNQXAC9IVRw",
                "audioOnly": False,
                "destination": ".mp4"
            }
        }

    print ("\nMerge Test")
    print (prefs._MergeSettings(datanew,datacurr))


    print ("Component Test End")

if __name__ == "__main__":
    main()