# Log Viewer for Logback Style JSON Formatted Logs

## Usage

After loading a JSON formatted file, the right click should display the `View Log` menu item.

It is possible to show/hide or highlight lines with particular severity.
It is also possible to show/hide particular columns.

Lines that are not JSON are displayed as they are.

All log levels are visible and no highlight is applied by default. You can show/hide, add or remove particular columns
by editing the `LogbackJsonLogViewer.sublime-settings` configuration file.

### Log Levels

You can toggle log levels using numerical keys:

| Key | Log Level |
|-----|-----------|
| `1` | DEBUG     |
| `2` | INFO      |
| `3` | WARN      |
| `4` | ERROR     |

### Columns

You can toggle pre-defined columns using numerical keys:

| Key | Column     |
|-----|------------|
| `1` | @timestamp |
| `2` | severity   |
| `3` | service    |
| `4` | trace      |
| `5` | span       |
| `6` | thread     |
| `7` | class      |
| `8` | msg        |
| `9` | version    |

### Windows/Linux

* `super + 1..4` - Show or hide the lines with a particular log level (1 - DEBUG, 2 - INFO, 3 - WARN, 4 - ERROR).
* `alt + 1..4` - Toggle highlight for log level.
* `ctrl + 1..9` - Toggle visibility for a particular column.

### MacOS

* `⌘ + 1..4` - Show or hide the lines with a particular log level (1 - DEBUG, 2 - INFO, 3 - WARN, 4 - ERROR).
* `option + 1..4` - Toggle highlight for log level.
* `ctrl + 1..9` - Toggle visibility for a particular column.

## Installation

**Without Git:** Download the latest source from [GitHub](https://github.com/neno--/LogbackJsonLogViewer) and copy the whole directory into
the `Packages` directory.

**With Git:** Clone the repository in your Sublime Text directory, located somewhere in the user's `Home` directory:

    `git clone git@github.com:neno--/LogbackJsonLogViewer.git`

The `Packages` packages directory is located:

* Windows: `%APPDATA%/Sublime Text/Packages/`
* Linux: `~/.Sublime Text/Packages/`
* OS X: `~/Library/Application Support/Sublime Text/Packages/`