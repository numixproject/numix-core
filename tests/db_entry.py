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

from utils import error, THEMES

ABS_PATH = path.dirname(path.abspath(__file__))
DB_FILE = path.join(ABS_PATH, "../data.json")
ICONS_DIR = path.join(ABS_PATH, "../icons/")

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

exit(has_errors)
