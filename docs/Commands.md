# Coffer Commands

Below are the commands available to Coffer, and what they do.

### Create

Usage: `coffer create <name>`

Creates an environment from scratch with the name `<name>`

### Clone

Usage: `coffer clone <name> <clone>`

Creates an exact copy of an environment `<name>` to a new environment by name `<clone>`

### Enter

Usage: `coffer enter <name>`

Enters a Coffer environment and launches a Bash shell. 

### List

Usage: `coffer list`

Lists all of the environments available to Coffer.

### Remove

Usage: `coffer remove <name>`

Removes a Coffer environment by name `<name>` 

This is a nonreversible action. Once an environmentis removed, it can not be restored.

### Version

Usage: `coffer version`

Displays the current version of Coffer.
