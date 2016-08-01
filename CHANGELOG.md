# 1.2.1

- Ability to execute templates on already existing coffer env `coffer enter <env> -t <template>` (NOT DONE #5)
- Add flag to `create` for selecting repo (NOT DONE #4)
- Add flag to `create` to select architecture (NOT DONE #2)
- Add flag to `create` to select download mirror (NOT DONE #3)
- Tests (NOT DONE #6)
- Code Cleanup


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
