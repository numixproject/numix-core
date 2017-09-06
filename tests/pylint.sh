#!/usr/bin/env sh
find . -name "*.py" | xargs pylint $1
