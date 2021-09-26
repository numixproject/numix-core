#!/usr/bin/env python3

"""
Copyright (C) 2019 Numix Project
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 3+) as
published by the Free Software Foundation. You should have received
a copy of the GNU General Public License along with this program.
If not, see <http://www.gnu.org/licenses/>.
"""

from os import path

# Functions and variables which are used across the tests, defined
# here so as not to be duplicated.


# list of paths the tests need
ABS_PATH = path.dirname(path.abspath(__file__))
DB_FILE = path.join(ABS_PATH, "../data.json")
ICONS_DIR = path.join(ABS_PATH, "../icons/")
SCHEMA_FILE = path.join(ABS_PATH, 'schema.json')

# list of themes to test
THEMES = ["circle", "square"]


def error(msg):
    """Print an error msg: Red color."""
    print("\033[91m{}\033[0m".format(msg))


def success(msg):
    """Print a success msg: Green color."""
    print("\033[92m{}\033[0m".format(msg))
