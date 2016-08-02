# Numix Core
This script powers the generation of the Numix app icon themes. This new method is designed to make keeping themes on different platforms on feature parity easier as well as making it as simple as possible to add support for new platforms.

## Dependencies
The main script needs Python 3.x to run. The downloading of the icon resources requires the [GitPython](https://github.com/gitpython-developers/GitPython) module and for [git](https://git-scm.com/) to be installed and accessible via system's PATH. The exporting-to-PNG part of the script currently uses [Cairo](https://cairographics.org/) or [Inkscape](https://inkscape.org/). The OSX packaging needs [libicns](http://icns.sourceforge.net/) for the `png2icns` command.

## How To Use
1. Download the repo
2. Run `gen.py`
3. Pick your theme
4. Pick your platform
5. Get your generated package
