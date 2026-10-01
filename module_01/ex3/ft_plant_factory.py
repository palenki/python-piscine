class Plant:
    def __init__(self, name: str, height: float, age_days: int):
        self.name = name
        self.height = height
        self.age_days = age_days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def grow(self, growth) -> None:
        self.height = round(self.height + growth, 1)

    def age(self, days) -> None:
        self.age_days += days


def main() -> None:
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    print("=== Plant Factory Output ===")
    


if __name__ == "__main__":
    main()
