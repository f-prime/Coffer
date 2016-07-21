import getpass

def isRoot():
    return getpass.getuser() == "root"
