class Plant:
    name: str
    _height: float
    _age_days: int

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self._height = 0.0
        self._age_days = 0

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

    def grow(self, growth: float) -> None:
        new_height = round(self._height + growth, 1)
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self._height = new_height

    def age(self, days: int) -> None:
        if days < 0:
            print(f"{self.name}: Error, plant can't age negative")
        else:
            self._age_days += days

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def set_age(self, age_days: int) -> None:
        if age_days < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_days = age_days
            print(f"Age updated: {self._age_days} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days


def main() -> None:
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created:", end=" ")
    rose.show()
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-10)
    rose.set_age(-10)
    print("")
    print("Current state:", end=" ")
    rose.show()


if __name__ == "__main__":
    main()
