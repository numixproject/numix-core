Hard Coded Icons
================

When making applications some developers choose to hard code their icons. This is a bad practice as it makes it impossible for icon themes to change them. Other than reporting these issues upstream there's not much that can be done about this.

However, this problem can be dealt with manually. Below is a list of all the hard coded icons that Numix has its own Circle icons for. The icon change can be manually made by changing the ```icon``` line of the ```application.desktop``` file in ```/usr/share/applications/``` as specified. The list also includes Steam games which list ```steam``` as their icon.

For example, take the **Format Junkie** application. Currently ```formatjunkie.desktop``` has the icon line ```Icon=/opt/extras.ubuntu.com/formatjunkie/pixmap/fjt.png``` but there's a numix icon for it called ```fjt.svg```. Using your text editor of choice simple replace ```/opt/extras.ubuntu.com/formatjunkie/pixmap/fjt.png``` with ```fjt``` and the change will be made.

Obviously this is just a temporary solution and to fix the problem for good upstream issues need to be filed for all these hard coded icons. To see the upstream report for an icon just click on the link in the icon's name below. No link? Then file that upstream now! Are we missing any reports? [File that issue with us!](https://github.com/numixproject/numix-icon-theme-circle/issues/new)

| Application Name | Current Icon Location | Numix Icon Name |
| :---------------: | :---------------: | :---------------: |
| 2048 | /usr/share/2048/meta/apple-touch-icon.png | 2048 |
| [Android Studio](https://code.google.com/p/android/issues/detail?id=67582) | /opt/android-studio/bin/idea.png | androidstudio |
| [Arista](https://github.com/danielgtaylor/arista/issues/164) | /usr/share/arista/ui/icon.svg | arista |
| Bastion (Steam) | steam | steam_icon_107100 |
| [Conky Manager](https://bugs.launchpad.net/conky-manager/+bug/1296810) | /usr/share/pixmaps/conky-manager.png | conky-manager |
| Diagnose Graphics Issues | /usr/share/xdiagnose/icons/microscope.svg | microscope |
| Dogecoin-qt (AUR) | /usr/share/pixmaps/dogecoin.png | dogecoin |
| Dota 2 (Steam) | steam | steam_icon_570 |
| Driver Manager | /usr/share/icons/hicolor/scalable/apps/driver-manager.svg | jockey |
| Easy Life | /usr/share/pixmaps/easylife.png | easylife |
| Fade In | /usr/share/fadein/icon_app/fadein_icon_128x128.png | fadein |
| FileBot | /usr/share/filebot/icon.svg | filebot |
| Format Junkie | /opt/extras.ubuntu.com/formatjunkie/pixmap/fjt.png | fjt |
| [Gcolor2](http://sourceforge.net/p/gcolor2/feature-requests/11/)| /usr/share/pixmaps/gcolor2/gcolor2.xpm | gcolor2 |
| [Gespeaker](https://github.com/muflone/gespeaker/issues/49) | /usr/share/gespeaker/data/icons/gespeaker.svg | gespeaker | 
| GNOME Weather | org.gnome.Weather.Application | gnome-weather |
| GNUcview | /usr/share/pixmaps/guvcview/guvcview.png | guvcview |
| GNU Octave | /usr/share/octave/3.6.4/imagelib/octave-logo.svg | octave |
| GoldenDict | /usr/share/pixmaps/goldendict.png | goldendict |
| Graphic Network Simulator | /usr/share/pixmaps/gns3.xpm | gns |
| Grisbi | /usr/share/pixmaps/grisbi/grisbi.svg | grisbi |
| Guake | /usr/share/pixmaps/guake/guake.png | guake |
| HipChat | hipchat.png | hipchat |
| [HPLJ](https://bugs.launchpad.net/ubuntu/+source/foo2zjs/+bug/1299552) | /usr/share/pixmaps/hplj1020_icon | printer |
| Intel Graphics Installer | /usr/share/intel-linux-graphics-installer/images/logo.png | intel-installer |
| [IntelliJ IDEA](http://youtrack.jetbrains.com/issue/IDEA-122364) | /opt/idea-IC/bin/idea.png | idea |
| Kerbal Space Program.desktop | steam | steam_icon_220200 |
| Klavaro | /usr/share/icons/hicolor/24x24/apps/klavaro.png | klavaro |
| Left 4 Dead 2.desktop | steam | steam_icon_550 |
| Left 4 Dead 2 Beta.desktop | steam | steam_icon_223530 |
| Lightworks | /usr/share/lightworks/Icons/App.png | lightworks |
| Lucky Backup | /usr/share/pixmaps/luckybackup.png | luckybackup |
| Master PDF Editor | /opt/master-pdf-editor/master-pdf-editor.png | master-pdf-editor |
| Mint Audio Tag | /usr/lib/linuxmint/mintInstall/icon.svg | audio-tag-tool |
| Mint Backup | /usr/lib/linuxmint/mintBackup/icon.png | mintbackup |
| Mint Software Manager | /usr/lib/linuxmint/mintInstall/icon.svg | software-manager |
| My Weather Indicator | /opt/extras.ubuntu.com/my-weather-indicator/share/pixmaps/my-weather-indicator.png | indicator-weather |
| Netbeans | /usr/share/netbeans/7.0.1/nb/netbeans.png | netbeans |
| Ninja IDE | /usr/share/ninja-ide/img/icon.png | ninja-ide |
| Nitro | /usr/share/nitrotasks/media/nitrotasks.png | nitrotasks |
| NotifyOSD | /usr/share/notifyosdconf/not.png | notifyosdconf |
| OmegaT | /usr/share/omegat/images/OmegaT.xpm | omegat |
| Oracle SQL Developer | /opt/oracle-sqldeveloper/icon.png | N/A |
| PacmanXG | /usr/share/pixmaps/pacmanxg.png | pacmanxg |
| Pamac (Install) | /usr/share/pamac/icons/32x32/apps/pamac.png | system-software-install |
| Pamac (Update) | /usr/share/pamac/icons/32x32/apps/pamac.png | system-software-update |
| pgAdmin3 | /usr/share/pgadmin3/pgAdmin3.png |pgAdmin3 |
| [pgModeler](https://github.com/pgmodeler/pgmodeler/issues/441) | etc/pgmodeler/pgmodeler_logo.png | NYA |
| PHP Storm | PhpStorm-133.803/bin/webide.png | phpstorm |
| Pycharm | /home/radio/Descargas/pycharm-community-3.1.1/bin/pycharm.png | pycharm |
| pyRenamer | /usr/share/pyrenamer/pyrenamer.png | pyrenamer |
| [Python 2.6](http://bugs.python.org/issue21096) | /usr/share/pixmaps/python2.6.xpm | python2.6 |
| [Python 2.7](http://bugs.python.org/issue21096) | /usr/share/pixmaps/python2.7.xpm | python2.7 |
| [Python 3.0](http://bugs.python.org/issue21096) | /usr/share/pixmaps/python3.0.xpm | python3.0 |
| [Python 3.1](http://bugs.python.org/issue21096) | /usr/share/pixmaps/python3.1.xpm | python3.1 |
| [Python 3.2](http://bugs.python.org/issue21096) | /usr/share/pixmaps/python3.2.xpm | python3.2 |
| [Python 3.3](http://bugs.python.org/issue21096) | /usr/share/pixmaps/python3.3.xpm | python3.3 |
| [Python 3.4](http://bugs.python.org/issue21096) | /usr/share/pixmaps/python3.4.xpm | python3.4 |
| Quick List Editor | /usr/share/pixmaps/qle_pix/logoqle2.svg | logoqle2 |
| Robomongo | robomongo.png | robomongo |
| SmartGitHG | smartgithg.png | smartgithg |
| Springseed | /usr/share/pixmaps/springseed/springseed.svg | springseed |
| [Synergy](http://synergy-foss.org/spit/issues/details/3971/#) | /usr/share/icons/synergy.ico | synergy |
| Tomate | /usr/share/tomate/media/tomate.png | tomate |
| Wireframe Sketcher | /usr/share/icons/hicolor/128x128/apps/WireframeSketcher.png | wireframe-sketcher.svg |
| Valentina Studio | /opt/VStudio/Resources/vstudio.png | vstudio |
| Viber | /usr/share/pixmaps/viber.png | viber |
| YouTube-DL GUI | /usr/share/pixmaps/youtube-dlg.png | youtube-dl |
| Zenmap | /usr/share/zenmap/pixmaps/zenmap.png | zenmap |
