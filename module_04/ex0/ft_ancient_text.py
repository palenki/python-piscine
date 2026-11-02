#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Acessing file '{filename}'")

    file: typing.Optional[typing.IO[str]] = None

    try:
        file = open(filename, "r")
        content: str = file.read()
        print("---\n")
        print(content, end="")
        print("\n---")
    except OSError as err:
        print(f"Error opening file '{filename}': {err}")
    finally:
        if file is not None and not file.closed:
            file.close()
            print(f"File '{filename} closed'")


if __name__ == "__main__":
    main()
