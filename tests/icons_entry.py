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

from utils import error, success, THEMES, DB_FILE, ICONS_DIR

# Test to check whether every icon in the themes which core support have
# associed entries in the data.json file Success signified by exit code.


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

if not has_errors:
    success("Every icon has a database entry")

exit(has_errors)
