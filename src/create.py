import os
from utils import getRootDir, text, getArg
import sys
import re
import string
import shutil

def createDir(name, root):
    print text.createDir
    if not os.path.exists("{}/{}".format(root, name)):
        os.mkdir("{}/{}".format(root, name))
        return True
    return False

def copyBaseFiles(name, root):
    root = root + "/" + name
    print text.copyingFiles
    for directory in ["/bin", "/lib", "/lib64"]:
        shutil.copytree(directory, root + directory, symlinks=True)
        
def create():
    root = getRootDir.getRoot() + "/.shiply"
    template = getArg.getArg("-t")
    if len(sys.argv) < 3:
        sys.exit(text.createHelper)
    name = sys.argv[2]
    if not createDir(name, root):
        sys.exit(text.envAlreadyExists)
    copyBaseFiles(name, root)
    if template:
        print template
    print text.envCreated

