# Contributing Guidelines

## Cotribution process
If you want to contribute to this project by making new icons you must follow our [guidelines](https://github.com/numixproject/numix-core/wiki/Guidelines). You can use these instructions as reference:

1. Fork our GitHub repository.
2. Create the new icon using [Inkscape](https://inkscape.org/) (free and open source)  
3. Push it to your forked repository. Remember to write a proper commit message ([example guide](https://gist.github.com/josh/539516)). If you are working on an open issue you can automatically close it using some keywords and the issue number ([more info here](https://help.github.com/articles/closing-issues-via-commit-messages/)).
4. Create a new pull request. You can include a sample of your icon here in PNG format ([example](https://github.com/numixproject/numix-core/pull/1422)).
5. When the pull request is accepted you can delete your fork or [sync it](https://help.github.com/articles/syncing-a-fork/). Now, you are ready to create new one!

Remember to create a different pull request for each icon you want to submit. All new contributions will be welcomed.

## Editing guidelines (circle)

### Anatomy
* Shadow layer - the dropshadow on the bottom right layer, don't touch it.
* Base layer - the base circle with the colour gradient and the inset shadow on the bottom right. Don't touch the shadow, but tweak the gradient. The only time you can touch the shadow is if you have to move it to the symbol layer when you use fullscreen symbol. It's coordinates are x = 7,531, y = 1.
* Symbol layer - the layer for all things symbol.

### Symbols
* User 24, 26 or 28 sized symbols and 30 or 32 sized symbols if they are circles.
* Avoid plain symbols, use quasi flat when possible.
* The size size doesn't have to be a perfect square, so for example 26px wide and 24px tall is perfectly acceptable.
* Always check for optical illusions by looking at the icon in 48 px size, sometimes you need to de-centre the symbol for it to look proper in smaller size.
* If you're going to use faux shadows in the symbol makes sure the "light source" is on the top left. The shadow should point to the bottom right just like the drop and inset shadow of the base-plate.
* The symbol shadow is a duplicate of the symbol background coloured black, made 10% opaque and moved 1px to the right and bottom and of course moved below the symbols. If the symbol shadow consists of more then one object, merge them into one single path.
* Don't use strokes. You can use objects that look like strokes, that's OK, but make sure they are paths.
* Fullscreen symbols (like in Kazam and Firefox for example) are accepted, but don't overuse this style. If you're gonna use this move the inset shadow to the symbol layer.
* Align to grid.

### Colouring
* Avoid white symbols. Use light (eeeeee for example is a good colour) and if you really have to use plain white symbol tint it with the same colour as the background.
* Colour the symbols in vivid, but not eye jarring colours when they are quasi flat styled.
* Colour the background (base layer) with subtle gradient (top is lighter, bottom is darker) with a colour in the same spectrum of the RGB wheel. Use nice and vivid colours, but don't use eye jarring ones.

## Optimisation options
These are the Inkscape optimised SVG settings which we use as standard when adding icons to the repo:

![inkscape](https://user-images.githubusercontent.com/7050624/27377172-81b5eec6-5674-11e7-94cd-44b9e001b4bc.png)

![inkscape2](https://user-images.githubusercontent.com/7050624/27377849-7795b6cc-5676-11e7-93c7-8b7fceabd0d3.png)

![inkscape3](https://user-images.githubusercontent.com/7050624/27377856-7afa5020-5676-11e7-93ae-d857b38988ec.png)

## Unthemed icons
So you're seeing icons which aren't themed on your desktop? There are 3 reasons why this isn't the case.

### Hardcoded Icons
We all make mistakes and developers are no exception. Sometimes they write programs in such a way that the icon cannot be themed even if an icon theme has the relevant icon; this is called hardcoding the icon. To deal with hardcoded application icons Numix uses the [hardcode-fixer](https://github.com/Foggalong/hardcode-fixer) script. A list of the applications supported by the script can be found [here](https://github.com/Foggalong/hardcode-fixer/wiki/App-Support).

### Invalid Icon Names
Another mistake developers sometimes make is creating an icon with an invalid name. When picking a name for an icon you cannot use non-[ASCII](https://en.wikipedia.org/wiki/ASCII) characters, spaces, or commas. Because of this if we get a request for an icon which has any of those things we cannot fulfill it. If we try to include an icon with invalid characters we get an error [like this](https://github.com/numixproject/numix-core/issues/915). Here's a list of such icons that have been requested to Numix:

* 56B4_Battle.net Launcher.0.svg
* 5C12_World of Warcraft Launcher.0.svg
* Angry Birds-chrome.angrybirds.com.svg
* Amazon Cloud Reader-read.amazon.com.svg
* Google Calendar-google.com.svg
* Google docs-docs.google.com.svg
* Google News-news.google.com.svg
* Yahoo Mail-mail.yahoo.com.svg


### Icon Requests
Maybe we just don't have your icon in our theme! For normal applications follow [this video tutorial](https://plus.google.com/+NumixprojectOrg/posts/DkRmhFZuWez), for Steam games follow [this one](https://www.youtube.com/watch?v=BuUy4CzCoXc) and for Chrome apps just post a link to the webstore page. When filing your request please be respectful, patient, and remember that Circle development is done solely on the back of donations.
