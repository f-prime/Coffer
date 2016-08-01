from coffer import create
from coffer import enter
from coffer import clone
from coffer import remove
from coffer import ls
from coffer import version
from coffer import rename

commands = {
    "create":create.create,
    "clone":clone.clone,
    "enter":enter.enter,
    "remove":remove.remove,
    "list":ls.ls,
    "version":version.version,
    "rename":rename.rename,
}

