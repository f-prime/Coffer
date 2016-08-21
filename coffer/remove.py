from coffer.utils import getRootDir, text, isRoot, getArg
import os
import shutil
import sys
import re

def removeDir(path):
    print (text.removingEnv)
    shutil.rmtree(path)

def checkIfExists(path):
    return os.path.exists(path)

def getMounted(path):
    mounted = os.popen("mount | grep 'coffer'").read()
    mounted = re.findall("on (.*) type", mounted)
    for m in mounted:
        if path in m:
            yield m

def unmountAll(path):
    for m in getMounted(path):
        print (text.umounted.format(m))
        os.system("umount {}".format(m))

def remove():
    rootDir = getRootDir.getEnvsDir()

    name = getArg.getArg(0)

    if not name:
        sys.exit(text.removeHelper)
    if not isRoot.isRoot():
        sys.exit(text.notRoot)
    if not checkIfExists(rootDir + name):
        sys.exit(text.envDoesntExist)
    unmountAll(rootDir + name)
    #removeDir(rootDir + name)
    print (text.removed)
