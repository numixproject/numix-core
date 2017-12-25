#!/usr/bin/env python3
"""
# Copyright (C) 2016
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License (version 3+) as
# published by the Free Software Foundation. You should have received
# a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.
"""

# Sorting out modules
from argparse import ArgumentParser
from io import BytesIO
from json import load
from os import listdir, makedirs, path, symlink
from shutil import copy2
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
    exit("Please use --theme argument with "
         "one of the following: {}".format(", ".join(themes)))
else:
    theme = args.theme

# User selects the platform
if not args.platform:
    exit("Please use --platform argument with "
         "one of the following: {}".format(", ".join(platforms)))
else:
    platform = args.platform


def mkdir(directory):
    """Create a directory if it doesn't exists."""
    if not path.exists(directory):
        makedirs(directory)


def convert_svg2png(infile, outfile, w, h):
    """
        Converts svg files to png using Cairosvg or Inkscape
        @file_path : String; the svg file absolute path
        @dest_path : String; the png file absolute path
    """
    if use_inkscape:
        cmd = Popen(["inkscape", "-z", "-f", infile, "-e", outfile,
                     "-w", str(w), "-h", str(h)],
                    stdout=PIPE, stderr=PIPE)
        cmd.communicate()
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
    sizes = listdir("icons/{0}".format(theme))
except FileNotFoundError:
    exit("The theme {0} does not exists. Please reclone"
         "the repository and try again.".format(theme))


# The Generation Stuff
if platform == "android":
    print("\nGenerating Android theme...")
    theme_name = "com.numix.icons_{0}".format(theme)
    android_dir = theme_name + "/MainActivity22/app/src/main/res/"
    app_filter = android_dir + "xml/appfilter.xml"
    theme_dir = android_dir + "drawable-xxhdpi/"

    app_filter_content = '<?xml version="1.0" encoding="utf-8"?>\n'
    app_filter_content += '<resources>\n'

    mkdir(theme_dir)
    mkdir(path.dirname(app_filter))

    for icon_name, icon in icons.items():
        for component_info in icon.get("android", []):
            source = "icons/{0}/48/{1}.svg".format(theme, format(icon_name))
            drawable_name = icon_name.replace(".", "_").replace("-", "_")
            output = "{0}/{1}.png".format(theme_dir,
                                          drawable_name)
            if path.exists(source):
                convert_svg2png(source, output, 192, 192)
            app_filter_content += '\t<item component="ComponentInfo{' + \
                component_info + '}" drawable="' + drawable_name + '"/>\n'

    app_filter_content += '</resources>'
    with open(app_filter, 'w') as app_filter_obj:
        app_filter_obj.write(app_filter_content)


elif platform == "linux":
    print("\nGenerating Linux theme...")
    linux_dir = "numix-icon-theme-{0}/Numix-{1}".format(theme, theme.title())
    for size in sizes:
        mkdir("{0}/{1}/apps".format(linux_dir, size))
    for icon_name, icon in icons.items():
        if not icon.get("linux"):
            continue
        for size in sizes:
            root = "{0}.svg".format(icon["linux"]["root"])
            source = "icons/{0}/{1}/{2}.svg".format(theme, size, icon_name)
            output = "{0}/{1}/apps/{2}".format(linux_dir, size, root)
            if path.exists(source):
                bfb_icon = icon["linux"].get("bfb")
                if bfb_icon:
                    output_bfb = "{0}/{1}/apps/{2}.png".format(linux_dir,
                                                               size,
                                                               bfb_icon)
                    if int(size) == 48:
                        convert_svg2png(source, output_bfb, 144, 144)
                copy2(source, output)
                for link in icon["linux"].get("symlinks", []):
                    output_symlink = "{0}/{1}/apps/{2}.svg".format(linux_dir,
                                                                   size, link)
                    try:
                        symlink(root, output_symlink)
                    except FileExistsError:
                        continue
elif platform == "osx":
    print("\nGenerating OSX theme...")
    ink_flag = call(['which', 'png2icns'], stdout=PIPE, stderr=PIPE)
    if ink_flag != 0:
        exit("You will need png2icns in order to generate OSX theme")
    osx_dir = "numix-{0}.icns".format(theme)
    osx_sub_dirs = ["icns", "pngs", "vectors"]
    for sub_dir in osx_sub_dirs:
        mkdir("{0}/{1}".format(osx_dir, sub_dir))
    for icon_name, icon in icons.items():
        for output_icon in icon.get("osx", []):
            source = "icons/{0}/48/{1}.svg".format(theme, icon_name)
            output_svg = "{0}/vectors/{1}.svg".format(osx_dir, output_icon)
            output_png = "{0}/pngs/{1}.png".format(osx_dir, output_icon)
            output_icn = "{0}/icns/{1}.icn".format(osx_dir, output_icon)
            if path.exists(source):
                copy2(source, output_svg)
                convert_svg2png(source, output_png, 1024, 1024)
                call(["png2icns", output_icn, output_png],
                     stdout=PIPE, stderr=PIPE)
# Clean Up
print("Done!\n")
