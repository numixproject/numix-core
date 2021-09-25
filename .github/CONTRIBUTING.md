# Contributing to Numix Core

So you want to contribute to the Numix app themes? Great! Make sure that you're doing the following so that we can get your contributions merged in as soon as possible.

## General Process

All contributions, regardless of which bit of the project they're part of, must follow these steps:

1. [Fork](https://help.github.com/articles/fork-a-repo/) our GitHub repository
2. Make your changes and [push them](https://help.github.com/articles/pushing-to-a-remote/) to your fork
    1. Remember to write a proper [commit message](https://chris.beams.io/posts/git-commit/)
    2. If you're fixing an issue, [close it using keywords](https://help.github.com/articles/closing-issues-via-commit-messages/)
3. Create a new [pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/)
4. Make any changes requested and push again
5. When the pull request is accepted you can delete your fork or [sync it](https://help.github.com/articles/syncing-a-fork/)

Now you are ready to start again!

## Icons

This section covers what to do when creating a new icon or changing the design for an existing icon. If you're wanting to add a symlink see the section on the data file.

1. Make your icon using [Inkscape](https://inkscape.org/) (free and open source)
    1. You must follow our [style guidelines](https://github.com/numixproject/numix-core/wiki/Guidelines)
    2. Icons must be saved as an optimized SVG with [these settings](https://github.com/numixproject/numix-core/wiki/Optimise-Options)
    3. New icon need an entry in the [data file](https://github.com/numixproject/numix-core/blob/master/.github/CONTRIBUTING.md#data-file)
2. Create a different pull request for each (unrelated) change you're submitting
    1. Pull requests must contain icons for Circle and Square at minimum
    2. Adding icons for other themes such as Shine and uTouch is optional
3. Include a sample of your icon ([example](https://github.com/numixproject/numix-core/pull/1422)) to make review easier

## Data File

The `data.json` file contains all the information needed for linking the icons to the names needed by different platforms. It has the following structure:

```json
{
    "icon-entry": {
        "android": [
            "com.example.app/com.example.app.Activity"
        ],
        "linux": {
            "root": "PrimaryName",
            "symlinks": [
                "alternative-entry",
                "org.other.Entry"
            ]
        }
    }
}
```

* The `icon-entry` is the name of the SVG file and should be [meaningfully named](https://github.com/numixproject/numix-core/blob/master/data.json#L7529-L7533) using [dash-case](https://en.wikipedia.org/wiki/Naming_convention_(programming)#Delimiter-separated_words).
* The `android`  part is the list of components the icon should use, which can be gathered from the "ComponentInfo" [here](http://activities.tundem.com/).
* The `linux` part holds the names from the `Icon=*` line of `*.desktop` files
  * the `root` holds the primary entry
  * the `symlinks` holds alternative names

If you're making changes to this file in a pull request Travis will run a validation check to make sure you haven't made any errors, but please try and check before pushing to make review as easy as possible.

## Code

The scripts used for theme building and validation are written in Python. Similarly to the data file, Travis will run a validation check using [pycodestyle](https://github.com/pycqa/pycodestyle) to make sure the coding style you've used is consistent with that used in the project. If you are working on this part of the project it's recommended that you check your changes using a pycodestyle linter before creating a pull request.

### Indentation

Throughout this project we use 4 spaces for JSON and Python files, and generally use 1 space for SVG. If you want to diverge, do it locally (e.g. using [git filters](https://stackoverflow.com/questions/2316677/can-git-automatically-switch-between-spaces-and-tabs#2318063)).
