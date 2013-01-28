# Sublime Text Spec Runner

Adds commands for running specs in iTerm that can be hooked into with key bindings.

Currently, this is only set up to work with iTerm through an AppleScript, so it's OSX only.

## Setup

Add SpecRunner directory to your Packages directory (Preferences > Browse Packages).

Create key bindings. The following commands are available:

- run_all_specs
- run_local_specs
- run_specific_specs
- debug_all_specs
- debug_local_specs
- debug_specific_specs
- rerun_last_specs

Use them like so in your user key bindings config:

    { "keys": ["super+alt+ctrl+y"], "command": "run_all_specs" },
    { "keys": ["super+alt+ctrl+u"], "command": "run_local_specs" },
    { "keys": ["super+alt+ctrl+i"], "command": "run_specific_specs" },
    { "keys": ["super+alt+ctrl+h"], "command": "debug_all_specs" },
    { "keys": ["super+alt+ctrl+j"], "command": "debug_local_specs" },
    { "keys": ["super+alt+ctrl+k"], "command": "debug_specific_specs" },
    { "keys": ["super+alt+ctrl+l"], "command": "rerun_last_specs" }