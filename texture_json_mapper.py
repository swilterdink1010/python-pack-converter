#
#   Program meant to parse game assets, pair them, and store their file
#   location mappings in a json file.
#
#   This code was originally written to map version 1.8.9 textures
#   to version 1.21.10. The paths in REL_FOLDERS are subject to change
#   as Mojang updates Minecraft's asset file structure.
#
#   Minecraft's game assets must be legally acquired and their paths
#   must be entered into the OLD_DIR and NEW_DIR variables manually for
#   this code to work.
#

from pathlib import Path
import os
import sys
import json

OLD_DIR = Path("./ASSETS_1.8.9")
NEW_DIR = Path("./ASSETS_1.21.10")

if not (OLD_DIR.exists() and NEW_DIR.exists()):
    sys.exit("Asset directories could not be found.")

REL_FOLDERS = {
    Path(os.path.join(OLD_DIR,"assets/minecraft/textures/items")): 
        Path(os.path.join(NEW_DIR,"assets/minecraft/textures/item")),
    Path(os.path.join(OLD_DIR,"assets/minecraft/textures/blocks")): 
        Path(os.path.join(NEW_DIR,"assets/minecraft/textures/block"))
               }

rel_auto = {}
rel_manual = {}

def rel_check(item):
    for rel in REL_FOLDERS.keys():
        for path in item.parents:
            if rel == path:
                item_check(item, REL_FOLDERS[rel])
    
def item_check(item, rel):
    if Path(os.path.join(rel,item.name)).exists():
        # Put into a dictionary for automatic recording
        rel_auto[str(item)] = os.path.join(rel,item.name)
    else:
        # Put into a list for manual recording
        rel_manual[str(item)] = str(rel)

def dir_iterate(dir):
    for item in dir.iterdir():
        if item.is_dir():
            dir_iterate(item)
        else:
            rel_check(item)

dir_iterate(OLD_DIR)

with open("map.json", "w") as map:
    map.write(json.dumps(rel_auto, indent=4))