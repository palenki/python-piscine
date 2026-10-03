class Plant:
	def __init__(self, name: str, height: float, age_days: int):
		self.name = name
		self.height = height
		self.age_days = age_days


	def show(self) -> None:
		print(f"\033[7;35;47m{self.name}\033[m: {self.height}cm, {self.age_days} days old")

	def grow(self, growth: float) -> None:
		self.height = round(self.height + growth, 1)

	def age(self, days: int) -> None:
		self.age_days += days


def main() -> None:
	rose = Plant("Rose", 30, 215)
	rose.show()


if __name__ == "__main__":
	main()
