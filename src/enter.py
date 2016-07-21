import os
import string
from utils import text, getRootDir, isRoot, getArg
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
    rootDir = getRootDir.getRoot() + "/.coffer"
    if len(sys.argv) < 3:
        sys.exit(text.enterHelper)
    name = sys.argv[2]
    path = rootDir + "/" + name
    if not os.path.exists(path):
        sys.exit(text.envDoesntExist)
    enterChroot(path)
    command = getArg.getArg("-c")
    if command:
        executeCommand(command=command)
    else:
        executeCommand()
