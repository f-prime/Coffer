import sys
sys.path.append("../")
from src.utils import templateUtils

templateUtils.executeCommand("yes | apt-get install git")
