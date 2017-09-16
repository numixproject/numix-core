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
from glob import glob
from subprocess import call
from tempfile import NamedTemporaryFile


ABSOLUTE_PATH = path.dirname(path.realpath(__file__))

TEMPLATES = glob(path.join(ABSOLUTE_PATH, "../templates/**/*.svg"))
ICONS = glob(path.join(ABSOLUTE_PATH, "../icons/**/**/*.svg"))

SVG_FILES = sorted(TEMPLATES + ICONS)


def scour_optimize(icon_path):
    """Optimise an SVG icon using scour."""
    tmp_icon = NamedTemporaryFile()
    output_file = tmp_icon.name + ".svg"
    scour_options = ["scour", "-i", icon_path, "-o", output_file]
    # Disable convert CSS attributes to XML attributes
    scour_options.append("--disable-style-to-xml")
    # Create groupe for similar attributes
    scour_options.append("--create-groups")
    # Work around renderer bugs
    scour_options.append("--renderer-workaround")
    # Remove the XML declaration
    scour_options.append("--strip-xml-prolog")
    # Remove comments
    scour_options.append("--enable-comment-stripping")
    # Remove metadata, title and desc
    scour_options.append("--remove-descriptive-elements")
    # Remove unused ID's
    scour_options.append("--enable-id-stripping")
    # Preserve Manually created IDs not ending with digits
    scour_options.append("--protect-ids-noninkscape")
    call(scour_options)
    return output_file


def is_optimized(icon_path):
    """Verify if an icon was optimized using Scour."""
    optimized_icon = scour_optimize(icon_path)
    with open(optimized_icon, 'r') as optimized_obj:
        optimized_data = optimized_obj.read()
    with open(icon_path, 'r') as icon_obj:
        icon_data = icon_obj.read()
    return icon_data == optimized_data

for icon in SVG_FILES:
    icon_name = path.sep.join(icon.split(path.sep)[-3:])
    if is_optimized(icon):
        print("\033[92m - {} is optimized\033[0m".format(icon_name))
    else:
        print("\033[91m - {} should be optimized \033[0m".format(icon_name))
