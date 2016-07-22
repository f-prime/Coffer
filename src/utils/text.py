helperText = """Coffer Help

coffer create <name> [-t <template>]
coffer enter <name> [-c <command>]
coffer list
coffer clone <name> <clone_name>
coffer remove <name>
"""

envAlreadyExists = "An environment by that name already exists."
envAlreadyExistsVar = "An environment by the name {} already exists."

envDoesntExist = "There is no environment by that name."
envDoesntExistVar = "There is no environment by the name {}"

programDoesNotExist = "There is no program found by the name {}"

notRoot = "Must be root to execute this command."
noEnvs = "There aren't any environments currently created"

cloneHelper = "Usage: coffer clone <name> <clone_name>"
cloned = "Environment has been cloned successfully"
cloning = "Cloning enviornment"

availableEnvironments = "Available Environments"

createHelper = "Usage: coffer create <name> [-t <template>]"
enterHelper = "Usage: coffer enter <name> [-c <command>]"
removeHelper = "Usage: coffer remove <name>"
removed = "Environment has been removed"
removingEnv = "Removing environment"
createDir = "Creating environment directory"
copyingFiles = "Copying necessary files over"
envCreated = "Environment has been created"
