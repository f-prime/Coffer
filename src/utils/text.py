helperText = """Shiply Help

shiply create <name> [-t <template>]
shiply enter <name> [-c <command>]
shiply list
shiply clone <name> <clone_name>
shiply remove <name>
"""

envAlreadyExists = "An environment by that name already exists."
envDoesntExist = "There is no environment by that name."

notRoot = "Must be root to execute this command."
noEnvs = "There aren't any environments currently created"

createHelper = "Usage: shiply create <name> [-t <template>]"
enterHelper = "Usage: shiply enter <name> [-c <command>]"
removeHelper = "Usage: shiply remove <name>"
removed = "Environment has been removed"
removingEnv = "Removing environment"
createDir = "Creating environment directory"
copyingFiles = "Copying necessary files over"
envCreated = "Environment has been created"
