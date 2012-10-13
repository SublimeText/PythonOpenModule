import sublime
import sublime_plugin
import sys
import imp
import subprocess


class PythonOpenModule(sublime_plugin.WindowCommand):

    # imp.find_module for dotted module names
    def find_module(self, module, path):
        parts = module.split(".")
        result = imp.find_module(parts[0], path)
        if len(parts) > 1:
            return self.find_module(".".join(parts[1:]), [result[1]])
        else:
            return result

    @property
    def subl_command(self):
        if sublime.platform() == 'windows':
            return 'sublime_text'
        else:
            return 'subl'

    """
    shell out to user's python and get their sys.path.
    use a virtualenv python executable, if the user specified 
    a virtual environment in the python_virtualenv setting.
    include any open folders on the syspath
    """
    def get_user_syspath(self):

        active_view = self.window.active_view()

        # can only obtain user settings from a view for some reason
        if active_view:
            # if the user has a python_executable in their project settings, use that
            # otherwise use `python`
            python_executable = active_view.settings().get('python_executable', 'python')
        # can't determine user settings, so use `python`
        else:
            python_executable = 'python'

        try:
            # try to get sys.path from the python executable
            args = [python_executable, '-c', 'import sys; print sys.path']
            sys_path_str = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]
            sys_path_str = sys_path_str.strip()
            sys_path = eval(sys_path_str)
        except OSError:
            # use sublime's sys.path instead
            sys_path = sys.path
        
        # add paths for any currently open folders
        sys_path.extend(self.window.folders())
        return sys_path

    def on_done(self, text):
        sys_path = self.get_user_syspath()
        try:
            module = self.find_module(text, sys_path)
            if module[2][2] == imp.PY_SOURCE:
                self.window.open_file(module[1])
            elif module[2][2] == imp.PKG_DIRECTORY:
                try:
                    # open module's directory and __init__.py in new sublime window
                    # sublime API does not currently allow opening directories
                    subprocess.Popen([self.subl_command, module[1], '%s/__init__.py' % module[1]])
                except OSError:
                    sublime.error_message('Could not open directory %s.\n\n'
                        'Add `%s` to your path to open module directories' % (module[1], self.subl_command))
            else:
                sublime.error_message('Could not open module %s' % module[1])
        except ImportError:
            sublime.error_message('Could not find module %s' % text)

    def run(self):
        self.window.show_input_panel("Python module on sys.path:", "", self.on_done, None, None)
