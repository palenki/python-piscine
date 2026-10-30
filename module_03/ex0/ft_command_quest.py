#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")

    program_name: str = sys.argv[0]
    args: list[str] = sys.argv[1:]
    total_args: int = len(sys.argv)

    print(f"Program name: {program_name}")

    if not args:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args)}")
        for index in range(len(args)):
            print(f"Argument {index + 1}: {args[index]}")

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
