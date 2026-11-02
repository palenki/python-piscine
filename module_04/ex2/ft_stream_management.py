#!/usr/bin/env python3

import sys
import typing


def read_file(file_name: str) -> typing.Optional[str]:
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Acessing file '{file_name}'\n")

    file: typing.Optional[typing.IO[str]] = None
    content: typing.Optional[str] = None

    try:
        file = open(file_name, "r")
        content = file.read()
        sys.stdout.write("---\n\n")
        sys.stdout.write(content)
        sys.stdout.write("\n\n---\n")
    except OSError as err:
        sys.stderr.write(f"[STDERR] Error opening file '{file_name}': {err}\n")
    finally:
        if file is not None and not file.closed:
            file.close()
            sys.stdout.write(f"File '{file_name}' closed\n\n")

    return content


def transform_data(content: str) -> str:
    lines: list[str] = content.splitlines()
    transformed_lines: list[str] = []

    for line in lines:
        transformed_lines.append(f"{line}#")

    transformed_content: str = "\n".join(transformed_lines) + "\n"

    sys.stdout.write("Transform data:\n\n")
    sys.stdout.write("---\n\n")
    sys.stdout.write(transformed_content)
    sys.stdout.write("\n---\n")

    return transformed_content


def save_file(save_filename: str, content: str) -> None:
    sys.stdout.write(f"Saving data to '{save_filename}'\n")

    file_obj: typing.Optional[typing.IO[str]] = None

    try:
        file_obj = open(save_filename, "w")
        file_obj.write(content)
        sys.stdout.write(f"Data saved in file '{save_filename}'.\n")
    except OSError as err:
        sys.stderr.write(f"[STDERR] Error opening file '{save_filename}':"
                         f" {err}\n")
    finally:
        if file_obj is not None and not file_obj.closed:
            file_obj.close()


def main() -> None:
    if len(sys.argv) != 2:
        sys.stdout.write("Usage: ft_stream_management.py <file>\n")
        return

    filename: str = sys.argv[1]

    content: typing.Optional[str] = read_file(filename)
    if content is None:
        return

    transformed_content: str = transform_data(content)

    sys.stdout.write("Enter new file name (or empty):")
    sys.stdout.flush()

    saved_filename: str = sys.stdin.readline().rstrip("\r\n")
    if not saved_filename:
        sys.stdout.write("Not saving data.\n")
        return

    save_file(saved_filename, transformed_content)


if __name__ == "__main__":
    main()
