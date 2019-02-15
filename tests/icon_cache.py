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
from collections import OrderedDict

from utils import error

ABS_PATH = path.dirname(path.abspath(__file__))
DB_FILE = path.join(ABS_PATH, "../data.json")

with open(DB_FILE, 'r') as db_obj:
    data = json.load(db_obj, object_pairs_hook=OrderedDict)

has_errors = False


def test_empty_space(icon_name):
    """Test if an icon name has an empty space on it."""
    global has_errors
    if " " in icon_name:
        has_errors = True
        error("{} contains an empty space on it".format(icon_name))


for key, value in data.items():
    if value.get("linux"):
        icon = data[key]["linux"]
        test_empty_space(icon["root"])
        if icon.get("symlinks"):
            symlinks = icon["symlinks"]
            for symlink in symlinks:
                test_empty_space(symlink)
exit(int(has_errors))
