from coffer.utils import templateUtils
import os

cmd = templateUtils.executeCommand

name = os.popen("logname").read().strip()

exc = """mkdir /home/{0};
touch /home/{0}/.bashrc;
cd /home/{0};
apt-get install -y git;
git clone https://github.com/Max00355/HNXplorer;
echo cd /home/{0}/HNXplorer >> ~/.bashrc;
echo python hnx.py >> ~/.bashrc;
echo exit >> ~/.bashrc
""".format(name)

cmd(exc)
cmd("echo Hackernews has been installed!")
