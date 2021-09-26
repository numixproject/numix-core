# Icons

This directory contains all the actual icons files that are used to build the Numix themes.

## Tags

Icon tags are a property located in [data.json](../data.json) used to relate similar icons together. This could be for related apps' icons (e.g. `ms-office`) or icons which use the same design element (e.g. `world-baseplate`). The idea is to make it less likely that related icons won't become out of sync design wise.

Running `tags.py --tag $TAG` will collect all the icons tagged `$TAG` into a directory called `tag.$TAG` where they can be modified and copied back into there associated theme folders. Running `tags.py --clean` will delete all `tag.$TAG` directories.

### `world-baseplate`

The [world-baseplate](circle/48/web-browser.svg) is a world map svg. This design is being [phased out](https://github.com/numixproject/numix-core/issues/5153) due to its complexity.

## Themes

Each directory in this folder represents a different icon theme, grouped roughly into the following styles.

### Vibrant

_**Themes:** Circle, Square_

Current Numix style; if you're submitting a contribution then you must cover its themes. Here are the [design guidelines](https://github.com/numixproject/numix-core/wiki/Guidelines) and below you can find groups of icons which use similar elements to help you along the way.

### Mono (uTouch, Shine)

_**Themes:** uTouch, Shine_

Earlier Numix style; its themes are no longer actively supported. If you're submitting a contribution then you do not have to submit icons for these themes. These icons have square baseplates with a coloured background, overlayed with a white transparent effect (diamond lattice for uTouch, cut-through for Shine), and finally an all-white symbol.
