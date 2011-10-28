import sublime, sublime_plugin, json

class PrettyjsonCommand(sublime_plugin.TextCommand):
    def run(self, edit): 
        view = self.view
        for region in view.sel():
            if not region.empty():
                s = view.substr(region).encode('utf-8')
                s = json.loads(s)
                s = json.dumps(s, sort_keys=True, indent=4)
                view.replace(edit, region, s)