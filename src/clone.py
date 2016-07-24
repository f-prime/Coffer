from utils import getRootDir, text, ccopy
import shutil
import sys
import os

def copyEnv(path, to):
    print text.cloning
    ccopy.copy(path, to)

def envExists(path):
    return os.path.exists(path)

def clone():
    if len(sys.argv) < 4:
        sys.exit(text.cloneHelper)

    name = sys.argv[2]
    clone = sys.argv[3]

    path = getRootDir.getRoot() + "/.coffer/envs/" + name
    clonePath = getRootDir.getRoot() + "/.coffer/envs/" + clone

    if not envExists(path):
        sys.exit(text.envDoesntExistVar.format(name))
    if envExists(clonePath):
        sys.exit(text.envAlreadyExistsVar.format(clone))

    copyEnv(path, clonePath)
    print text.cloned
