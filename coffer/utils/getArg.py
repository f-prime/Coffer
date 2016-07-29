import sys

def getArg(num):
    start = sys.argv[2:]
    if num > len(start):
        return None
    on = 0
    while on < num:
        if start[on].startswith("-"):
            on += 2
            if on > len(start):
                return None
        else:
            on += 1
    return start[on]
