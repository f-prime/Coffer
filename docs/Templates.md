Templates
=========

Templates are used to programatically add extra functionalities to a chroot. By default, a coffer environment is nothing more than a very basic bash shell. It is stripped
of most other features and just contains the bare minimum to be considered usable. Templates allow developers to leverage certain functionalities of coffer to add more
programs and functionalities to a coffer environment. For example, a Python environment could be setup by simply executing `coffer create pythonenv -t python` granted
the Python template exists in your current directory.

### Creating Templates

Templates are Python files that import the `templateUtils` module provided by coffer. In the example below we will be setting up an Ubuntu Python environment.

```
from coffer.utils import templateUtils

copy = templateUtils.copyProgram
execute = templateUtils.executeProgram

copy("/usr/bin/apt-get")

execute("apt-get update")
execute("apt-get install python")
execute("apt-get install python-pip")
```

Templates are system dependant so the above example will only work on a system with `apt-get` installed, but it could very easily be altered to work on a Fedora or 
any other OS/distro.

Templates are meant to be simple, they are Python scripts at heart but coffer tries to do a lot of the heavy lifting. We will save this template as `python-ubuntu.py`

### Creating env with template

Now that we have our template created and saved we can use it to create an environment.

`coffer create python-env -t python-ubuntu`

The above command will create the environment `python-env` and then execute the `python-env` template granted that it is in your current directory. Coffer will come with
a few built in templates that can be used and will als have access to a repository of templates (future reference)

### Template Utilities Functions

#### execute

`execute(command)`

Execute allows a template to execute a shell command inside of an environment.

#### copy 

`copy(path_to_program)`

Copy allows a template to copy a dynamic program outside of the environment into the evironment. Example, apt-get, or Python.
