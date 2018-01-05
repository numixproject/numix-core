import json
from collections import OrderedDict
from os import listdir, path
from shutil import move


# Load themes paths
themes = listdir("./icons")
themes_paths = []
for theme in themes:
    theme_path = path.join(path.dirname(path.realpath(path.abspath(__file__))),
                           "icons", theme, "48")
    themes_paths.append(theme_path)

# Data base file
data_file = path.realpath("./data.json")

# The icons map dict should follow this format
# Old icon name as a key
# The new icon name as a value
icons_map = {
    "chrome-mojepfklcankkmikonjlnidiooanmpbb-Default": "sunrise-calendar"
}

# Read the database file
with open(data_file, 'r') as db_obj:
    data = json.load(db_obj, object_pairs_hook=OrderedDict)


def _move(old_name, new_name):
    for theme_path in themes_paths:
        old_path = path.join(theme_path, old_name) + ".svg"
        new_path = path.join(theme_path, new_name) + ".svg"
        if path.exists(old_path):
            print(old_path)
            move(old_path, new_path)


to_delete = []
for old_name, new_name in icons_map.items():
    _move(old_name, new_name)
    if data.get(old_name):
        data[new_name] = data[old_name]
        to_delete.append(old_name)

for entry in to_delete:
    del data[entry]

with open(data_file, 'w') as db_obj:
    json.dump(data, db_obj, indent=4)
