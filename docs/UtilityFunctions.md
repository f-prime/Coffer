# Overview

Coffer has utility functions that make it easier to perform many common tasks when developing a coffer command. 

## ccopy

ccopy, or `coffer copy` is the coffer utility for copying directories and files.

#### Functions

`ccopy.copy(origin, destination, useShutil=False)`

Example: `ccopy.copy("/home/project", "/home/backup/project")`

## getArg

Utility used for extracting value of argument flags from a command.

#### Functions

`getArg.getArg(flag)`

Example: `getArg.getArg("-v")`

Returns: Value of flag

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


