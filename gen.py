#!/usr/bin/env python3

"""
Copyright (C) 2019 Numix Project
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
from shutil import copy2
from subprocess import PIPE, Popen, call
try:
    from gi import require_version
    require_version("Rsvg", "2.0")
    from gi.repository import Rsvg
    from cairo import ImageSurface, Context, FORMAT_ARGB32
    use_inkscape = False
except (ImportError, AttributeError, ValueError):
    # Assigns true if Inkscape found, false otherwise
    use_inkscape = not call(["which", "inkscape"], stdout=PIPE, stderr=PIPE)
    if not use_inkscape:
        exit("Can't load CairoSVG nor Inkscape")


# Loading the JSON data file
try:
    with open("data.json") as data:
        icons = load(data)
except FileNotFoundError:
    exit("Please clone the whole repository and try again.")


# Parsing build arguments
parser = ArgumentParser(prog="Numix-core")

try:
    # Exclude files and tag directories from the list of themes
    themes = [dir for dir in listdir("icons") if "." not in dir]
except FileNotFoundError:
    exit("No icons folder found. Please reclone and try again.")
parser.add_argument("--theme", "-t",
                    help="Theme you want to build.",
                    choices=themes)

platform, platforms = "", ["android", "linux", "osx"]
parser.add_argument("--platform", "-p",
                    help="Platform you like to build the theme for.",
                    choices=platforms)

args = parser.parse_args()

# User selects the theme
if not args.theme:
    msg = "Please use --theme argument with one of the following: "
    exit(msg + ", ".join(themes))
else:
    theme = args.theme
    # Each theme may support different sizes
    sizes = listdir("icons/" + theme)

# User selects the platform
if not args.platform:
    msg = "Please use --platform argument with one of the following: "
    exit(msg + ", ".join(platforms))
else:
    platform = args.platform


def mkdir(directory):
    """Create a directory if it doesn't exists."""
    if not path.exists(directory):
        makedirs(directory)


def convert_svg2png(infile, outfile, w, h):
    """
    Converts svg files to png using CairoSVG or Inkscape
    @file_path : String; the svg file absolute path
    @dest_path : String; the png file absolute path
    """
    if use_inkscape:
        cmd = Popen([
            "inkscape", "-z", infile, "-o", outfile,
            "-w", str(w), "-h", str(h)
        ], stdout=PIPE, stderr=PIPE)
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
        with open(outfile, "wb") as fout:
            fout.write(png_io.getvalue())
        svg.close()
        png_io.close()
        img.finish()


# Android Generation Code
if platform == "android":
    print("\nGenerating Android theme...")

    # Define and create theme locations
    theme_name = "com.numix.icons_" + theme
    android_dir = theme_name + "/MainActivity22/app/src/main/res/"
    app_filter = android_dir + "xml/appfilter.xml"
    theme_dir = android_dir + "drawable-xxhdpi/"
    mkdir(theme_dir)
    mkdir(path.dirname(app_filter))

    # app_filter file contains Android meta data for the theme
    app_filter_content = '<?xml version="1.0" encoding="utf-8"?>\n'
    app_filter_content += '<resources>\n'

    for icon_name, icon in icons.items():
        for component_info in icon.get("android", []):
            # Check icon source exists before it's used
            source = "icons/{0}/48/{1}.svg".format(theme, format(icon_name))
            if not path.exists(source):
                continue

            # Render icon to resources directory
            drawable_name = icon_name.replace(".", "_").replace("-", "_")
            output = "{0}/{1}.png".format(theme_dir, drawable_name)
            convert_svg2png(source, output, 192, 192)

            # Add icons app_filter data (afd) to the app_filter file
            afd = '\t<item component="ComponentInfo{{{0}}}" drawable="{1}"/>\n'
            app_filter_content += afd.format(component_info, drawable_name)

    app_filter_content += '</resources>'
    with open(app_filter, "w") as app_filter_obj:
        app_filter_obj.write(app_filter_content)


# Linux Generation Code
elif platform == "linux":
    print("\nGenerating Linux theme...")

    # Define and create theme locations
    linux_dir = "numix-icon-theme-{0}/Numix-{1}".format(theme, theme.title())
    for size in sizes:
        mkdir("{0}/{1}/apps".format(linux_dir, size))

    for icon_name, icon in icons.items():
        if not icon.get("linux"):
            continue

        for size in sizes:
            # Check icon source exists before it's used
            source = "icons/{0}/{1}/{2}.svg".format(theme, size, icon_name)
            if not path.exists(source):
                continue

            # Create root SVG icon
            root = icon["linux"]["root"] + ".svg"
            output = "{0}/{1}/apps/".format(linux_dir, size)
            copy2(source, output + root)

            # Symlinks to root icon
            for link in icon["linux"].get("symlinks", []):
                output_symlink = output + link + ".svg"
                try:
                    symlink(root, output_symlink)
                except FileExistsError:
                    continue

            # Unity 7 BFB icons
            if icon["linux"].get("bfb") and (size == "48"):
                output_bfb = icon["linux"].get("bfb") + ".png"
                convert_svg2png(source, output + output_bfb, 144, 144)


# OSX Generation Code
elif platform == "osx":
    print("\nGenerating OSX theme...")

    # OSX generation depends on libicns function png2icns
    no_icns = call(["which", "png2icns"], stdout=PIPE, stderr=PIPE)
    if no_icns:
        exit("You will need png2icns in order to generate OSX theme")

    # Define and create theme locations
    osx_dir = "numix-{0}.icns".format(theme)
    for sub_dir in ["icns", "pngs", "vectors"]:
        mkdir("{0}/{1}".format(osx_dir, sub_dir))

    for icon_name, icon in icons.items():
        for output_icon in icon.get("osx", []):
            # Check icon source exists before it's used
            source = "icons/{0}/48/{1}.svg".format(theme, icon_name)
            if not path.exists(source):
                continue

            # Icon output locations
            svg_icon = "{0}/vectors/{1}.svg".format(osx_dir, output_icon)
            png_icon = "{0}/pngs/{1}.png".format(osx_dir, output_icon)
            icn_icon = "{0}/icns/{1}.icn".format(osx_dir, output_icon)

            # Create icon in SVG, PNG, and ICNS formats
            copy2(source, svg_icon)
            convert_svg2png(source, png_icon, 1024, 1024)
            call(["png2icns", icn_icon, png_icon], stdout=PIPE, stderr=PIPE)


# Clean Up
print("Done!\n")
