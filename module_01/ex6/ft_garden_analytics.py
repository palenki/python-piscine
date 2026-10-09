class Plant:
    class Stats:
        _grow_calls: int
        _age_calls: int
        _show_calls: int

        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def count_grow(self) -> None:
            self._grow_calls += 1

        def count_age(self) -> None:
            self._age_calls += 1

        def count_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, "
                  f"{self._show_calls} show")

    name: str
    _height: float
    _age_days: int
    _stats: Stats

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self._height = 0.0
        self._age_days = 0
        self._stats = Plant.Stats()

        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self._height = height
        if age_days < 0:
            print(f"{self.name}: Error, age can't be negative")
        else:
            self._age_days = age_days

    def show(self) -> None:
        print(f"{self.name}: {self.get_height():.1f}cm, "
              f"{self._age_days} days old")
        self._stats.count_show()

    def grow(self, growth: float = 1.0) -> None:
        new_height = round(self._height + growth, 1)
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self._height = new_height
            self._stats.count_grow()

    def age(self, days: int = 1) -> None:
        if days < 0:
            print(f"{self.name}: Error, plant can't age negative")
        else:
            self._age_days += days
            self._stats.count_age()

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative\n"
                  "Height update rejected")
        else:
            self._height = round(height, 1)
            print(f"Height updated: {self._height}cm")

    def set_age(self, age_days: int) -> None:
        if age_days < 0:
            print(f"{self.name}: Error, age can't be negative\n"
                  "Age update rejected")
        else:
            self._age_days = round(age_days, 2)
            print(f"Age updated: {self._age_days} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    @staticmethod
    def more_than_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def make_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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
    class TreeStats(Plant.Stats):
        _shade_calls: int

        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def count_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    _trunk_diameter: float

    def __init__(self, name: str, height: float,
                 age_days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age_days)
        self._trunk_diameter = trunk_diameter
        self._stats = Tree.TreeStats()

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height:.1f}cm long and "
              f"{self._trunk_diameter:.1f}cm wide.")
        self._stats.count_shade()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant._stats.display()


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


class Seed(Flower):
    _seeds: int

    def __init__(self, name: str, height: float,
                 age_days: int, color: str) -> None:
        super().__init__(name, height, age_days, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

def main() -> None:
    print("=== Garden statistics ===\n"
          "=== Check year-old\n"
          f"Is 30 days more than a year? -> {Plant.more_than_year(30)}\n"
          f"Is 400 days more than a year? -> {Plant.more_than_year(400)}\n\n"
          "=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.grow(8)
    rose.show()
    display_plant_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.age(20)
    sunflower.grow(30.0)
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print("\n=== Anonymous")
    anonymous = Plant.make_anonymous()
    anonymous.show()
    display_plant_stats(anonymous)


if __name__ == "__main__":
    main()
