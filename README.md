# Numix uTouch

Numix uTouch is an icon theme from the [Numix project](http://numixproject.org). The theme isn't actively maintained anymore (we'd recommend you use [Circle](https://github.com/numixproject/numix-icon-theme-circle)) but you can use it from here if you wish. This readme provides information on [installation](https://github.com/numixproject/numix-icon-theme-utouch/#installation), [icon requests](https://github.com/numixproject/numix-icon-theme-utouch/#icon-requests) and [hardcoded icons](https://github.com/numixproject/numix-icon-theme-utouch/#hardcoded-icons). Licensed under the GPL-3.0+

### Installation

Because uTouch is no longer actively maintained the only way to install it is through `git`. Here's how you do that:

```bash
cd ~/.local/share/icons
git clone https://github.com/numixproject/numix-icon-theme-utouch.git
mv numix-icon-theme-utouch/Numix-uTouch .
rm -rf numix-icon-theme-utouch LICENSE README.md
```

### Icon Requests
For normal applications follow [this video tutorial](https://plus.google.com/+NumixprojectOrg/posts/DkRmhFZuWez), for Steam games follow [this one](https://www.youtube.com/watch?v=BuUy4CzCoXc) and for Chrome apps just post a link to the webstore page. For non-app requests try to include as much information (especially icon names) as possible to make our job easier.

### Hardcoded Icons
To deal with hardcoded application icons Numix uses the [hardcode-fixer](https://github.com/Foggalong/hardcode-fixer) script. A list of the applications supported by the script can be found [here](https://github.com/Foggalong/hardcode-fixer/wiki/App-Support). To deal with hardcoded status icons Numix recommends you use the [Hardcode Tray](https://github.com/bil-elmoussaoui/Hardcode-Tray) script.
