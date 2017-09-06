#!/usr/bin/env python3
# pylint: disable=C0103
"""
# Copyright (C) 2016
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License (version 3+) as
# published by the Free Software Foundation. You should have received
# a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.
"""

import json
from os import path

from jsonschema import validate, ValidationError

DB_FILE = path.join(path.dirname(path.abspath(__file__)), "../data.json")
SCHEMA_FILE = path.join(path.dirname(path.abspath(__file__)), 'schema.json')

with open(SCHEMA_FILE, 'r') as schema_obj:
    SCHEMA = json.load(schema_obj)

has_errors = False
with open(DB_FILE, 'r') as db_obj:
    try:
        validate(json.load(db_obj), SCHEMA)
    except (ValidationError, ValueError) as error:
        has_errors = True
        print("\033[91m Invalid database \033[0m")
        print("\033[91m {}\033[0m".format(error))
    else:
        print("\033[92m The database is valid\033[0m")
exit(int(has_errors))
