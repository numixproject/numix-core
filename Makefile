INSTALL_DIR=$(DESTDIR)/usr/share/icons/Discreete-Linux

all: icons

icons:
	./gen.py --theme circle --platform linux

clean:
	rm -rf discreete-linux-icon-theme-circle
	rm -rf discreete-linux-icon-theme-square

install:

.PHONY: all
.PHONY: icons

.DEFAULT_GOAL := all

# vim: set ts=4 sw=4 tw=0 noet :
