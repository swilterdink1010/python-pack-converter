import os
from pathlib import Path

OLD_DIR = Path("./assets/ASSETS_1.8.9")
NEW_DIR = Path("./assets/ASSETS_1.21.10")

REL_FOLDERS = {
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/items")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/item")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/blocks")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/block")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/colormap")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/colormap")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/effect")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/effect")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/armorstand")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/armorstand")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/banner")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/banner")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/cat")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/cat")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/chest")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/chest")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/cow")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/cow")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/creeper")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/creeper")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/endercrystal")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/end_crystal")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/enderdragon")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/enderdragon")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/enderman")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/enderman")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/ghast")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/ghast")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/horse")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/horse")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/horse/armor")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/equipment/horse_body")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/pig")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/pig")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/rabbit")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/rabbit")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/sheep")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/sheep")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/skeleton")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/skeleton")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/slime")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/slime")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/spider")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/spider")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/villager")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/villager")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/wither")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/wither")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/wolf")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/wolf")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/entity/zombie")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/entity/zombie")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/environment")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/environment")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/font")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/font")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/gui")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/gui")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/map")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/map")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/misc")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/misc")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/models")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/models")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/painting")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/painting")),
    Path(os.path.join(OLD_DIR, "assets/minecraft/textures/particle")): 
        Path(os.path.join(NEW_DIR, "assets/minecraft/textures/particle")),
}