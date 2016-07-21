import os
from utils import getRootDir

def list():
    print '\n'.join(os.listdir(getRootDir.getRoot() + "/.shiply"))
