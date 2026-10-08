class Plant:
    name: str
    _height: float
    _age_days: int

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self._height = 0.0
        self._age_days = 0

        if height < 0:
            print("{self.name}: Error, height can't be negative")
        else:
            self._height = height
        if age_days < 0:
            print("{self.name}: Error, age can't be negative")
        else:
            self._age_days = age_days

    def show(self) -> None:
        print(f"{self.name}: {self.get_height():.1f}cm, "
              f"{self._age_days} days old")

    def grow(self, growth: float = 1.0) -> None:
        new_height = round(self._height + growth, 1)
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self._height = new_height

    def age(self, days: int = 1) -> None:
        if days < 0:
            print(f"{self.name}: Error, plant can't age negative")
        else:
            self._age_days += days

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = round(height, 1)
            print(f"Height updated: {self._height}cm")

    def set_age(self, age_days: int) -> None:
        if age_days < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_days = round(age_days, 2)
            print(f"Age updated: {self._age_days} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days


class Flower(Plant):
    _color: str
    _bloomed: bool

    def __init__(self, name: str, height: float,
                 age_days: int, color: str) -> None:
        super().__init__(name, height, age_days)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        if self._bloomed:
            print(f" Color: {self._color}\n"
                  f" {self.name} is blooming beautifully!")
        else:
            print(f" Color: {self._color}\n {self.name} has not bloomed yet")


class Tree(Plant):
    _trunk_diameter: float

    def __init__(self, name: str, height: float,
                 age_days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age_days)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height:.1f}cm long and "
              f"{self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    _harvest_season: str
    _nutritional_value: float

    def __init__(self, name: str, height: float,
                 age_days: int, harvest_season: str) -> None:
        super().__init__(name, height, age_days)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self, growth: float = 1.0) -> None:
        super().grow(growth)
        self._nutritional_value = self._nutritional_value + 0.5

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value = self._nutritional_value + 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}"
              f"\n Nutritional value: {self._nutritional_value:.0f}")


def main() -> None:
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200, 365, 5)
    tomato = Vegetable("Tomato", 5, 10, "April")

    print("=== Garden Plant Types ===\n===Flower")
    rose.show()
    rose.bloom()
    print("[asking the rose to bloom]")
    rose.show()

    print("\n=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(1, 21):
        tomato.age(1)
        tomato.grow(2.1)
    tomato.show()


if __name__ == "__main__":
    main()
