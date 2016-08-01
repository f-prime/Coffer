import sys
from coffer.utils import text, getRootDir, setupEnv, getArg, commands
import os

def checkArgs():
    rootDir = getRootDir.getCofferDir()
    if not os.path.exists(rootDir):
        print(text.settingUpEnv)
        setupEnv.setup()

    mainCmd = getArg.getCommandName()
    if not mainCmd:
        sys.exit(text.helperText)
    
    if mainCmd in commands.commands:
        commands.commands[mainCmd]()
    else:
        sys.exit(text.helperText)

if __name__ == "__main__":
    checkArgs()
