#!/bin/bash

for f in *.svg; do inkscape $f --without-gui --export-png="${f%.*}.png" --export-background-opacity 0.0 -w 1024 -h 1024; done
rm osx.sh *.svg
