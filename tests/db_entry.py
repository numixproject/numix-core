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

from utils import error, success, DB_FILE, ICONS_DIR, THEMES

# Test which checks whether every key in data.json has an icon in
# the themes which Core supports. Success signified by exit code.


with open(DB_FILE, 'r') as db_obj:
    data = load(db_obj)

has_errors = False
for entry in data:
    for theme in THEMES:
        icon = path.join(ICONS_DIR, theme, "48/{}.svg".format(entry))
        if path.exists(icon):
            continue

        has_errors = True
        error("'{}' doesn't have an icon in the {} theme".format(entry, theme))

if not has_errors:
    success("Every database entry has an icon")

exit(has_errors)
