import sys
sys.path.insert(1,".")

import tools.Album2Folder as AF

class AF_CompTest(object):
    def main(self):
        print("Album2Folder component test: start")
        
        self.af = AF.Album2Folder()
        testFile = "test\\test5.ogg"
        print(f"album for '{testFile}': {self.af.GetAlbum(testFile)} ({self.af.GetAlbum(testFile).__class__})")

        testDir = "test\\"
        print(f"list of files for '{testDir}': {self.af.GetFilesFromDir(testDir)}")

        print("moment of truth")
        #self.af.Album2Folder(testDir)
        print("did it work?")

        print("Album2Folder component test: complete")

if __name__ == "__main__":
    theApp= AF_CompTest()
    sys.exit(theApp.main())