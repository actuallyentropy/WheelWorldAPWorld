from __future__ import annotations

from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule

from .items import LEGENDARY_PARTS, SYNTHETIC_PARTS

if TYPE_CHECKING:
    from .world import WheelWorldWorld


def set_all_rules(world: WheelWorldWorld) -> None:
    set_entrance_rules(world)
    set_location_rules(world)
    set_completion_condition(world)


def set_entrance_rules(world: WheelWorldWorld) -> None:
    legendary_tuple = tuple(LEGENDARY_PARTS)
    synthetic_tuple = tuple(SYNTHETIC_PARTS)

    set_rule(
        world.get_entrance("Lunardo Island to Tramonto"),
        lambda state: state.has("Commuter Wheel", world.player),
    )
    set_rule(
        world.get_entrance("Tramonto to Wasteland"),
        lambda state: state.has_all(legendary_tuple, world.player),
    )
    set_rule(
        world.get_entrance("Wasteland to Mount Send"),
        lambda state: state.has_all(synthetic_tuple, world.player),
    )


def set_location_rules(world: WheelWorldWorld) -> None:
    set_rule(
        world.get_location("Lunardo Hill Boys"),
        lambda state: state.has("Commuter Wheel", world.player),
    )


def set_completion_condition(world: WheelWorldWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has(
        "Victory", world.player
    )
