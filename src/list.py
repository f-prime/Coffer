import os
from utils import getRootDir, text

def list():
    check = os.listdir(getRootDir.getRoot() + "/.coffer")
    if len(check) == 0:
        print text.noEnvs
    else:
        print '\n'.join(check)
