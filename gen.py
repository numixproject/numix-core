#!/usr/bin/python3

# Copyright (C) 2016
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License (version 3+) as
# published by the Free Software Foundation. You should have received
# a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

# Sorting out modules
from json import load
import urllib.request
from os import listdir, makedirs, path, symlink
from shutil import copy2, move, rmtree
from subprocess import PIPE, Popen, call
from io import BytesIO
from gi import require_version
require_version('Rsvg', '2.0')
git_flag = call(['which', 'git'], stdout=PIPE, stderr=PIPE)
if git_flag != 0:
    exit("Please install git first. Exiting")
try:
    from gi.repository import Rsvg
    import cairo
    use_inkscape = False
except (ImportError, AttributeError):
    ink_flag = call(['which', 'inkscape'], stdout=PIPE, stderr=PIPE)
    if ink_flag == 0:
        use_inkscape = True
    else:
        exit("Can't load cariosvg nor inkscape")
# Importing JSON
try:
    with open('data.json') as data:
        icons = load(data)
except FileNotFoundError:
    exit("Database file not found, please download data.json. Exiting")

# User selects the theme
theme, themes = "", ["circle"]
while True:
    theme = input("What theme would you like to build? ").lower().strip()
    if theme in themes:
        break
    else:
        print("Please enter one of the following:", ", ".join(themes), "\n")

# User selects the platform
platform, platforms = "", ["android", "linux", "osx"]
while True:
    platform = input("What OS would you like to build for? ").lower().strip()
    if platform in platforms:
        break
    else:
        print("Please enter one of the following:", ", ".join(platforms), "\n")


def mkdir(dir):
    if not path.exists(dir):
        makedirs(dir)


def clone(repo):
    try:
        urllib.request.urlopen("https://google.com", timeout=1)
        print("Cloning the repo...")
        p = Popen(["git", "clone", repo], stdout=PIPE, stderr=PIPE)
        p.communicate()
    except urllib.request.URLError:
        exit("Internet connection is needed in order to download the icon theme. Existing")


def convert_svg2png(infile, outfile, w, h):
    """
        Converts svg files to png using Cairosvg or Inkscape
        @file_path : String; the svg file absolute path
        @dest_path : String; the png file absolute path
    """
    if use_inkscape:
        p = Popen(["inkscape", "-f", infile, "-e", outfile,
                   "-w" + str(w), "-h" + str(h)],
                  stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
    else:
        handle = Rsvg.Handle()
        svg = handle.new_from_file(infile)
        dim = svg.get_dimensions()

        img = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
        ctx = cairo.Context(img)
        ctx.scale(w / dim.width, h / dim.height)
        svg.render_cairo(ctx)

        png_io = BytesIO()
        img.write_to_png(png_io)
        with open(outfile, 'wb') as fout:
            fout.write(png_io.getvalue())
        svg.close()
        png_io.close()
        img.finish()


# Downloading icons
print("Cloning icons from GitHub...")
if path.isdir(theme + "-core/icons"):
    print("The icon theme already exists.")
    print("1 - Update")
    print("2 - Ignore")
    print("3 - Cancel")
    choosed = False
    while not choosed:
        try:
            choice = int(input("Please choose : "))
        except ValueError:
            continue
        if choice == 1:
            choosed = True
            print("Updating..")
            rmtree(theme + "-core")
            clone("https://github.com/numixproject/" + theme + "-core.git")
        elif choice == 2:
            choosed = True
        elif choice == 3:
            choosed = True
            exit("Exiting")
else:
    clone("https://github.com/numixproject/" + theme + "-core.git")

# Only certain icon sizes may be covered
sizes = listdir(theme + "-core/icons")


# The Generation Stuff
if platform == "android":
    print("\nGenerating Android theme...")
    adir = "com.numix.icons_{0}/".format(theme)
    adir_extra = "MainActivity22/app/src/main/res/drawable-xxhdpi/"
    adir = adir + adir_extra
    mkdir(adir)
    for icon in icons:
        for name in icons[icon].get("android", []):
            name = name.replace("_", ".")
            if path.exists("icons/48/" + icon + ".svg"):
                convert_svg2png(theme + "-core/icons/48/" + icon + ".svg",
                                adir + name + ".png", 192, 192)
elif platform == "linux":
    print("\nGenerating Linux theme...")
    ldir = "numix-icon-theme-{0}/Numix-{1}/".format(theme, theme.title())
    for size in sizes:
        mkdir(ldir + size + "/apps")
    for icon in icons:
        if "linux" in icons[icon].keys():
            for size in sizes:
                root = icons[icon]["linux"]["root"] + ".svg"
                if path.exists(theme + "-core/icons/" + size + "/" + icon + ".svg"):
                    copy2(theme + "-core/icons/" + size + "/" + icon + ".svg",
                          ldir + size + "/apps/" + root)
                    for link in icons[icon]["linux"].get("symlinks", []):
                        try:
                            symlink(root,
                                    ldir + size + "/apps/" + link + ".svg")
                        except FileExistsError:
                            continue
elif platform == "osx":
    print("\nGenerating OSX theme...")
    odir = "numix-{0}.icns/".format(theme)
    for ext in ["icns", "pngs", "vectors"]:
        mkdir(odir + ext)
    try:
        ink_flag = call(['which', 'png2icns'], stdout=PIPE, stderr=PIPE)
        if ink_flag != 0:
            raise Exception
    except (FileNotFoundError, Exception):
        exit("You will need png2icns in order to generate OSX theme")
    for icon in icons:
        for name in icons[icon].get("osx", []):
            if path.exists(theme + "-core/cons/48/" + icon + ".svg"):
                copy2(theme + "-core/icons/48/" + icon + ".svg",
                      odir + "vectors/" + name + ".svg")
                convert_svg2png(theme + "-core/icons/48/" + icon + ".svg",
                                odir + "pngs/" + name + ".png", 1024, 1024)
                call(["png2icns", odir + "icns/" + name + ".icn",
                      odir + "pngs/" + name + ".png"],
                     stdout=PIPE, stderr=PIPE)
# Clean Up
print("Done!\n")
exit(0)
