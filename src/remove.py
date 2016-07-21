from utils import getRootDir, text
import os
import shutil
import sys

def removeDir(path):
    print text.removingEnv
    shutil.rmtree(path)

def checkIfExists(path):
    return os.path.exists(path)

def remove():
    rootDir = getRootDir.getRoot() + "/.shiply"
    if len(sys.argv) < 3:
        sys.exit(text.removeHelper)
    name = sys.argv[2]
    if not checkIfExists(rootDir + "/" + name):
        sys.exit(text.envDoesntExist)
    removeDir(rootDir + "/" + name)
    print text.removed
