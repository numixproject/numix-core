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

from utils import error, success, DB_FILE

# Test which checks whether the Linux icon cache would be valid for
# the given data.json file. Success signified by exit code.


def space_check(string):
    """Checks if a string contains an empty space."""
    if " " in string:
        error("'{}' contains an empty space".format(string))
        return True
    else:
        return False


with open(DB_FILE, 'r') as db_obj:
    data = load(db_obj)

has_errors = False
for key, value in data.items():
    if not value.get("linux"):
        continue

    icon = data[key]["linux"]
    if space_check(icon["root"]):
        has_errors = True

    if not icon.get("symlinks"):
        continue

    symlinks = icon["symlinks"]
    for symlink in symlinks:
        if space_check(symlink):
            has_errors = True

if not has_errors:
    success("Icon cache is valid")

exit(has_errors)
