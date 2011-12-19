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

    # shell out to user's python and get their sys.path
    # include any open folders on the syspath
    def get_user_syspath(self):
        try:
            # try to get sys.path from python on user path
            args = ['python', '-c', 'import sys; print sys.path']
            sys_path = eval(subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0])
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
        except ImportError:
            pass

    def run(self):
        self.window.show_input_panel("Python module on sys.path:", "", self.on_done, None, None)
