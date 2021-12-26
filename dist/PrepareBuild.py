
import sys
import os
import pydist as pd

def ReadVersionFile(filename):
    filelines=[]
    with open (filename) as hfile:
        for line in hfile:
            filelines.append(line)
    return filelines

def WriteVersionFile(filename, lines):
    hfile = open(filename, "w")
    if not hfile:
        return
    for line in lines:
        hfile.writelines(line)
    hfile.close()
    return

def UpdateLines(lines,version=[]):
    lines[2] = f"    filevers=({version[0]}, {version[1]}, {version[2]}, {version[3]}),\n"
    lines[18] = f"        StringStruct(u'FileVersion', u'{version[0]}.{version[1]}.{version[2]}.{version[3]} (Release)'),\n"
    
def UpdateResourcesFile(filename, version):
    print (f"Preparing the Build Version: {version[0]}.{version[1]}.{version[2]}.{version[3]}")
    lines=ReadVersionFile(filename)
    UpdateLines(lines,version)
    WriteVersionFile(filename,lines)

def UpdatedUpgradeFile(filename,version=[]):
    file = open(filename, 'r+')
    line=file.readline()
    params=line.split(" ")
    file.seek(0,0)
    line=f"{version[0]}.{version[1]}.{version[2]}.{version[3]} {params[1]}"
    file.writelines(line)
    print (f"Update UPG file:[{filename,}] -> {line}")
    file.close()

def GetRevisionNumber():
    svninfo=os.popen('svn info').read()
    svninfo=svninfo.split('\n')
    for line in svninfo:
        line=line.split(':')
        if line[0]=='Revision':
            return int(line[1])
    return 0

def BuildExecutable(python, app):
    pyinstaller=python[:python.rfind('\\')+1]+'scripts\\pyinstaller.exe'
    cmd='"'+pyinstaller+'" '+app
    print ("\nBuild App...\n")
    print ("Execute Command: ",cmd)
    os.system(cmd)
    print ("\nBuild App...Executed. >>> Please TEST before release!")


def main(argv):
    filename="dist\\Resources.rc"
    print ("\nRelease Script Tool - CM2019-2022\n")

    if (len(argv)<5):
        print ("Usage: Build.py <app_spec> <Version> <MajorFeat> <MinorFeat> <BugsFixs>")
        return

    program=argv[1][argv[1].rfind("\\")+1:argv[1].rfind(".")]
    print (f"Building [{program}.exe]")
    print (f"Update {filename} file")
    #Revision=GetRevisionNumber()
    #print ("SVN Revison:"+str(GetRevisionNumber()))
    #UpdateResourcesFile(filename, [argv[2],argv[3],argv[4],str(Revision+1)])
    UpdateResourcesFile(filename, [argv[2],argv[3],argv[4],argv[5]])
    UpdatedUpgradeFile(f".\\update\\{program}.upg",[argv[2],argv[3],argv[4],argv[5]])
    print (f"Done. Please verify the [{filename}] file.\n")

    build=input("Build the executable now? (y/N) ")
    if build=='y':
        pd.__PyDist__.PrepareDist()
        BuildExecutable(pd.__PyDist__.GetExecutable(), argv[1])
    else:
        print ("\nBuild later then....")

    print ("")

if __name__ == "__main__":
    main(sys.argv)



