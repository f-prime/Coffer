import os
import string
from coffer.utils import text, getRootDir, isRoot, getFlag, getArg
from coffer import create
import sys
import re

def enterChroot(path):
    os.chdir(path)
    os.chroot(path)

def executeCommand(command="/bin/bash"):
    os.system(command)

def enter():
    if not isRoot.isRoot():
        sys.exit(text.notRoot)
    rootDir = getRootDir.getEnvsDir()
    name = getArg.getArg(0)
    if not name:
        sys.exit(text.enterHelper)
    template = getFlag.getFlag("-t")
    if template:
        create.executeTemplate(template)
    path = rootDir + name
    if not os.path.exists(path):
        sys.exit(text.envDoesntExist)
    enterChroot(path)
    command = getFlag.getFlag("-c")
    if command:
        executeCommand(command=command)
    else:
        executeCommand()
