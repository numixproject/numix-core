#!/usr/bin/env python3

"""
Copyright (C) 2019 Numix Project
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 3+) as
published by the Free Software Foundation. You should have received
a copy of the GNU General Public License along with this program.
If not, see <http://www.gnu.org/licenses/>.
"""

from json import load
from os import path

from utils import error, space_check


ABS_PATH = path.dirname(path.abspath(__file__))
DB_FILE = path.join(ABS_PATH, "../data.json")

with open(DB_FILE, 'r') as db_obj:
    data = load(db_obj)

has_errors = False
for key, value in data.items():
    if not value.get("linux"):
        continue

    icon = data[key]["linux"]
    has_errors = space_check(icon["root"])

    if not icon.get("symlinks"):
        continue

    symlinks = icon["symlinks"]
    for symlink in symlinks:
        has_errors = space_check(symlink)

exit(has_errors)
