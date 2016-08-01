from coffer.utils import getRootDir, text, isRoot, getArg
import os
import shutil
import sys

def removeDir(path):
    print (text.removingEnv)
    shutil.rmtree(path)

def checkIfExists(path):
    return os.path.exists(path)

def remove():
    rootDir = getRootDir.getEnvsDir()

    name = getArg.getArg(0)

    if not name:
        sys.exit(text.removeHelper)
    if not isRoot.isRoot():
        sys.exit(text.notRoot)
    if not checkIfExists(rootDir + name):
        sys.exit(text.envDoesntExist)
    
    removeDir(rootDir + name)
    print (text.removed)
