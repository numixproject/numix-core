#!/usr/bin/python3

# Copyright (C) 2015
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License (version 3+) as
# published by the Free Software Foundation. You should have received
# a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

# Sorting out modules
from json import load
from os import chdir, devnull, getcwd, listdir, makedirs, path, symlink
from shutil import copy2
from subprocess import call
try:
    # Use of CairoSVG rather than the Inkscape bashscripts
    # hasn't been implemented yet but will be before release
    from cairosvg import svg2png
except ImportError:
    exit("You need python3-cairosvg to run this scripts")

# Importing CSV
with open('data.json') as data:
    icons = load(data)

# User selects the platform
ans, platforms = "", ["android", "linux", "osx"]
while True:
    ans = input("What OS would you like to build for? ").lower().strip()
    if ans in platforms:
        break
    else:
        print("Please enter one of the following:", ", ".join(platforms), "\n")


def mkdir(dir):
    if not path.exists(dir):
        makedirs(dir)


class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = getcwd()
        chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        chdir(self.savedPath)


sizes = listdir("icons")
adir = "com.numix.icons_circle/MainActivity22/app/src/main/res/drawable-xxhdpi/"
ldir = "numix-icon-theme-circle/Numix-Circle/"
odir = "numix-circle.icns/"

# The Generation Stuff
if ans == "android":
    print("\nGenerating Android theme...")
    mkdir(adir)
    for icon in icons:
        for name in icons[icon]["android"]:
            copy2("icons/48/"+icon+".svg", adir+name+".svg")
    # Androidizing
    copy2("scripts/android.sh", adir)
    with cd(adir):
        devnull = open(devnull, 'w')
        call("./android.sh", stdout=devnull, stderr=devnull)
elif ans == "linux":
    print("\nGenerating Linux theme...")
    for size in sizes:
        mkdir(ldir + size + "/apps")
    for icon in icons:
        for size in sizes:
            root = icons[icon]["linux"]["root"]+".svg"
            copy2("icons/"+size+"/"+icon+".svg", ldir+size+"/apps/"+root)
            with cd(ldir+size+"/apps/"):
                for link in icons[icon]["linux"]["symlinks"]:
                    symlink(root, link+".svg")
elif ans == "osx":
    print("\nGenerating OSX theme...")
    for ext in ["icns", "pngs", "vectors"]:
        mkdir(odir + ext)
    for icon in icons:
        for name in icons[icon]["osx"]:
            copy2("icons/48/"+icon+".svg", odir+"vectors/"+name+".svg")
            copy2("icons/48/"+icon+".svg", odir+"pngs/"+name+".svg")
    copy2("scripts/osx.sh", odir+"pngs/")
    with cd(odir + "pngs"):
        devnull = open(devnull, 'r')
        call("./osx.sh", stdout=devnull, stderr=devnull)
    for icon in listdir(odir+"pngs"):
        call(["png2icns", odir+"icns/"+icon.replace(".png", ".icn"),
              odir+"pngs/"+icon], stdout=devnull, stderr=devnull)

# Clean Up
print("Done!\n")
exit(0)
