#!/usr/bin/env python3
"""
# Copyright (C) 2016
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License (version 3+) as
# published by the Free Software Foundation. You should have received
# a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.
"""

from os import path
import json

from utils import error

ABS_PATH = path.dirname(path.abspath(__file__))
DB_FILE = path.join(ABS_PATH, "../data.json")
THEMES = ["circle", "square"]
ICONS_DIR = path.join(ABS_PATH, "../icons/")


has_errors = False
with open(DB_FILE, 'r') as db_obj:
    data = json.load(db_obj)
    for entry in data:
        for theme in THEMES:
            icon = path.join(ICONS_DIR, theme, "48/{}.svg".format(entry))
            if not path.exists(icon):
                has_errors = True
                error("The icon {} doesn't exist"
                      " in the theme {}".format(
                          entry, theme
                      ))
exit(int(has_errors))
