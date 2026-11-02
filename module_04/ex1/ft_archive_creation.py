#!/usr/bin/env python3

import sys
import typing


def read_file(file_name: str) -> typing.Optional[str]:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Acessing file '{file_name}'")

    file: typing.Optional[typing.IO[str]] = None
    content: typing.Optional[str] = None

    try:
        file = open(file_name, "r")
        content = file.read()
        print("---\n")
        print(content, end="")
        print("\n---")
    except OSError as err:
        print(f"Error opening file '{file_name}': {err}")
    finally:
        if file is not None and not file.closed:
            file.close()
            print(f"File '{file_name} closed'")

    return content


def transform_data(content: str) -> str:
    lines: list[str] = content.splitlines()
    transformed_lines: list[str] = []

    for line in lines:
        transformed_lines.append(f"{line}#")

    transformed_content: str = "\n".join(transformed_lines) + "\n"

    print("Transform data:")
    print("---\n")
    print(transformed_content, end="")
    print("\n---")

    return transformed_content


def save_file(save_filename: str, content: str) -> None:
    print(f"Saving data to '{save_filename}'")

    file_obj: typing.Optional[typing.IO[str]] = None

    try:
        file_obj = open(save_filename, "w")
        file_obj.write(content)
        print(f"Data saved in file '{save_filename}'")
    except OSError as err:
        print(f"Error saving file '{save_filename}': {err}")
    finally:
        if file_obj is not None and not file_obj.closed:
            file_obj.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename: str = sys.argv[1]

    content: typing.Optional[str] = read_file(filename)
    if content is None:
        return

    transformed_content: str = transform_data(content)

    saved_filename: str = input("Enter new file name (or empty): ")
    if not saved_filename:
        print("Not saving data.")
        return

    save_file(saved_filename, transformed_content)


if __name__ == "__main__":
    main()
