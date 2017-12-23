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

from utils import sort, error


ABS_PATH = path.dirname(path.abspath(__file__))
DB_FILE = path.realpath(path.join(ABS_PATH, "../data.json"))


with open(DB_FILE, 'r') as db_obj:
    data = json.load(db_obj, object_pairs_hook=OrderedDict)

keys = list(data.keys())
ordreded_keys = sort(keys)
has_errors = False

for i in range(len(keys)):
    if keys[i] != ordreded_keys[i]:
        correct_position = ordreded_keys.index(keys[i])
        has_errors = True
        error("Database entry {} not correctly "
              "ordred".format(keys[i]))
        print("Should be placed at {} instead "
              "of {}".format(correct_position, i))


for key, value in data.items():
    if value.get("linux"):
        symlinks = value["linux"].get("symlinks")
        if symlinks:
            ordered_symlinks = sort(symlinks)
            for i in range(len(symlinks)):
                if symlinks[i] != ordered_symlinks[i]:
                    has_errors = True
                    error("Linux symlink of \"{}\" not correctly "
                          "ordered: {}".format(key, symlinks[i]))
    if value.get("android"):
        android_icons = value["android"]
        ordered_and_icons = sort(android_icons)
        for i in range(len(android_icons)):
            if android_icons[i] != ordered_and_icons[i]:
                has_errors = True
                error("Android Icon \"{}\" not correctly "
                      "ordered".format(android_icons[i]))
exit(int(has_errors))
