versions = ['karmic', 'wily', 'jessie-kfreebsd', 'sarge.buildd', 'maverick', 'oneiric', 'gutsy', 'quantal', 'hardy', 'jessie', 'precise', 'stretch', 'woody.buildd', 'dasyatis', 'utopic', 'lenny', 'jaunty', 'yakkety', 'warty.buildd', 'etch-m68k', 'oldstable', 'hoary', 'stable', 'warty', 'edgy', 'vivid', 'lucid', 'intrepid', 'woody', 'unstable', 'trusty', 'sarge.fakechroot', 'etch', 'xenial', 'breezy', 'feisty', 'wheezy', 'hoary.buildd', 'saucy', 'dapper', 'squeeze', 'natty', 'aequorea', 'sid', 'chromodoris', 'sarge', 'raring', 'bartholomea', 'potato', 'testing']

settingUpEnv = "Setting up environment"
downloadingFiles = "Downloading necessary files"
version = "1.1.1"
helperText = """Coffer Help

coffer create <name> [-t <template> -v <ubuntu/debian version>]
coffer enter <name> [-c <command>]
coffer list
coffer clone <name> <clone_name>
coffer remove <name>
coffer version
coffer rename
"""

usingVersion = "Using version {}"

invalidTemplate = "Template is either invalid or does not exist"
templateSuccess = "Template has been executed successfully"

envAlreadyExists = "An environment by that name already exists."
envAlreadyExistsVar = "An environment by the name {} already exists."

envDoesntExist = "There is no environment by that name."
envDoesntExistVar = "There is no environment by the name {}"

programDoesNotExist = "There is no program found by the name {}"
fileDoesNotExist = "There is no file found by the name {}"
folderDoesNotExist = "There is no folder found by the name {}"

notRoot = "Must be root to execute this command."
noEnvs = "There aren't any environments currently created"

cloneHelper = "Usage: coffer clone <name> <clone_name>"
cloned = "Environment has been cloned successfully"
cloning = "Cloning enviornment"
nameAlreadyExists = "Can't rename to environment that already exists"

availableEnvironments = "Available Environments"

renameSuccessful = "Renamed Successfully"

renameHelper = "Usage: coffer rename <name> <new name>" 
createHelper = "Usage: coffer create <name> [-t <template>]"
enterHelper = "Usage: coffer enter <name> [-c <command>]"
removeHelper = "Usage: coffer remove <name>"
removed = "Environment has been removed"
removingEnv = "Removing environment"
createDir = "Creating environment directory"
copyingFiles = "Copying necessary files over. This could take a bit."
envCreated = "Environment has been created"
