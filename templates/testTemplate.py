import sys
sys.path.append("../")
from src.utils import templateUtils

#templateUtils.executeCommand("ls")

templateUtils.copyProgram("/etc/resolve.conf")
templateUtils.copyProgram("/usr/bin/wget")
