# Circle Core
This is a demo repo for testing the new generation idea for the Numix app icons theme. This new method is designed to make keeping themes on different platforms on feature parity easier as well as making it as simple as possible to add support for new platforms.


## Dependencies
The main script needs Python 3.x to run. The exporting-to-PNG part of the script currently uses bash scripts and [Inkscape](https://inkscape.org/) but I hope to move these into the main script asap. The OSX packaging needs [libicns](http://icns.sourceforge.net/) for the `png2icns` command.

## How To Use
1. Download the repo
2. Run `gen.py`
3. Pick your platform
4. Get your generated package
