# About

>- Notepad++ [web](https://notepad-plus-plus.org/)
>- download [page](https://notepad-plus-plus.org/downloads/)


# Notepad++ editor configuration

1. EDITOR variable
Setting the EDITOR environment variable points to the default text editor. Thanks to this setting,
calling the `ipython` magic function `%edit` (alias `%ed`) will run the indicated text etior.

Windows:
 - open system settings
 - click the Advanced system settings link
 - click `Environment Variables`, click `New`
 - in the `Variable name` box, enter: `EDITOR`
 - in the `Variable value` box, enter the path to the executable file: notepad.exe, e.g. `C:/Program Files/Notepad++/notepad++.exe` 


On Linux:
 - edit your `~/.bashrc` (or `~./profile`) file
 - add line: `export EDITOR=notepad++`
---


# Settings
 - menu `Language` -> `Python`
 - menu `Preferences` -> `New Document` -> `Default Language` -> `Python`
 - menu `Preferences` -> `New Document` -> `Encoding` -> `UTF-8`
 - menu `Preferences` -> `Language` -> `Tab Settings` -> `Tab Size`: 4
 - menu `Preferences` -> `Language` -> `Tab Settings` -> `Replace by space`
