#!/usr/bin/env python3

"""
Copyright (C) 2019 Numix Project
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 3+) as
published by the Free Software Foundation. You should have received
a copy of the GNU General Public License along with this program.
If not, see <http://www.gnu.org/licenses/>.
"""

from glob import glob
from json import load
from os import path

from utils import error, THEMES

ABS_PATH = path.dirname(path.abspath(__file__))
DB_FILE = path.join(ABS_PATH, "../data.json")
ICONS_DIR = path.join(ABS_PATH, "../icons/")

with open(DB_FILE, 'r') as db_obj:
    entries = load(db_obj).keys()

has_errors = False
reported = []
for theme in THEMES:
    icons = glob(path.join(ICONS_DIR, theme, "48") + "/*.svg")
    for icon in icons:
        icon_name = path.splitext(path.basename(icon))[0]
        if icon_name in entries or icon_name in reported:
            continue

        reported.append(icon_name)
        has_errors = True
        error("'{}' doesn't have an entry in the database.".format(icon_name))

exit(has_errors)
