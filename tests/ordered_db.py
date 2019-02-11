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
from os import path

from utils import error, sort_check


ABS_PATH = path.dirname(path.abspath(__file__))
DB_FILE = path.realpath(path.join(ABS_PATH, "../data.json"))

with open(DB_FILE, 'r') as db_obj:
    data = load(db_obj, object_pairs_hook=OrderedDict)

has_errors = sort_check(list(data.keys()), "Database entry")

for key, value in data.items():
    if value.get("android"):
        has_errors = sort_check(value["android"], "Android icon")

    if value.get("linux"):
        symlinks = value["linux"].get("symlinks")
        if not symlinks:
            continue
        has_errors = sort_check(symlinks, "Linux symlink", key)

    if value.get("osx"):
        has_errors = sort_check(value["osx"], "OSX icon")

exit(has_errors)
