import sys

def getCommandName():
    if len(sys.argv) >= 2:
        return sys.argv[1]
    return None

def getArg(num):
    start = sys.argv[2:]
    args = []
    skip = False
    for s in start:
        if skip:
            skip = False
            continue
        if s.startswith("-"):
            skip = True
            continue
        args.append(s)
    if num > len(args) - 1:
        return None
    return args[num]
