#!/usr/bin/python3

# Copyright (C) 2016
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License (version 3+) as
# published by the Free Software Foundation. You should have received
# a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

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
         ", ".join(themes))
else:
    theme = args.theme

# User selects the platform
if not args.platform:
    exit("Please use --platform argument with one of the following: " +
         ", ".join(platforms))
else:
    platform = args.platform


def mkdir(dir):
    if not path.exists(dir):
        makedirs(dir)


def convert_svg2png(infile, outfile, w, h):
    """
        Converts svg files to png using Cairosvg or Inkscape
        @file_path : String; the svg file absolute path
        @dest_path : String; the png file absolute path
    """
    if use_inkscape:
        p = Popen(["inkscape", "-z", "-f", infile, "-e", outfile,
                   "-w", str(w), "-h", str(h)],
                  stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
    else:
        handle = Rsvg.Handle()
        svg = handle.new_from_file(infile)
        dim = svg.get_dimensions()

        img = ImageSurface(FORMAT_ARGB32, w, h)
        ctx = Context(img)
        ctx.scale(w / dim.width, h / dim.height)
        svg.render_cairo(ctx)

        png_io = BytesIO()
        img.write_to_png(png_io)
        with open(outfile, 'wb') as fout:
            fout.write(png_io.getvalue())
        svg.close()
        png_io.close()
        img.finish()


# Only certain icon sizes may be covered
try:
    sizes = listdir(path.join("icons", theme))
except FileNotFoundError:
    exit("The theme {0} does not exists. Please reclone" 
        "the repository and try again.".format(theme))


# The Generation Stuff
if platform == "android":
    print("\nGenerating Android theme...")
    android_dir = path.join("com.numix.icons_{0}".format(theme), "MainActivity22", "app", "src", "main", "res", "drawable-xxhdpi")
    mkdir(android_dir)
    for icon in icons:
        for name in icons[icon].get("android", []):
            name = name.replace("_", ".")
            source = path.join("icons", theme, "48", "{0}.svg".format(icon))
            output = path.join(android_dir, "{0}.png".format(name))
            if path.exists(source):
                convert_svg2png(source, output, 192, 192)
elif platform == "linux":
    print("\nGenerating Linux theme...")
    linux_dir = path.join("numix-icon-theme-{0}".format(theme), "Numix-{0}".format(theme.title()))
    for size in sizes:
        mkdir(path.join(linux_dir, size, "apps"))
    for icon in icons:
        if "linux" in icons[icon].keys():
            for size in sizes:
                root = "{0}.svg".format(icons[icon]["linux"]["root"])
                source = path.join("icons", theme, size, "{0}.svg".format(icon))
                output = path.join(linux_dir, size, "apps", root)
                if path.exists(source):
                    if "bfb" in icons[icon]["linux"].keys():
                        output_bfb = path.join(linux_dir, size, "apps", "{0}.png".format(icons[icon]["linux"]["bfb"]))
                        if int(size) == 48:
                            convert_svg2png(source, output_bfb, 144, 144)
                    copy2(source, output)
                    for link in icons[icon]["linux"].get("symlinks", []):
                        output_symlink = path.join(linux_dir, size, "apps", "{0}.svg".format(link))
                        try:
                            symlink(root, output_symlink)
                        except FileExistsError:
                            continue
elif platform == "osx":
    print("\nGenerating OSX theme...")
    ink_flag = call(['which', 'png2icns'], stdout=PIPE, stderr=PIPE)
    if ink_flag != 0:
        exit("You will need png2icns in order to generate OSX theme")
    osx_dir = path.join("numix-{0}.icns".format(theme), "")
    osx_sub_dirs = ["icns", "pngs", "vectors"]
    for sub_dir in osx_sub_dirs:
        mkdir(path.join(osx_dir, sub_dir, "")) 
    for icon in icons:
        for name in icons[icon].get("osx", []):
            source = path.join("icons", theme, "48", "{0}.svg".format(icon))
            output_svg = path.join(osx_dir, "vectors", "{0}.svg".format(icon))
            output_png = path.join(osx_dir, "pngs", "{0}.png".format(icon))
            output_icn = path.join(osx_dir, "icns", "{0}.icn".format(icon))
            if path.exists(source):
                copy2(source, output_svg)
                convert_svg2png(source, output_png, 1024, 1024)
                call(["png2icns", output_icn, output_png], stdout=PIPE, stderr=PIPE)
# Clean Up
exit("Done!\n")
