import sys
import os
from coffer.utils import text
import re
import shutil
from coffer.utils import getRootDir
from coffer.utils import ccopy

def copyProgram(path):
    if not os.path.exists(path):
        print (text.programDoesNotExist.format(path))
    else:
        deps = os.popen("ldd {}".format(path)).read()
        deps = deps.replace("\t", "").replace("\n", " ")
        deps = re.findall("=> ([a-z\/0-9\.\_\-\+]+) ", deps)
        dependencies = [path]
        for x in deps:
            if os.path.exists(x):
                dependencies.append(x)
        for dep in dependencies:
            split = dep.split("/")
            split = split[1:len(split)-1]
            createPath(split)
            copyDep(dep)

def copyFile(path):
    if not os.path.exists(path):
        print (text.fileDoesNotExist.format(path))
    else:
        split = path.split("/")
        split = split[:len(split)-1]
        createPath(split)
        copyDep(path)
        

def copyDir(path):
    if not os.path.exists(path):
        print (text.folderDoesNotExist.format(path))
    else:
        split = filter(None, path.split("/"))
        createPath(split[:-1])
        ccopy.copy(path, getRootDir.getRoot() + "/.coffer/envs/" + getEnvName() + "/" + path)

def createPath(path):
    root = getRootDir.getRoot() + "/.coffer/envs/" + getEnvName() + "/" 
    for p in path:
        root += "/" + p
        if not os.path.exists(root):
            os.mkdir(root)
        
def copyDep(dep):
    root = getRootDir.getRoot() + "/.coffer/envs/" + getEnvName()
    shutil.copy(dep, root + dep)

def executeCommand(command):
    cwd = os.getcwd()
    rr = os.open("/", os.O_RDONLY)
    os.chroot(getRootDir.getRoot() + "/.coffer/envs/" + getEnvName())
    os.system(command)
    os.fchdir(rr)
    os.chroot(".")
    os.close(rr)
    os.chdir(cwd)

def getEnvName():
    # This has to work because `create` has already checked that the syntax is correct.
    if len(sys.argv) < 3:
        sys.exit("Cannot continue, working outside context of coffer")
    return sys.argv[2]
