import os
from utils import getRootDir, text, getArg, ccopy, templateUtils, isRoot
import sys
import re
import string
import imp
import urllib

def createDir(path):
    print (text.createDir)
    if not os.path.exists(path):
        os.mkdir(path)
        return True
    return False

def copyBaseFiles(path):
    print (text.copyingFiles)
    debCmd = "bash " + getRootDir.getRoot() + "/.coffer/debootstrap/debootstrap precise {}"
    os.system(debCmd.format(path))

    # Debootstrap does not install a decent source.list, so we have to do it here

    with open(path + "/etc/apt/sources.list", 'w') as f:
        f.write(urllib.urlopen("https://help.ubuntu.com/12.04/sample/sources.list").read())

    # Then we have to add keys since we are using a  new source list.

    templateUtils.executeCommand("gpg --keyserver keyserver.ubuntu.com --recv 3E5C1192")
    templateUtils.executeCommand("gpg --export --armor 3E5C1192 | sudo apt-key add -")
    templateUtils.executeCommand("apt-get update")

def executeTemplate(template):
    try:
        imp.load_source(template.split(".")[0], template)
        print (text.templateSuccess)
    except Exception as e:
        print (e)
        print (text.invalidTemplate)

def create():
    root = getRootDir.getRoot() + "/.coffer/envs"
    template = getArg.getArg("-t")
    if len(sys.argv) < 3:
        sys.exit(text.createHelper)
    if not isRoot.isRoot():
        sys.exit(text.notRoot)
    name = sys.argv[2]
    path = root + "/" + name
    if not createDir(path):
        sys.exit(text.envAlreadyExists)
    copyBaseFiles(path)
    if template:
        executeTemplate(template)
    print (text.envCreated)

