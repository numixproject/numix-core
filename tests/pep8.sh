#!/usr/bin/env sh
find . -name "*.py" | xargs pep8 $1
