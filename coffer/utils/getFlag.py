import sys
import copy

def getFlag(flag):
    if flag in sys.argv:
        check = sys.argv.index(flag)
        if check != -1 and len(sys.argv) - 1 > check:
            return sys.argv[check + 1]
    return None

def getFlags(flag):
    values = []
    argvs = copy.deepcopy(sys.argv)
    for x in range(argvs.count(flag)):
        check = argvs.index(flag)
        if check != -1 and len(argvs) - 1 > check:
            values.append(argvs[check + 1])
            argvs.pop(check)
    return values
    
