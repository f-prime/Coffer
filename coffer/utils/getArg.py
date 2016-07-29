import sys

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
    print args
    if num > len(args) - 1:
        return None
    return args[num]
