# Overview

Commands are what add functionality to coffer. All commands are modules and are very straight forward to start developing. 

An example command execution looks like: `coffer create environment -v jessie` where `create` is the command in this case.

# Adding Commands

## Create the module file

All commands are modules and belong in the `coffer/` directory. 
Create a `.py` file that looks like this: `<name of command>.py`

So let's say we are creating the command `version` we'd create the
file `coffer/version.py`

Naming is very important for readability so be sure abide by this system.


## Add module to coffer.py

Now we need to make the command callable. This is done in `utils/commands.py`
by importing the module and modifying the `commands` dictionary. 

Adding to the commands dictionary should follow this pattern:

`<command>:<entry point function>`

So, for our `version.py` example if `version.py` was our only command then `commands.py` would look something like this:

```
from coffer import version

commands = {
     
  "version":version.version  

}
```

The entry point function should be named the same as the command.


## Update help text

The command now needs to be documented. This can be done my modifying
`coffer/utils/text.py` and adding the command and its flags
to the `helperText` variable. 

Also, the documentation 

## Writing the code

Now it is time to write the code that makes the new command work. This is up 
to how you decide to implement the command, but before you proceed here are a few things to keep in mind.

- Create many small functions that do one thing very well. That will make it easier for future developers to develop tests and find bugs.
- Plan the command before you start to code. Make sure the idea is clear and that everthing has been planned out.
- Ask for help when needed, and report problems as you find them. If you are stumped on something you can ask on our [community chat](https://gitter.im/cofferproject/Lobby).
  As you find bugs create issues describing what the problem is so that other developers can be aware that they exist, and possibly create a fix. 
- Test your command thoroughly before creating a pull request.
- All commands are to be parsed as follows: `coffer <command> <arg1> <arg2..n> <flag1> <flag2..n>` 
- If arguments are expected to be in your command use the `utils.getArg` function. 
- If flags are expected to be in your use the `utils.getFlag` function. 
