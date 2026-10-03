#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age_days: int):
        self.name = name
        self.height = height
        self.age_days = age_days

    def show(self) -> None:
        print("{}: {}cm, {} days old".format(self.name, self.height, self.age_days))

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
	print("Created:", end=" ")
	rose.show()
	print("Created:", end=" ")
	oak.show()
	print("Created:", end=" ")
	cactus.show()
	print("Created:", end=" ")
	sunflower.show()
	print("Created:", end=" ")
	fern.show()

if __name__ == "__main__":
    main()
