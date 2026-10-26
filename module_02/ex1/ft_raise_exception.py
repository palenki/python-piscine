def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)
    if temp_int < 0:
        raise ValueError(f"{temp_int} is too cold for plants (min 0°C)")
    if temp_int > 40:
        raise ValueError(f"{temp_int} is too hot for plants (max 40°C)")
    return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    test1: str = "25"
    print(f"\nInput data is '{test1}'")
    try:
        temp: int = input_temperature(test1)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error:{err}")

    test2: str = "abc"
    print(f"\nInput data is '{test2}'")
    try:
        temp = input_temperature(test2)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")

    test3: str = "100"
    print(f"\nInput data is '{test3}'")
    try:
        temp = input_temperature(test3)
        print("Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")

    test4: str = "-50"
    print(f"\nInput data is '{test4}'")
    try:
        temp = input_temperature(test4)
        print("Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
