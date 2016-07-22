import os

def copy(orig, dest):
    if os.path.isdir(orig):
        os.system("cp -rf {} {}".format(orig, dest))
    else:
        os.system("cp {} {}".format(orig, dest))
