import sys
sys.path.append("../")
from src.utils import templateUtils

templateUtils.executeCommand("ls")
templateUtils.copyFile("/etc/resolv.conf")
templateUtils.copyFile("/dev/null")

templateUtils.copyProgram("/usr/bin/apt-get")
templateUtils.copyDir("/usr/share/git-core")
templateUtils.copyProgram("/usr/bin/wget")
