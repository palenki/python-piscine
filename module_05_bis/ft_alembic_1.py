import alchemy


def main() -> None:
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")

    print("Testing create_air:", alchemy.create_air())

    print(
        "Now show that not all functions can be reached\n"
        "This will raise an exception!"
    )
    try:
        print("Testing the hidden create_earth:")
        print(alchemy.create_earth())
    except Exception as err:
        print(f"Excepted error: {err}")


if __name__ == "__main__":
    main()
