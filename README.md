# Python Open Module
This plugin will open a python module file present on sys.path and any open folders in the window

After opening, type the package name (e.g. `decimal` or `logging.config`) into the input panel and press enter.

## Notes:
*   If `python` exists on the user path, it's sys.path is used
*   Otherwise it will fallback to a search on sublime's python sys.path
