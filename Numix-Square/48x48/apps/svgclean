#!/bin/bash
find . -type f -name '*.svg' -print0 | while IFS= read -r -d '' file; do
if [[ `grep -i "inkscape\|sodipodi\|rgb" "$file"` || "$1" = "-f" ]]; then
echo "Optimizing $file"
        svgcleaner-cli "$file" "$file" --preset=basic --remove-prolog --remove-proc-instr --remove-unused-defs --remove-metadata-elts --remove-inkscape-elts --remove-sodipodi-elts --remove-ai-elts --remove-corel-elts --remove-msvisio-elts --remove-sketch-elts --remove-outside-elts --equal-elts-to-use --remove-version --remove-unreferenced-ids --trim-ids --remove-inkscape-atts --remove-sodipodi-atts --remove-ai-atts --remove-corel-atts --remove-msvisio-atts --remove-sketch-atts --remove-stroke-props --remove-fill-props
    fi
done
