def ft_count_harvest_recursive() -> None:
    harvest_day = int(input("Days until harvest: "))

    def count(current: int) -> None:
        if current > harvest_day:
            return
        print(f"Day {current}")
        count(current + 1)

    count(1)
    print("Harvest time!")
