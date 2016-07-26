Templates
=========

Templates are used to programatically add extra functionalities to a Coffer environment. By default, Coffer is similar in functionality to a fresh
Ubuntu intallation, but still lacks many features. Templates allow developers to leverage certain functionalities of Coffer to add more
programs and functionalities to a Coffer environment.

### Creating Templates

Templates are Python files that import the `templateUtils` module provided by coffer. In the example below we will be setting up an Ubuntu Python environment.

```
from coffer.utils import templateUtils

execute = templateUtils.executeCommand

execute("apt-get install -y git")
execute("git clone https://github.com/Max00355/Coffer.git")
execute("cd Coffer")
execute("python setup.py install")
```

The template above will download git, then install Coffer in a new Coffer environment. Cofferception.

Templates are meant to be simple, they are Python scripts at heart, but coffer tries to do a lot of the heavy lifting. 
We will save this template as `first-template.py`

### Creating env with template

Now that we have our template created and saved we can use it to create an environment.

`coffer create coffer-env -t first-template.py`

The above command will create the environment `coffer-env` and then execute the `first-template.py` template granted that it is in your current directory. 

### Template Utilities Functions

Import coffer utils using `from coffer.utils import templateUtils`

#### executeCommand

`templateUtils.executeCommand(command)`

Allows a template to execute a shell command inside of an environment.

#### copyDir

`templateUtils.copyDir(path)`

Copies a directory from the host system to the new environment

#### copyFile

`templateUtils.copyFile(path)`

Copies a file from the host system to the new env in the same directory.

Example: Copying `/etc/resolv.conf` will create `etc` in the environment then copy `resolv.conf` into `etc`

#### copyProgram

`templateUtils.copyProgram(path_to_program)`

Copy allows a template to copy a program outside of the environment into the environment along with all its dependencies. Example: `/usr/bin/wget`.
