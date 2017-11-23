#!/usr/bin/env python3
"""
# Copyright (C) 2016
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License (version 3+) as
# published by the Free Software Foundation. You should have received
# a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.
"""
from glob import glob
from os import path
import json

ABS_PATH = path.dirname(path.abspath(__file__))
DB_FILE = path.join(ABS_PATH, "../data.json")
THEMES = ["circle", "square"]
ICONS_DIR = path.join(ABS_PATH, "../icons/")


has_errors = False
with open(DB_FILE, 'r') as db_obj:
    entries = json.load(db_obj).keys()

reported = []
for theme in THEMES:
    icons = glob(path.join(ICONS_DIR, theme, "48") + "/*.svg")
    for icon in icons:
        icon_name = path.splitext(path.basename(icon))[0]
        if icon_name not in entries and icon_name not in reported:
            reported.append(icon_name)
            has_errors = True
            print("\033[91m The icon {} doesn't have any entry in the database \033[0m".format(
                icon_name
            ))
exit(int(has_errors))