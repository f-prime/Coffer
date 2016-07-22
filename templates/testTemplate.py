import sys
sys.path.append("../")
from src.utils import templateUtils

templateUtils.executeCommand("ls")
templateUtils.copyFile("/etc/resolv.conf")
templateUtils.copyFile("/dev/null")

templateUtils.copyProgram("/usr/bin/apt-get")
templateUtils.copyProgram("/usr/bin/dpkg")
templateUtils.copyDir("/var/lib/dpkg")
templateUtils.copyDir("/etc/apt")
templateUtils.copyDir("/usr/share/git-core")
templateUtils.copyProgram("/usr/bin/wget")
