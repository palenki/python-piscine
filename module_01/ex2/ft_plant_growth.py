class Plant:
    def __init__(self) -> None:
        self.name: str = ""
        self.height: float = 0.0
        self.age_days: int = 0

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def grow(self, growth: float) -> None:
        self.height = round(self.height + growth, 1)

    def age(self, days: int) -> None:
        self.age_days = self.age_days + days


def main() -> None:
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.age_days = 30
    initial_height: float = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow(0.8)
        rose.age(1)
        rose.show()

    total_growth = round(rose.height - initial_height, 1)
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    main()
