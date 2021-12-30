import json,sys,os
sys.path.insert(1,'.')

from components import prefSaver as ps

def main():
    print ("Component Test Begin")

    prefs= ps.PreferencesSaver(".\\settings.json")
    

    print ("Component Test End")

if __name__ == "__main__":
    main()