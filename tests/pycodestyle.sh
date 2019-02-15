#!/usr/bin/env sh
find . -name "*.py" | xargs pycodestyle $1
