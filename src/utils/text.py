helperText = """Coffer Help

coffer create <name> [-t <template>]
coffer enter <name> [-c <command>]
coffer list
coffer clone <name> <clone_name>
coffer remove <name>
"""

envAlreadyExists = "An environment by that name already exists."
envDoesntExist = "There is no environment by that name."

notRoot = "Must be root to execute this command."
noEnvs = "There aren't any environments currently created"

createHelper = "Usage: coffer create <name> [-t <template>]"
enterHelper = "Usage: coffer enter <name> [-c <command>]"
removeHelper = "Usage: coffer remove <name>"
removed = "Environment has been removed"
removingEnv = "Removing environment"
createDir = "Creating environment directory"
copyingFiles = "Copying necessary files over"
envCreated = "Environment has been created"
