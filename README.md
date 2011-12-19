This plugin will try to open a python module file on sys.path and any of the open folders in the window

Notes:
- If `python` exists on the user path, it's sys.path is used
- Otherwise it will fallback to a search on sublime's python sys.path
