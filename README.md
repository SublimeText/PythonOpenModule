# Python Open Module
This plugin will open a python module file present on sys.path and any open folders in the window.

## Usage
After opening the input panel (by either "Open Python module" under the File menu, or a keyboard shortcut, type the package name (e.g. `decimal` or `logging.config`) into the input panel and press enter.

## Python sys.path
The sys.path that is searched depends on the python executable, which is selected in the following manner:

1. `python_executable` in user settings (if set and a valid executable)
1. `python` on the current user's path
1. `python` used by sublime itself

## Virtual Environments
You may wish to set `python_executable` in your project settings if you are using a virtualenv. 
For example, if your virtualenv was called `monty`:

    {
		"settings": {
			"python_executable": "/Users/glen/.virtualenvs/monty/bin/python"
		},
		"folders":
		[
			{
				"path": "/Users/glen/monty"
			}
		]
	}
