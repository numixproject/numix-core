#!/usr/bin/python3

# Copyright (C) 2015
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License (version 3+) as
# published by the Free Software Foundation. You should have received
# a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

# Sorting out modules
from csv import reader
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
with open('db.csv', 'r') as db:
    csv, data = reader(db, delimiter=',', quotechar='|'), []
    for row in csv:
        data.append(row)

# User selects the platform
ans, platforms = "", data[0][1:]
while True:
    ans = input("What OS would you like to build for? ").lower().strip()
    if ans in platforms:
        break
    else:
        print("Please enter one of the following:", ", ".join(platforms), "\n")

# Cleans up the data
position = data[0].index(ans)
for line in data:
    for x in range(1, len(data[0])):
        if x != position:
            line[x] = ""
        else:
            line[x] = line[x].split(" ")
for line in data:
    for item in line:
        line.remove("")


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
    for x in range(1, len(data)):
        for icon in data[x][1]:
            copy2("icons/48/"+data[x][0]+".svg", adir+icon+".svg")
    # Androidizing
    copy2("scripts/android.sh", adir)
    with cd(adir):
        devnull = open(devnull, 'w')
        call("./android.sh", stdout=devnull, stderr=devnull)
elif ans == "linux":
    print("\nGenerating Linux theme...")
    for size in sizes:
        mkdir(ldir + size + "/apps")
    for x in range(1, len(data)):
        for size in sizes:
            copy2("icons/"+size+"/"+data[x][0]+".svg",
                  ldir+size+"/apps/"+data[x][1][0]+".svg")
            with cd(ldir+size+"/apps/"):
                for icon in data[x][1][1:]:
                    symlink(data[x][1][0]+".svg", icon+".svg")
elif ans == "osx":
    print("\nGenerating OSX theme...")
    for ext in ["icns", "pngs", "vectors"]:
        mkdir(odir + ext)
    for x in range(1, len(data)):
        for icon in data[x][1]:
            copy2("icons/48/"+data[x][0]+".svg", odir+"vectors/"+icon+".svg")
            copy2("icons/48/"+data[x][0]+".svg", odir+"pngs/"+icon+".svg")
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
