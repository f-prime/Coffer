import os

def isRoot():
    return os.geteuid() == 0
