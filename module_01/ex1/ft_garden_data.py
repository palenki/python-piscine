class Plant:
    def __init__(self) -> None:
        self.name: str = "name"
        self.height: float = 0
        self.age: int = 0

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")
    flower1 = Plant()
    flower1.name = "Rose"
    flower1.height = 25
    flower1.age = 30
    flower1.show()

    flower2 = Plant()
    flower2.name = "Sunflower"
    flower2.height = 80
    flower2.age = 45
    flower2.show()

    flower3 = Plant()
    flower3.name = "Cactus"
    flower3.height = 15
    flower3.age = 120
    flower3.show()


if __name__ == "__main__":
    main()
