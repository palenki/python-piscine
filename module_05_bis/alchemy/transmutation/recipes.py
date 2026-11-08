from elements import create_fire
from alchemy.elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    air: str = create_air()
    strength: str = strength_potion()
    fire: str = create_fire()

    return (
        f"Recipe transmuting Lead to Gold: "
        f"brew '{air}' an '{strength}' "
        f"mixed with '{fire}'"
    )
