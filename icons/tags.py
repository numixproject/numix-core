#!/usr/bin/env python3

"""
Copyright (C) 2021 Numix Project
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 3+) as
published by the Free Software Foundation. You should have received
a copy of the GNU General Public License along with this program.
If not, see <http://www.gnu.org/licenses/>.
"""

# Sorting out modules
from argparse import ArgumentParser
from json import load
from os import listdir, makedirs, path
from shutil import copy2, rmtree

# Used for viewing all the icon files across all themes that have a
# certain tag. Can be used either for related icons (e.g. ms-office,
# icons using the same design element (e.g. world-baseplate), etc.


def mkdir(directory):
    """Create a directory if it doesn't exists."""
    if not path.exists(directory):
        makedirs(directory)


# Parse arguments
parser = ArgumentParser(prog="Core Tag Viewer")
parser.add_argument("--tag", "-t", help="Tag you want to view.")
parser.add_argument("--clean", "-c", action="store_true",
                    help="Delete all tag outputs.")
args = parser.parse_args()

# Cleanup first if `--clean` passed
if args.clean:
    for dir in listdir("./"):
        if "tag." in dir:
            rmtree(dir)
    # If `--clean` run alone, done
    if not args.tag:
        exit(0)

# Check `--tag` used correctly
if not args.tag:
    exit("Please specify a tag using --tag")
else:
    tag = args.tag

# Exclude files and tag directories from the list of themes
themes = [dir for dir in listdir("./") if "." not in dir]

# Make folder and subfolders for tag location
for theme in themes:
    if "." not in theme:
        mkdir("tag.{0}/{1}".format(tag, theme))

# Loading the JSON data file
try:
    with open("../data.json") as data:
        icons = load(data)
except FileNotFoundError:
    exit("Couldn't find data.json!")

# iterate over data.json looking for keys with tag
for icon_name, icon in icons.items():
    if tag in icon.get("tags", []):
        for theme in themes:
            # Check icon source exists before it's used
            source = "{0}/48/{1}.svg".format(theme, icon_name)
            if not path.exists(source):
                continue
            # Copy icons for tagged keys into output directory
            copy2(source, "tag.{0}/{1}".format(tag, theme))

# Clean Up
print("Done!")
