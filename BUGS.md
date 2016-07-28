# Known Bugs

### WIll be fixed in 1.1.1

- Clone closes before the clone is complete (FIXED)
- apt-get does not installon Fedora
- FileNotFoundError: [Errno 2] No such file or directory: '/root/.coffer/envs/abc/etc/apt/sources.list'
  Sources.list file not correct
  File "/usr/local/lib/python3.4/dist-packages/Coffer-1.1.0-py3.4.egg/coffer/coffer.py", line 33, in checkArgs
  File "/usr/local/lib/python3.4/dist-packages/Coffer-1.1.0-py3.4.egg/coffer/create.py", line 62, in create
  File "/usr/local/lib/python3.4/dist-packages/Coffer-1.1.0-py3.4.egg/coffer/create.py", line 34, in copyBaseFiles
  FileNotFoundError: [Errno 2] No such file or directory: '/root/.coffer/envs/abc/etc/apt/sources.list' 
  (
    This means that certain packages could not be retrieved and an error should be returned suggesting that the user try a different version of debian/ubuntu
    May be fixed by allowing user to select mirror
    Use: https://repogen.simplylinux.ch/generate.php 
  )

- Templates aren't working
- Fix command line argument parsing
- Code cleanup 

### Other Bugs
