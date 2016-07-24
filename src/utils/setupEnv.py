import os
import urllib
import getRootDir
import tarfile
import text

def setup():
    root = getRootDir.getRoot()
    os.mkdir(root + "/.coffer")
    os.mkdir(root + "/.coffer/envs")
    print text.downloadingFiles
    deboot = urllib.urlopen("http://ftp.debian.org/debian/pool/main/d/debootstrap/debootstrap_1.0.81~bpo8+1.tar.gz").read()
    path = getRootDir.getRoot() + "/.coffer/deboot.tar"
    with open(path, 'wb') as tarf:
        tarf.write(deboot)
    tarfile.open(path).extractall(path=root + "/.coffer/")
    os.remove(path)
    edit = open(root + "/.coffer/debootstrap/debootstrap").read()
    edit = "DEBOOTSTRAP_DIR={}\n".format(root + "/.coffer/debootstrap") + edit
    with open(root + "/.coffer/debootstrap/debootstrap", 'w') as w:
        w.write(edit) 
