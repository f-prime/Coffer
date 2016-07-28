import os
from coffer.utils import getRootDir, text, getArg, ccopy, templateUtils, isRoot
import sys
import re
import string
import imp
import urllib.request as urllib
import platform

def createDir(path):
    print (text.createDir)
    if not os.path.exists(path):
        os.mkdir(path)
        return True
    return False

def copyBaseFiles(path):
    print (text.copyingFiles)
    # Supports 64 bit and 32 bit, no arm yet (though should be an easy fix)
    if platform.architecture()[0] == "64bit":
        arch = "amd64"
    else:
        arch = "i386"
    
    version = getArg.getArg("-v")
    if version not in text.versions:
        version = "precise"
    print (text.usingVersion.format(version))
    debCmd = "bash " + getRootDir.getRoot() + "/.coffer/debootstrap/debootstrap --arch=" + arch + " {} {}"
    os.system(debCmd.format(version, path))

    # Debootstrap does not install a decent source.list, so we have to do it here

    with open(path + "/etc/apt/sources.list", 'wb') as f:
        f.write(urllib.urlopen("https://help.ubuntu.com/12.04/sample/sources.list").read())

    # Then we have to add keys since we are using a  new source list.
    # This should only be a temp fix

    templateUtils.executeCommand("gpg --keyserver keyserver.ubuntu.com --recv 3E5C1192")
    templateUtils.executeCommand("gpg --export --armor 3E5C1192 | sudo apt-key add -")
    templateUtils.executeCommand("apt-get update")

def executeTemplate(template):
    templateName = template.split("/")[-1]
    templateName = templateName.split(".")[0]
    imp.load_source(templateName, template) # This could break, but I'd rather allow it to break
    print (text.templateSuccess)

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

