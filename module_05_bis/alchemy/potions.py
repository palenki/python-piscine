from elements import create_fire, create_water
from .elements import create_earth, create_air


def healing_potion() -> str:
    earth: str = create_earth()
    air: str = create_air()

    return (
        f"Healing potion brewed with '{earth}' "
        f"and '{air}'"
    )


def strength_potion() -> str:
    fire = create_fire()
    water = create_water()

    return (
        f"Strength potion brewed with '{fire}' "
        f"and '{water}'"
    )
