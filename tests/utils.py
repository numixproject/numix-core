#!/usr/bin/env python3
"""
# Copyright (C) 2016
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License (version 3+) as
# published by the Free Software Foundation. You should have received
# a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.
"""


def sort(icons_list):
    """Sort list case insensitive."""
    return sorted(icons_list,
                  key=lambda icon_name: icon_name.lower())


def error(msg):
    """Print an error msg: Red color."""
    print("\033[91m{}\033[0m".format(msg))


def success(msg):
    """Print a success msg: Green color."""
    print("\033[92m{}\033[0m".format(msg))
