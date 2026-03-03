from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules
from .options import WheelWorldOptions
from .web_world import WheelWorldWebWorld


class WheelWorldWorld(World):
    """
    Wheel World is a cycling adventure game set in a vibrant open world.
    Collect bike parts to build and customize your ultimate bicycle.
    """

    game = "Wheel World"
    web = WheelWorldWebWorld()

    options_dataclass = WheelWorldOptions
    options: WheelWorldOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.WheelWorldItem:
        return items.create_item(self, name)

    def get_filler_item_name(self) -> str:
        return "Corp Wheel"

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {}
