import sys
import create
import enter
import clone
import remove
import list as list_
from utils import text, getRootDir
import os

def checkArgs():
    rootDir = getRootDir.getRoot()
    if not os.path.exists(rootDir + "/.coffer"):
        os.mkdir(rootDir + "/.coffer")

    if len(sys.argv) < 2:
        sys.exit(text.helperText)
    
    functions = {
        "create":create.create,
        "clone":clone.clone,
        "enter":enter.enter,
        "remove":remove.remove,
        "list":list_.list,
    }

    mainCmd = sys.argv[1]
    if mainCmd in functions:
        functions[mainCmd]()
    else:
        sys.exit(text.helperText)

if __name__ == "__main__":
    checkArgs()
