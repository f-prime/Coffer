import os

def getRoot():
    root = os.getenv("HOME")
    if not root:
        return os.getcwd()
    else:
        return root

def getCofferDir():
    return getRoot() + "/.coffer/"

def getEnvsDir():
    return getCofferDir() + "envs/"
