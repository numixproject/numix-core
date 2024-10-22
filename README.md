# Numix Core

[![By The Numix Project](https://img.shields.io/badge/By-The%20Numix%20Project-f0544c.svg?style=flat-round)](https://numixproject.org/)&nbsp;[![Test](https://img.shields.io/github/actions/workflow/status/numixproject/numix-core/test.yml?branch=master)](https://github.com/numixproject/numix-core/actions/workflows/test.yml)

This repository powers the generation of the all the Numix app icon themes across all platforms. This new method is designed to make keeping themes on different platforms on feature parity easier as well as making it as simple as possible to add support for new platforms. Licensed under the GPL-3.0+ and maintained by [@palob](https://github.com/palob).

## Artwork

This repo contains the artwork used for the Numix icon themes, split into the vibrant themes (Circle and Square) and the mono themes (uTouch and Shine). Only the Circle and Square vibrant themes are currently maintained but this script can build all.

### Icon Requests

Please report icon requests in this repo using the [appropriate issue template](https://github.com/numixproject/numix-core/issues/new/choose) or [read this page](https://github.com/numixproject/numix-core/wiki/Requesting-Icons) for more information.

### Contributions

We accept contributions, read [this page](.github/CONTRIBUTING.md#Icons) for more info. If you're interested in taking up maintenance of an unmaintained theme then [get in touch](mailto:numixproject@gmail.com).

### Hardcoded Icons

To deal with hardcoded application icons Numix uses the [hardcode-fixer](https://github.com/Foggalong/hardcode-fixer) script. A list of the applications supported by the script can be found [here](https://github.com/Foggalong/hardcode-fixer/wiki/App-Support).

## Script

This repo also contains [gen.py](https://github.com/numixproject/numix-core/blob/master/gen.py), the code used for building the icon themes. The Linux themes in particular are then packaged using [this script](https://github.com/numixproject/numix-tools/blob/master/numix-tools/package.sh) into [Circle](https://github.com/numixproject/numix-icon-theme-circle) and [Square](https://github.com/numixproject/numix-icon-theme-square).

### Dependencies

The script needs Python 3.x to run. While the script can build themes for many platforms, running it is only officially supported on Linux. The exporting-to-PNG part of the script currently uses [Cairo](https://cairographics.org/) or [Inkscape](https://inkscape.org/). The macOS packaging needs [libicns](http://icns.sourceforge.net/) for the `png2icns` command. More information can be found [in our wiki](https://github.com/numixproject/numix-core/wiki/Dependencies).

### How To Use

1. [Download](https://github.com/numixproject/numix-core/archive/refs/heads/master.zip) the repo
2. Run `gen.py --theme {circle,square} --platform {android,linux,osx}`
3. Get your generated package

### Tests

The [tests/](https://github.com/numixproject/numix-core/tree/master/tests) directory contains several tests for making sure the [data.json](data.json) is valid. We also use [flake8](https://flake8.pycqa.org/), [markdownlint](https://github.com/DavidAnson/markdownlint), and [editorconfig](.editorconfig) for linting.
