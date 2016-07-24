import sys

def getArg(flag):
    if flag in sys.argv:
        check = sys.argv.index(flag)
        if check != -1 and len(sys.argv) - 1 > check:
            return sys.argv[check + 1]
    return None
