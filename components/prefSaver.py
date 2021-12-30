import json,sys,os
sys.path.insert(1,'.')



class PreferencesSaver(object):

    data=None

    def __init__(self,filename):
        self.filename=filename

    def ReadJSON(self):
        with open(self.filename) as outfile:
            try:
                self.data=json.load(outfile)
            except ValueError as e:
                raise Exception('Invalid json: {}'.format(e)) from None
            outfile.close()
        return self.data

    def WriteJSON(self,filename,data):
        with open(filename, "w") as outfile:
            json.dump(data,outfile,indent=4,default=str)
            outfile.close()