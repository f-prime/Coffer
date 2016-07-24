import os
from utils import getRootDir, text, getArg, ccopy
import sys
import re
import string
import imp

def createDir(path):
    print text.createDir
    if not os.path.exists(path):
        os.mkdir(path)
        return True
    return False

def copyBaseFiles(path):
    print text.copyingFiles
    debCmd = "bash " + getRootDir.getRoot() + "/.coffer/debootstrap/debootstrap precise {}"
    os.system(debCmd.format(path))

def executeTemplate(template):
    try:
        imp.load_source(template.split(".")[0], template)
        print text.templateSuccess
    except Exception, e:
        print e
        print text.invalidTemplate

def create():
    root = getRootDir.getRoot() + "/.coffer"
    template = getArg.getArg("-t")
    if len(sys.argv) < 3:
        sys.exit(text.createHelper)
    name = sys.argv[2]
    path = root + "/" + name
    if not createDir(path):
        sys.exit(text.envAlreadyExists)
    copyBaseFiles(path)
    if template:
        executeTemplate(template)
    print text.envCreated

