from coffer.utils import getRootDir, text, isRoot, getArg
from coffer import remove
from coffer import create
import tarfile
import sys
import os

def decompressArchive(compressed, path):
    f = tarfile.TarFile(compressed)
    f.extractall(path=path)

def decompress(compressed, path):
    create.createDir(path)
    print (text.unpackaging)
    decompressArchive(compressed, path)
    
def unpackage():
    rootDir = getRootDir.getEnvsDir()
    compressed = getArg.getArg(0)

    if not compressed:
        sys.exit(text.unpackageHelper)
    if not isRoot.isRoot():
        sys.exit(text.noRoot)
    if not remove.checkIfExists(compressed):
        sys.exit(text.packageDoesntExist)

    env = compressed.split("/")[-1].split(".")[0]

    if remove.checkIfExists(rootDir + env):
        sys.exit(text.envAlreadyExists)

    decompress(compressed, rootDir + env)
    print (text.unpackagedSuccessful)
