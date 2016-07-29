import os

def getRoot():
    root = os.getenv("HOME")
    if not root:
        return os.getcwd()
    else:
        return root

def getCofferRoot():
    return getRoot() + "/.coffer"
