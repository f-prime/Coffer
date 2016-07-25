from coffer.utils import isRoot, text, getRootDir
import os
import sys

def renameDir(path, name):
    os.rename(path, name)

def rename():
    if not isRoot.isRoot():
        sys.exit(text.notRoot)
    root = getRootDir.getRoot() + "/.coffer/envs/"

    if len(sys.argv) < 4:
        sys.exit(text.renameHelper)

    name = sys.argv[2]
    newName = sys.argv[3]
    

    if not os.path.exists(root + name):
        sys.exit(text.envDoesntExist)

    if os.path.exists(root + newName):
        sys.exit(text.nameAlreadyExists)

    renameDir(root + name, root + newName)
    sys.exit(text.renameSuccessful)
