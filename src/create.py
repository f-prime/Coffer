import os
from utils import getRootDir, text
import sys
import re
import string
import shutil

def getTemplate():
    check = re.findall("-t [a-zA-Z0-9{}]+".format(string.punctuation), ' '.join(sys.argv))
    if check:
        return check[0]
    return None

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
    template = getTemplate()
    name = sys.argv[2]
    if not createDir(name, root):
        sys.exit(text.envAlreadyExists)
    copyBaseFiles(name, root)
    print text.envCreated

