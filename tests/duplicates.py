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

# Test which checks for duplicates across all the Linux root icons
# and symlinks. Success signified by exit code.


with open(DB_FILE, 'r') as db_obj:
    data = load(db_obj)

linux_names = []
for key, value in data.items():
    # At the moment we're only concerned with Linux duplicates
    if not value.get("linux"):
        continue

    icon = data[key]["linux"]
    linux_names.append(icon["root"])

    if data[key]["linux"].get("symlinks"):
        linux_names += icon["symlinks"]

has_linux_dupes = False

linux_dupes = {}
for name in linux_names:
    if linux_names.count(name) > 1:
        linux_dupes[name] = linux_names.count(name)

if len(linux_dupes) > 0:
    has_linux_dupes = True
    error("Found the following Linux icon names duplicated:")
    for dupe in sorted(linux_dupes.keys()):
        error("- {} ({} times)".format(dupe, linux_dupes[dupe]))
else:
    success("No database duplicates")

exit(has_linux_dupes)
