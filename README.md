# Numix Core
[![By The Numix Project](https://img.shields.io/badge/By-The%20Numix%20Project-f0544c.svg?style=flat-round)](https://numixproject.org/) &nbsp;[![Build Status](https://travis-ci.org/numixproject/numix-core.svg?branch=master)](https://travis-ci.org/numixproject/numix-core)

This repository powers the generation of the all the Numix app icon themes across all platforms. This new method is designed to make keeping themes on different platforms on feature parity easier as well as making it as simple as possible to add support for new platforms. Licensed under the GPL-3.0+


## Artwork

### Icon Requests
Please report icon requests in this repo, providing all the details required. For normal applications follow [this video tutorial](https://plus.google.com/+NumixprojectOrg/posts/DkRmhFZuWez), for Steam games follow [this one](https://www.youtube.com/watch?v=BuUy4CzCoXc) and for Chrome apps just post a link to the webstore page. When filing your request please be respectful, patient, and remember that development is done solely on the back of donations.

### Contributions
We accept contributions, read [this page](https://github.com/numixproject/numix-core/wiki/Contributing) for more info.

### Hardcoded Icons
To deal with hardcoded application icons Numix uses the [hardcode-fixer](https://github.com/Foggalong/hardcode-fixer) script. A list of the applications supported by the script can be found [here](https://github.com/Foggalong/hardcode-fixer/wiki/App-Support).


## Script

### Dependencies
The script needs Python 3.x to run. While the script can build themes for many platforms, running it is only officialy supported on Linux. The exporting-to-PNG part of the script currently uses [Cairo](https://cairographics.org/) or [Inkscape](https://inkscape.org/). The OSX packaging needs [libicns](http://icns.sourceforge.net/) for the `png2icns` command.

### How To Use
1. Download the repo
2. Run `gen.py --theme {square,circle} --platform {linux,osx,android}`
3. Get your generated package
