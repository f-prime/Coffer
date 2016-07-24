import os
from utils import getRootDir, text

def list():
    print text.availableEnvironments
    check = os.listdir(getRootDir.getRoot() + "/.coffer/envs")
    if len(check) == 0:
        print text.noEnvs
    else:
        print '\n'.join(check)
