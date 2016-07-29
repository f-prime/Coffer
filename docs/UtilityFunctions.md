# Overview

Coffer has utility functions that make it easier to perform many common tasks when developing a coffer command. 

## ccopy

ccopy, or `coffer copy` is the coffer utility for copying directories and files.

#### Functions

`ccopy.copy(origin, destination, useShutil=False)`

Example: `ccopy.copy("/home/project", "/home/backup/project")`

## getFlag

Utility used for extracting value of argument flags from a command.

#### Functions

`getFlag.getFlag(flag)`

Example: `getFlag.getFlag("-v")`

Returns: Value of flag


## getArg

Used for getting the arguments of a command. Arguments are numbered starting from 0.

#### Functions

`getArg.getArg(num)`

Example: `getArg.getArg(1)`

Input: `coffer clone test test2`

Returns: `test2`

NOTE: `getArg` skips over flags. So for example the output would be the same for the above if the command looked like `coffer clone test -v example test2`. The output would still be `test2`

## getRootDir

Returns the home directory of a computer. This is used to setup the `.coffer` directory.

#### Functions

`getRootDir.getRoot()`

Returns: Home directory

`getRootDir.getCofferRoot()`

Returns: Home directory + "/.coffer"

## isRoot

Determines whether coffer is running as root or not.

#### Functions

`isRoot.isRoot()`

Returns: Bool

## setupEnv

Sets up the `~/.coffer` directory. Downloaded debootstrap and creates the `~/.coffer/envs` directory.

#### Functions

`setupEnv.setup()`


