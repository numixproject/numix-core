#!/usr/bin/env python3

"""
Copyright (C) 2019 Numix Project
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 3+) as
published by the Free Software Foundation. You should have received
a copy of the GNU General Public License along with this program.
If not, see <http://www.gnu.org/licenses/>.
"""

import json
from jsonschema import validate, ValidationError
from jsonschema.exceptions import SchemaError as SchemaError
from os import path

from utils import error, success


ABS_PATH = path.dirname(path.abspath(__file__))
DB_FILE = path.join(ABS_PATH, "../data.json")
SCHEMA_FILE = path.join(ABS_PATH, 'schema.json')

with open(SCHEMA_FILE, 'r') as schema_obj:
    SCHEMA = json.load(schema_obj)

has_errors = False
with open(DB_FILE, 'r') as db_obj:
    try:
        validate(json.load(db_obj), SCHEMA)
    except (ValidationError, ValueError, SchemaError) as error:
        has_errors = True
        error("Invalid database")
        error("{}".format(error))
    else:
        success("The database is valid")

exit(has_errors)
