import importlib


def check_dependency(module_name: str,
                     description: str) -> bool:
    try:
        module = importlib.import_module(module_name)
        version: str = getattr(module, "__version__", "unknown")

        print(f"[OK] {module_name} ({version} - {description} ready)")
        return True

    except ImportError:
        print(f"[MISSING] {module_name} is not installed.")
        print(f" pip: pip install {module_name}")
        print(f" Poetry: poetry add {module_name}")
        return False
    except AttributeError:
        print(f"[WARNING] {module_name} is installed,"
              " but version is unavailable.")
        return True


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")

    pandas_ok: bool = check_dependency("pandas", "Data manipulation")

    numpy_ok: bool = check_dependency("numpy", "Numerical computation")

    print("\npip vs Poetry:")
    print("requirements.txt declares what to install; "
          "pip resolves it at install time.")
    print("pyproject.toml declares the same constraints, and "
          "Poetry pins the resolved versions in poetry.lock\n"
          "so every install is identical.")
    if pandas_ok and numpy_ok:
        print("\nAll reagents present and accounted for.")
    else:
        print("\nSome reagents are missing.")
        print("Install them using pip or Poetry.")


if __name__ == "__main__":
    main()
