from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import WheelWorldWorld

ALL_REGIONS: list[str] = [
    "Menu",
    "Lunardo Island",
    "Tramonto",
    "Wasteland",
    "Mount Send",
]


def create_and_connect_regions(world: WheelWorldWorld) -> None:
    regions = [Region(name, world.player, world.multiworld) for name in ALL_REGIONS]
    world.multiworld.regions += regions

    menu = world.get_region("Menu")
    menu.connect(world.get_region("Lunardo Island"), "Menu to Lunardo Island")

    lunardo = world.get_region("Lunardo Island")
    lunardo.connect(world.get_region("Tramonto"), "Lunardo Island to Tramonto")

    tramonto = world.get_region("Tramonto")
    tramonto.connect(world.get_region("Wasteland"), "Tramonto to Wasteland")

    wasteland = world.get_region("Wasteland")
    wasteland.connect(world.get_region("Mount Send"), "Wasteland to Mount Send")
