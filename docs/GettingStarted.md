# Installing Coffer
 
Coffer currently only supports Linux and MacOS systems. Windows is currently not supported.

1. Clone the repo `git clone https://github.com/Max00355/Coffer.git`
2. Install Coffer from setup.py `python setup.py install`
3. Setup coffer by typing `coffer`

Coffer will create a folder called `.coffer` in your home directory. This folder will contain all of your environments as well as tools that Coffer needs to create these
environments.

Coffer should now be installed.

# Setting up your first environment

Now that Coffer has been installed we can get started with creating environments. Coffer environments are Ubuntu environments, thus by default they have access to many of the 
applications that a default Ubuntu installation has access to such as `apt-get`.

Creating environments requires access to the internet.
Creating Coffer environments also requires root access, so make sure that your account has `sudo` rights.

1. In a new terminal type `sudo coffer create myenv`

Coffer will now download and install all of the requirements of an environment. This could take a bit depending on your computer and internet connection.

2. Enter the environment `sudo coffer enter myenv` 

And like that you are now in your first coffer environment! You can now install applications using `apt-get` or however else you'd like.

# Introduction to templates

Coffer gives the ability to create templates for environments which automatically executes commands and adds functionalities which aren't in a coffer environment by default.

For more information about templates checkout the [template documentation](https://github.com/Max00355/Coffer/blob/master/docs/Templates.md)

# Usage Tips

- Since creating environments requires access to the internet it is suggested that you create a `template` environment which you can then `clone` using `coffer clone` 
  This is much quicker and faster than using the `coffer create` command every time.

- Use `coffer list` to list the environments that are available to you.

- You can share environments using either a template, or by sending the environment folder which is located in `~/.coffer/envs/`
