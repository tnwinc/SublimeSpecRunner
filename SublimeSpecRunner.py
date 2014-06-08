import sublime
import sublime_plugin
import re

def applescriptPath():
    return sublime.packages_path() + "/SublimeSpecRunner/sendCommand.scpt"

def get_file_path(full_path):
    file_match = re.match('^\/(.+\/)*(.+)\.(.+)$', full_path)
    return '/' + file_match.group(1)

def run_script(view, scriptArgs):
    view.window().run_command("exec", {
        "cmd": ["osascript", applescriptPath()] + scriptArgs
    })


class RunAllSpecs(sublime_plugin.TextCommand):
    def run(self, edit):
        run_script(self.view, [
            "spec_all",
            "setopt NULL_GLOB; cd " + get_file_path(self.view.file_name()) + "; clear; rake test reporter=progress"
        ])


class RunLocalSpecs(sublime_plugin.TextCommand):
    def run(self, edit):
        run_script(self.view, [
            "specs_local",
            "setopt NULL_GLOB; cd " + get_file_path(self.view.file_name()) + "; clear; rake test reporter=spec " + get_file_path(self.view.file_name()) + "*.spec.js " + get_file_path(self.view.file_name()) + "*/*.spec.js"
        ])


class RunSpecificSpecs(sublime_plugin.TextCommand):
    def run(self, edit):
        run_script(self.view, [
            "specs_local",
            "setopt NULL_GLOB; cd " + get_file_path(self.view.file_name()) + "; clear; rake test reporter=spec " + self.view.file_name()
        ])


class DebugAllSpecs(sublime_plugin.TextCommand):
    def run(self, edit):
        run_script(self.view, [
            "spec_all",
            "setopt NULL_GLOB; cd " + get_file_path(self.view.file_name()) + "; clear; rake test debug=true;",
            "focus"
        ])


class DebugLocalSpecs(sublime_plugin.TextCommand):
    def run(self, edit):
        run_script(self.view, [
            "specs_local",
            "setopt NULL_GLOB; cd " + get_file_path(self.view.file_name()) + "; clear; rake test debug=true " + get_file_path(self.view.file_name()) + "*.spec.js " + get_file_path(self.view.file_name()) + "*/*.spec.js",
            "focus"
        ])


class DebugSpecificSpecs(sublime_plugin.TextCommand):
    def run(self, edit):
        run_script(self.view, [
            "specs_local",
            "setopt NULL_GLOB; cd " + get_file_path(self.view.file_name()) + "; clear; rake test debug=true " + self.view.file_name(),
            "focus"
        ])


class RerunLastSpecs(sublime_plugin.TextCommand):
    def run(self, edit):
        run_script(self.view, [
            "specs_local",
            "setopt NULL_GLOB; cd " + get_file_path(self.view.file_name()) + "; clear; rake test rerun=true"
        ])
