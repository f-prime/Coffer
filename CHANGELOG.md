# 1.3.1

- Added `-m` flag for mounting directories into env 
- Added `getFlags` function for returning multiple values with the same flag
- Auto unmounts directory when removing/cloning 
- `package` command which compresses an env and allows for easier sending of an env (NOT DONE)
- `open` command restores a packaged environment (NOT DONE)
- Ability to remove multiple environments at once (NOT DONE)


# 1.2.1

- Ability to execute templates on already existing coffer env `coffer enter <env> -t <template>`
- Add flag to `create` for selecting repo
- Add flag to `create` to select architecture
- Code Cleanup
- Default settings now use ubuntu xenial instead of ubuntu precise
- Documented changed
- Now treats source.list as content in `content.py` instead of pulling from a URL that could be down.

# 1.1.1

- Clone waits until environment has been cloned before closing
- Fixed issue with templates that prevented multiple `template.executeCommand` functions to be called
- Coffer `create` fails gracefully when the environment cannot be created
- Appropriate sources.list is downloaded for the version of the environment being downloaded.
- Added `content` utility for managing content
- Added function to getRootDir `getCofferRoot`
- Added docs for utility functions
- Added docs for adding a command to coffer

# 1.1.0

- Fixed issue #1
- Updated code base to Python 3
- Added `rename` command to rename envs
- Better root checking
- Added `-v` flag to the `create` that allows for the specifying of the debian/ubuntu environment to be installed. `coffer create env -v wheezy`
