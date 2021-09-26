#!/usr/bin/env python3

"""
Copyright (C) 2019 Numix Project
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 3+) as
published by the Free Software Foundation. You should have received
a copy of the GNU General Public License along with this program.
If not, see <http://www.gnu.org/licenses/>.
"""

from collections import OrderedDict
from json import load

from utils import error, success, DB_FILE

# Test which checks whether the data.json file is sorted by key and
# any lists within those keys. Success signified by exit code.


def sort_errors(list, stype, root=""):
    """
    Checks if a list of 'stype' strings has sorting errors, case insensitive.
    Takes as optional string 'root' as a root value for use with sublists.
    """
    has_errors = False
    reference = sorted(list, key=lambda item: item.lower())

    for i in range(len(list)):
        if list[i] == reference[i]:
            continue

        correct_index = reference.index(list[i])
        has_errors = True

        if root == "":
            error_msg = "{} '{}' not correctly ordred"
        else:
            error_msg = "{} '{}' of '{}' not correctly ordred"

        error(error_msg.format(stype, list[i], root))
        print("Should be placed at {} instead of {}".format(correct_index, i))

    return has_errors


with open(DB_FILE, 'r') as db_obj:
    data = load(db_obj, object_pairs_hook=OrderedDict)

has_errors = sort_errors(list(data.keys()), "Database entry")

for key, value in data.items():
    if value.get("android") and sort_errors(value["android"], "Android icon"):
        has_errors = True

    if value.get("linux"):
        symlinks = value["linux"].get("symlinks")
        if symlinks and sort_errors(symlinks, "Linux symlink", key):
            has_errors = True

    if value.get("osx") and sort_errors(value["osx"], "OSX icon"):
        has_errors = True

    if value.get("tags") and sort_errors(value["tags"], "Icon tag"):
        has_errors = True

if not has_errors:
    success("Database is properly sorted")

exit(has_errors)
