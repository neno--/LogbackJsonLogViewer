import json

import sublime
import sublime_plugin


def display_log(self):
  lines = []
  for parsed_line in self.settings().get("parsed_log"):
    if isinstance(parsed_line, str):
      lines.append(parsed_line)
      line = parsed_line
      self.run_command('append', {"characters": line + "\n"})
    else:
      log_level = parsed_line['severity']
      if self.settings().get("log_settings")["severity"][log_level]["visible"]:
        line = log_line(parsed_line,
                        self.settings().get("log_settings")["columns"])
        if parsed_line["stacktrace"] and self.settings().get("log_settings")[
          "stacktrace_visible"]:
          line += "\n" + parsed_line["stacktrace"]

        if self.settings().get("log_settings")["severity"][log_level][
          "highlight"]:
          current_regions = self.get_regions(log_level)
          begin = self.size()
          self.run_command('append', {"characters": line + "\n"})
          new_region = sublime.Region(begin, self.size())
          self.add_regions(log_level, current_regions + [new_region],
                           self.settings().get("log_settings")["severity"][
                             log_level][
                             "color"])
        else:
          self.run_command('append', {"characters": line + "\n"})


def log_line(parsed_line, columns):
  line = ""
  first = True

  for column in columns:
    value = parsed_line[column["name"]]
    if column["visible"] and (len(value.strip()) > 0):
      line += ("" if first else " ") + value
      first = False

  return line


class ViewLogCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    new_view = self.view.window().new_file()
    new_view.settings().set("parsed_log", self.parse_log(
        self.view.substr(sublime.Region(0, len(self.view)))))
    new_view.settings().set("is_log", True)
    settings = sublime.load_settings('LogbackJsonLogViewer.sublime-settings')
    log_settings = {
      "columns": settings.get("columns"),
      "stacktrace_visible": settings.get("stacktraceVisible"),
      "severity": settings.get("severity"),
    }
    new_view.settings().set("log_settings", log_settings)
    display_log(new_view)

  def parse_log(self, file_content):
    lines = []
    for line in file_content.split('\n'):
      try:
        lines.append(json.loads(line))
      except ValueError:
        lines.append(str(line))
    return lines


class UpdateSeveritySettingsCommand(sublime_plugin.TextCommand):
  def run(self, edit, log_level, log_operation):
    log_settings = self.view.settings().get("log_settings")
    log_settings["severity"][log_level][log_operation] = not \
      log_settings["severity"][log_level][
        log_operation]
    self.view.settings().set("log_settings", log_settings)

    self.view.erase(edit, sublime.Region(0, self.view.size()))
    display_log(self.view)


class UpdateColumnSettingsCommand(sublime_plugin.TextCommand):
  def run(self, edit, column_index):
    log_settings = self.view.settings().get("log_settings")
    log_settings["columns"][column_index]["visible"] = not \
      log_settings["columns"][column_index]["visible"]
    self.view.settings().set("log_settings", log_settings)

    self.view.erase(edit, sublime.Region(0, self.view.size()))
    display_log(self.view)


class LogbackJsonLogViewerOpenDefaultSettingsCommand(
    sublime_plugin.WindowCommand):
  def run(self):
    self.window.run_command(
        'open_file',
        {
          "file": "${packages}/LogbackJsonLogViewer/LogbackJsonLogViewer.sublime-settings"
        }
    )


class LogbackJsonLogViewerOpenUserSettingsCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.run_command(
        'open_file',
        {
          "file": "${packages}/User/LogbackJsonLogViewer.sublime-settings",
          "contents":
            "// See Preferences > Package Settings > LogbackJsonLogViewer > Settings - Default\n"
            "// for the list of settings and valid values\n"
            "{\n"
            "\t$0\n"
            "}\n"
        }
    )


class LogbackJsonLogViewerEditSettingsCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.run_command(
        'edit_settings',
        {
          "base_file": "${packages}/LogbackJsonLogViewer/LogbackJsonLogViewer.sublime-settings",
          "default":
            "// See the left pane for the list of settings and valid values\n"
            "{\n"
            "\t$0\n"
            "}\n"
        }
    )
