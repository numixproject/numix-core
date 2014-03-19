Hard Coded Icons
================

When making applications a lot of developers choose to hard code their icons. This is a bad practice as it makes it impossible for icon themes to change them in any way. Other than reporting these issues upstream there's not much that can be done about this.

However, this problem can be dealt with manually. Below is a list of all the hard coded icons that Numix has its own Circle icons for. The icon change can be manually made by changing the ```icon``` line of the ```application.desktop``` file in ```/usr/share/applications/``` as specified.

For example, take the **Format Junkie** applications. Currently ```formatjunkie.desktop``` has the icon line ```Icon=/opt/extras.ubuntu.com/formatjunkie/pixmap/fjt.png``` but there's a numix icon for it called ```fjt.svg```. Using your text editor of choice simple replace ```/opt/extras.ubuntu.com/formatjunkie/pixmap/fjt.png``` with ```fjt``` and the change will be made.

| Application Name | Current Icon Location | Numix Icon Name |
| :---------------: | :---------------: | :---------------:|
| Format Junkie | /opt/extras.ubuntu.com/formatjunkie/pixmap/fjt.png | fjt |