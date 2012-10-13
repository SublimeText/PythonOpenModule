# Python Open Module
This plugin will open a python module file/directory present on sys.path and any open folders in the window.

## Install
1. Install `PythonOpenModule` through Package Control 
1. Set up the `subl` command on your system (required to open new sublime windows for module directories)

## Virtual Environments
If you are using a virtual environment in your project, then set the `python_executable` in your project settings. This overrides the sys.path that is searched by the plugin.

For example:

    {
		"settings": {
			"python_executable": "/Users/glen/.virtualenvs/monty/bin/python"
		}
	}

## Usage
After opening the input panel (by either "Open Python module" under the File menu, or a keyboard shortcut, type the package name (e.g. `decimal` or `logging.config`) into the input panel and press enter.
