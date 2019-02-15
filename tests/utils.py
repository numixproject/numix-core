#!/usr/bin/env python3

"""
Copyright (C) 2019 Numix Project
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 3+) as
published by the Free Software Foundation. You should have received
a copy of the GNU General Public License along with this program.
If not, see <http://www.gnu.org/licenses/>.
"""

# list of themes to test
THEMES = ["circle", "square"]


def error(msg):
    """Print an error msg: Red color."""
    print("\033[91m{}\033[0m".format(msg))


def success(msg):
    """Print a success msg: Green color."""
    print("\033[92m{}\033[0m".format(msg))


def space_check(string):
    """Checks if a string contains an empty space."""
    if " " in string:
        error("'{}' contains an empty space".format(string))
        return True
    else:
        return False


def sort_check(list, stype, root=""):
    """
    Checks if a list of 'stype' strings is sorted, case insensitive. Takes as
    optional string 'root' as a root value for use with sublists.
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
