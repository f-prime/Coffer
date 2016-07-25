import sys
from coffer import create
from coffer import enter
from coffer import clone
from coffer import remove
from coffer import ls
from coffer import version
from coffer import rename
from coffer.utils import text, getRootDir, setupEnv
import os

def checkArgs():
    rootDir = getRootDir.getRoot()
    if not os.path.exists(rootDir + "/.coffer"):
        print(text.settingUpEnv)
        setupEnv.setup()

    if len(sys.argv) < 2:
        sys.exit(text.helperText)
    
    functions = {
        "create":create.create,
        "clone":clone.clone,
        "enter":enter.enter,
        "remove":remove.remove,
        "list":ls.ls,
        "version":version.version,
        "rename":rename.rename,
    }

    mainCmd = sys.argv[1]
    if mainCmd in functions:
        functions[mainCmd]()
    else:
        sys.exit(text.helperText)

if __name__ == "__main__":
    checkArgs()
