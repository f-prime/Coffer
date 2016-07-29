import os
from coffer.utils import getRootDir, text, getFlag, ccopy, templateUtils, isRoot, content
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
    
    version = getFlag.getFlag("-v")
    if version not in content.versions:
        version = "precise"
    print (text.usingVersion.format(version))
    debCmd = "bash " + getRootDir.getRoot() + "/.coffer/debootstrap/debootstrap --arch=" + arch + " {} {}"
    os.system(debCmd.format(version, path))
    getSourceList(path, version)

def getSourceList(path, version):
    version = version.lower()
    if not os.path.exists(path + "/etc/apt/"):
        sys.exit(text.failedToCreate)
    
    if version in content.listUrls:
        with open(path + "/etc/apt/sources.list", 'wb') as f:
            source = urllib.urlopen(content.listUrls[version]).read()
            f.write(source)

def executeTemplate(template):
    templateName = template.split("/")[-1]
    templateName = templateName.split(".")[0]
    imp.load_source(templateName, template) # This could break, but I'd rather allow it to break
    print (text.templateSuccess)

def create():
    root = getRootDir.getRoot() + "/.coffer/envs"
    template = getFlag.getFlag("-t")
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

