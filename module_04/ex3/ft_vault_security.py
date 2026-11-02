#! /usr/bin/env python3

def secure_archive(filename: str,
                   mode: str = "read",
                   content: str | None = None
                   ) -> tuple[bool, str]:
    if mode == "read":
        try:
            with open(filename, "r") as file:
                file_content: str = file.read()
                return (True, file_content)
        except OSError as err:
            return (False, str(err))
    elif mode == "write":
        if content is None:
            content = ""
        try:
            with open(filename, "w") as file:
                file.write(content)
                return(True, "Content successfully written to file")
        except OSError as err:
            return(False, str(err))

    return (False, f"Invalid action: '{mode}'")


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    nonexistent: tuple[bool, str] = secure_archive("/not/existing/file")
    print(nonexistent)

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    inaccessible: tuple[bool, str] = secure_archive("/etc/shadow")
    print(inaccessible)

    print("\nUsing 'secure_archive' to read from a regular file:")
    readable: tuple[bool, str] = secure_archive("ancient_fragment.txt")
    print(readable)

    if readable[0]:
        print("\nUsing 'secure_archive'"
              " to write previous content to a new file")
        result_write: tuple[bool, str] = secure_archive(
                "new_vault_file.txt",
                "write",
                readable[1]
        )
        print(result_write)


if __name__ == "__main__":
    main()
