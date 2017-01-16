#!/usr/bin/python3
# pylint: disable=C0103
"""
Copyright (C) 2016
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 3+) as
published by the Free Software Foundation. You should have received
a copy of the GNU General Public License along with this program.
If not, see <http://www.gnu.org/licenses/>.
"""
# Sorting out modules
from argparse import ArgumentParser
from io import BytesIO
from json import load
from os import listdir, makedirs, path, symlink
from shutil import copy2, rmtree
from subprocess import PIPE, Popen, call
try:
    from gi import require_version
    require_version('Rsvg', '2.0')
    from gi.repository import Rsvg
    from cairo import ImageSurface, Context, FORMAT_ARGB32
    use_inkscape = False
except (ImportError, AttributeError, ValueError):
    ink_flag = call(['which', 'inkscape'], stdout=PIPE, stderr=PIPE)
    if ink_flag == 0:
        use_inkscape = True
    else:
        exit("Can't load cariosvg nor inkscape")


class PNG2IcnsNotInstalled(Exception):
    """Exception raised when png2icns is not installed."""

    def __init__(self):
        super(PNG2IcnsNotInstalled, self).__init__()


def mkdir(base_directory, sub_dirs=None):
    """Create a directory and subdirs."""
    try:
        if not sub_dirs:
            makedirs(base_directory)
        else:
            for sub_directory in sub_dirs:
                makedirs(path.join(base_directory, sub_directory))
    except FileExistsError:
        answer = input("The theme already exists."
                       "Would you like to rebuild it again? "
                       "Y[es], N[o]").strip().lower()
        if answer in ["y", "yes"]:
            rmtree(base_directory)
            mkdir(base_directory, sub_dirs)
        else:
            exit()


def convert_svg2png(infile, outfile, width, height):
    """
    Convert svg files to png using Cairosvg or Inkscape.

    @file_path : String; the svg file absolute path
    @dest_path : String; the png file absolute path
    """
    if use_inkscape:
        cmd = ["inkscape", "-z", "-f", infile, "-e", outfile,
               "-w", str(width), "-h", str(height)]
        Popen(cmd, stdout=PIPE, stderr=PIPE).communicate()
    else:
        handle = Rsvg.Handle()
        svg = handle.new_from_file(infile)
        dim = svg.get_dimensions()

        img = ImageSurface(FORMAT_ARGB32, width, height)
        ctx = Context(img)
        ctx.scale(width / dim.width, height / dim.height)
        svg.render_cairo(ctx)

        png_io = BytesIO()
        img.write_to_png(png_io)
        with open(outfile, 'wb') as fout:
            fout.write(png_io.getvalue())
        fout.close()
        svg.close()
        png_io.close()
        img.finish()


parser = ArgumentParser(prog="Numix-core")

# Importing JSON
try:
    with open('data.json') as data:
        icons = load(data)
except FileNotFoundError:
    exit("Please clone the whole repository and try again.")

try:
    theme, themes = "", listdir("icons")
    parser.add_argument("--theme", "-t",
                        help="Theme you want to build.", choices=themes)
except FileNotFoundError:
    exit("No icons folder found. Please reclone and try again.")

platform, platforms = "", ["android", "linux", "osx"]
parser.add_argument("--platform", "-p",
                    help="Platform you like to build the theme for.",
                    choices=platforms)

args = parser.parse_args()

# User selects the theme
if not args.theme:
    exit("Please use --theme argument with one of the following: " +
         ", ".join(themes) + "\n")
else:
    theme = args.theme

# User selects the platform
if not args.platform:
    exit("Please use --platform argument with one of the following: " +
         ", ".join(platforms) + "\n")
else:
    platform = args.platform


# Only certain icon sizes may be covered
try:
    sizes = listdir(path.join("icons", theme))
except FileNotFoundError:
    exit("The theme {0} does not exists.Please reclone" 
        "the repository and try again.".format(theme))


# The Generation Stuff
if platform == "android":
    print("\nGenerating Android theme...")
    android_dir = path.join("MainActivity22", "app", "src", "main", "res",
                            "drawable-xxhdpi", "com.numix.icons_{0}".format(theme))
    mkdir(android_dir)
    for icon in icons:
        for name in icons[icon].get("android", []):
            name = name.replace("_", ".")
            input_icon = path.join("icons", theme, "48",
                                   "{0}.svg".format(icon))
            output_icon = path.join(android_dir, "{0}.png".format(name))
            if path.exists(input_icon):
                convert_svg2png(input_icon, output_icon, 192, 192)
elif platform == "linux":
    print("\nGenerating Linux theme...")
    linux_dir = path.join(
        "numix-icon-theme-{0}".format(theme), "Numix-{0}".format(theme.title()), "")
    mkdir(linux_dir, [path.join(size, "apps") for size in sizes])
    for icon in icons:
        if "linux" in icons[icon].keys():
            for size in sizes:
                root_icon = "{0}.svg".format(icons[icon]["linux"]["root"])
                input_icon = path.join(
                    "icons", theme, size, "{0}.svg".format(icon))
                output_vector = path.join(linux_dir, size, "apps", root_icon)
                if path.exists(input_icon):
                    if "bfb" in icons[icon]["linux"].keys():
                        bfb_icon = "{0}.png".format(
                            icons[icon]["linux"]["bfb"])
                        output_bfb = path.join(
                            linux_dir, size, "apps", bfb_icon)
                        if int(size) == 48:
                            convert_svg2png(input_icon, output_bfb, 144, 144)
                    copy2(input_icon, output_vector)
                    for link in icons[icon]["linux"].get("symlinks", []):
                        link_path = path.join(
                            linux_dir, size, "apps", "{0}.svg".format(link))
                        try:
                            symlink(root_icon, link_path)
                        except FileExistsError:
                            continue
elif platform == "osx":
    print("\nGenerating OSX theme...")
    try:
        ink_flag = call(['which', 'png2icns'], stdout=PIPE, stderr=PIPE)
        if ink_flag != 0:
            raise PNG2IcnsNotInstalled
    except PNG2IcnsNotInstalled:
        exit("You will need png2icns in order to generate OSX theme")

    osx_dir = "numix-{0}.icns".format(theme)
    mkdir(osx_dir, ["icns", "pngs", "vectors"])
    for icon in icons:
        for name in icons[icon].get("osx", []):
            input_icon = path.join("icons", theme, "48",
                                   "{0}.svg".format(icon))
            output_vector = path.join(
                osx_dir, "vectors", "{0}.svg".format(name))
            output_png = path.join(osx_dir, "pngs", "{0}.png".format(name))
            output_icns = path.join(osx_dir, "icns", "{0}.icn".format(name))
            if path.exists(input_icon):
                copy2(input_icon, output_vector)
                convert_svg2png(input_icon, output_png, 1024, 1024)
                call(["png2icns", output_icns, output_png],
                     stdout=PIPE, stderr=PIPE)
# Clean Up
exit("Done!\n")
