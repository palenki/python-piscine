class GardenError(Exception):
    def __init__(self, message: str = "Garden Error occurred") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_plant(plant: str, health: int) -> None:
    if health < 42:
        raise PlantError(f"The {plant} plant is wilting!")


def test_water(water_tank: int) -> None:
    if water_tank < 42:
        raise WaterError("Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        test_plant("tomato", 40)
    except PlantError as err:
        print(f"Caught PlantError: {err}")

    print("\nTesting WaterError...")
    try:
        test_water(40)
    except WaterError as err:
        print(f"Caught WaterError: {err}")

    print("\nTesting catching all garden errors...")
    try:
        test_plant("tomato", 40)
    except GardenError as err:
        print(f"Caught GardenError: {err}")
    try:
        test_water(40)
    except GardenError as err:
        print(f"Caught GardenError: {err}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
