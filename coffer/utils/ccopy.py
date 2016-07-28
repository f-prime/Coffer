import os
import shutil

def copy(orig, dest, useShutil=False):
    if os.path.isdir(orig):
        if useShutil:
            shutil.copytree(orig, dest, symlinks=True)
        else:
            os.system("cp -rf {} {}".format(orig, dest))
    else:
        if useShutil:
            shutil.copy(orig, dest)
        else:
            os.system("cp {} {}".format(orig, dest))
