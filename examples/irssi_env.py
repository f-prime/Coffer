from coffer.utils import templateUtils
import os

exe = templateUtils.executeCommand

logname = os.popen("logname").read().strip()

command = """
apt-get update
apt-get install -y irssi
mkdir /home/{}
cd ~/
touch .bashrc
echo irssi > .bashrc
echo exit >> .bashrc
""".format(logname)

exe(command)

