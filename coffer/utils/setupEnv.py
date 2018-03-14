import os
import urllib.request as urllib
from coffer.utils import getRootDir
import tarfile
from coffer.utils import text

def setup():
    root = getRootDir.getCofferDir()
    envs = getRootDir.getEnvsDir()
    os.mkdir(root)
    os.mkdir(envs)
    print (text.downloadingFiles)
    deboot = urllib.urlopen("http://ftp.debian.org/debian/pool/main/d/debootstrap/debootstrap_1.0.92~bpo9+1.tar.gz").read()
    path = root + "deboot.tar"
    with open(path, 'wb') as tarf:
        tarf.write(deboot)
    tarfile.open(path).extractall(path=root)
    os.rename(root + "debootstrap-1.0.92~bpo9+1", root + "debootstrap") 
    os.remove(path)
    edit = open(root + "debootstrap/debootstrap").readlines()
    edit[485] = "#" + edit[485]
    edit[486] = "#" + edit[486]
    edit[487] = "#" + edit[487]
    edit = "".join(edit)
    edit = "DEBOOTSTRAP_DIR={}\n".format(root + "debootstrap") + edit
    with open(root + "debootstrap/debootstrap", 'w') as w:
        w.write(edit) 

