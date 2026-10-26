def input_temperature(temp_str: str) -> int:
    return int(temp_str)

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
        temp: int = input_temperature(test2)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")

    print("\nAll tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()
