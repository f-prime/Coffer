import sys
import os
import text
import re
import shutil
import getRootDir

def copyProgram(path):
    if not os.path.exists(path):
        print text.programDoesNotExist.format(path)
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

def createPath(path):
    root = getRootDir.getRoot() + "/.coffer/" + getEnvName() + "/"
    for p in path:
        root += "/" + p
        if not os.path.exists(root):
            os.mkdir(root)

def copyDep(dep):
    root = getRootDir.getRoot() + "/.coffer/" + getEnvName()
    shutil.copy(dep, root + dep)

def executeCommand(command):
    pass

def getEnvName():
    # This has to work because `create` has already checked that the syntax is correct.
    if len(sys.argv) < 3:
        sys.exit("Cannot continue, working outside context of coffer")
    return sys.argv[2]
