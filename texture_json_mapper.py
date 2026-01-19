"""
Program meant to parse game assets, pair them, and store their file
location mappings in a json file.

Originally written to map version 1.8.9 textures
to version 1.21.10. The paths in REL_FOLDERS are subject to change
as Mojang updates Minecraft's asset file structure.

Minecraft's game assets must be legally acquired and their paths
must be entered into the OLD_DIR and NEW_DIR variables in rels.py 
for this code to work.

This code is tested locally and may not work on all machines.
"""

import json
import os
import sys
from pathlib import Path

from rels import REL_FOLDERS
from rels import NEW_DIR
from rels import OLD_DIR

# Value that controls whether manual logging of textures is overwritten.
manual_override = False

if not (OLD_DIR.exists() and NEW_DIR.exists()):
    sys.exit("Asset directories could not be found.")

rel_auto = {}
rel_manual = {}

def rel_check(item):
    for rel in REL_FOLDERS.keys():
        for path in item.parents:
            if rel == path:
                item_check(item, REL_FOLDERS[rel])

def item_check(item, rel):
    if Path(os.path.join(rel, item.name)).exists():
        # Put into a dictionary for automatic recording
        rel_auto[str(item)] = os.path.join(rel, item.name)
    else:
        # Put into a list for manual recording
        rel_manual[str(item)] = str(rel)


def dir_iterate(dir_):
    for item in dir_.iterdir():
        if item.is_dir():
            dir_iterate(item)
        else:
            rel_check(item)


dir_iterate(OLD_DIR)

with open("map.json", "w") as map_:
    map_.write(json.dumps(rel_auto, indent=4))

if manual_override:
    with open("map_manual.json", "w") as map_:
        map_.write(json.dumps(rel_manual, indent=4))