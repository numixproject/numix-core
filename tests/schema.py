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

from utils import error, success, DB_FILE, SCHEMA_FILE

# Test which checks whether data.json matches with schema.json using
# jsonschema. Success is signified by exit code.


with open(SCHEMA_FILE, 'r') as schema_obj:
    SCHEMA = json.load(schema_obj)

has_errors = False
with open(DB_FILE, 'r') as db_obj:
    try:
        validate(json.load(db_obj), SCHEMA)
    except (ValidationError, ValueError, SchemaError) as thrown:
        has_errors = True
        error("Invalid database")
        error("{}".format(thrown))
    else:
        success("The database is valid")

exit(has_errors)
