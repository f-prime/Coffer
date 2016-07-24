import sys
sys.path.append("../")
from src.utils import templateUtils

#templateUtils.copyFile("/etc/resolv.conf")
#templateUtils.copyProgram("/usr/bin/apt-get")
#templateUtils.copyProgram("/usr/bin/dpkg")
templateUtils.copyDir("/usr/bin")
templateUtils.copyDir("/usr/lib")
templateUtils.copyDir("/usr/sbin")
