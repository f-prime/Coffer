import os
from utils import getRootDir, text, getArg
import sys
import re
import string
import shutil

def createDir(path):
    print text.createDir
    if not os.path.exists(path):
        os.mkdir(path)
        return True
    return False

def copyBaseFiles(path):
    print text.copyingFiles
    for directory in ["/bin", "/lib", "/lib64"]:
        shutil.copytree(directory, path + directory, symlinks=True)
        
def create():
    root = getRootDir.getRoot() + "/.shiply"
    template = getArg.getArg("-t")
    if len(sys.argv) < 3:
        sys.exit(text.createHelper)
    name = sys.argv[2]
    path = root + "/" + name
    if not createDir(path):
        sys.exit(text.envAlreadyExists)
    copyBaseFiles(path)
    if template:
        print template
    print text.envCreated

