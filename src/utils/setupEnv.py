import os
import urllib
import getRootDir
import tarfile
import text

def setup():
    root = getRootDir.getRoot()
    os.mkdir(root + "/.coffer")
    print text.downloadingFiles
    deboot = urllib.urlopen("http://ftp.debian.org/debian/pool/main/d/debootstrap/debootstrap_1.0.81~bpo8+1.tar.gz").read()
    path = getRootDir.getRoot() + "/.coffer/deboot.tar"
    with open(path, 'wb') as tarf:
        tarf.write(deboot)
    tarfile.open(path).extractall(path=root + "/.coffer/")
    os.remove(path)
