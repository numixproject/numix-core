# Contributing to Numix Core

## Contribution process

1. Fork our GitHub repository.

2. Create the new icon using [Inkscape](https://inkscape.org/) (free and open source)

3. Push it to your forked repository.

   > Remember to write a proper commit message ([example guide](https://chris.beams.io/posts/git-commit/)).

   > If you are working on an open issue you can automatically close it using some keywords and the issue number ([more info here](https://help.github.com/articles/closing-issues-via-commit-messages/)).

4. Create a new pull request. It helps if you include a sample of your icon here in PNG format ([example](https://github.com/numixproject/numix-core/pull/1422)).

   > Remember to create a different pull request for each icon you want to submit.

5. When the pull request is accepted you can delete your fork or [sync it](https://help.github.com/articles/syncing-a-fork/). Now, you are ready to create new one!

## New Icons

New icons you must follow our [style guidelines](https://github.com/numixproject/numix-core/wiki/Guidelines). Furthermore:

 * All new icons must have a **circle** and a **square** version - other shapes (_shine_, _utouch_) are optional
 * All new icons must have an entry in the `data.json` file (more on this in the _Data File_ section)


## Data File

The `data.json`  file contains all the information needed for linking the icons to the names needed by different platforms.

The file's structure:

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

* the **icon-entry** is the name of the `SVG`
  * it should be in dash-case
  * it should be a meaningful name
* the **android**  part is the list of components the should use the icon
  * this information can be gathered from the **ComponentInfo** on http://activities.tundem.com/
* the **linux** part holds the names that a linux desktop files _Icon_ line says
  * the **root** holds the primary entry
  * the **symlinks** holds alternative names

## Python

Theme building and validation scripts are written in Python.

## Optimisation options

These are the Inkscape optimised SVG settings which we use as standard when adding icons to the repo:

![inkscape](https://user-images.githubusercontent.com/7050624/27377172-81b5eec6-5674-11e7-94cd-44b9e001b4bc.png)

![inkscape2](https://user-images.githubusercontent.com/7050624/27377849-7795b6cc-5676-11e7-93c7-8b7fceabd0d3.png)

![inkscape3](https://user-images.githubusercontent.com/7050624/27377856-7afa5020-5676-11e7-93ae-d857b38988ec.png)
