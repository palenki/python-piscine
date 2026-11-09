import sys
import site
import os


def main() -> None:
    print("LABORATORY STATUS: ", end="")
    in_venv: bool = sys.prefix != sys.base_prefix

    print("The laboratory is sealed" if in_venv
          else "You are working in the open")

    print(f"\nCurrent Python: {sys.executable}")

    if in_venv:
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.\n")

        print("Reagent installation path:")

        for path in site.getsitepackages():
            print(path)
    else:
        print("Virtual Environment: None detected")
        print("\nWARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print("\nTo seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate    # On Unix")
        print("lab_env\\Scripts\\activate     # On Windows")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
