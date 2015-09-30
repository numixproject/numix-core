#!/bin/bash

for f in *.*; do mv "$f" "${f//./_}"; done
for f in *_svg*; do mv "$f" "${f//_svg/.svg}"; done
for f in *_sh*; do mv "$f" "${f//_sh/.sh}"; done
for f in `find`; do mv -v $f `echo $f | tr '[A-Z]' '[a-z]'`; done
for f in *.svg; do inkscape $f --without-gui --export-png="${f%.*}.png" --export-background-opacity 0.0 -w 192 -h 192; done
rm android.sh *.svg
