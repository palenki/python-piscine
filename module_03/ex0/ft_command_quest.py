import sys


def main():
    print("=== Command Quest ===")

    program_name = sys.argv[0]
    args = sys.argv[1:]
    total_args = len(sys.argv)

    print(f"Program name: {program_name}")

    if not args:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args)")
        for i, arg in enumerate(args, start=1):
            print(f"Argument {i}: {arg}")

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
