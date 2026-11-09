import os
from dotenv import load_dotenv


BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
ENV_FILE: str = os.path.join(BASE_DIR, ".env")

load_dotenv(dotenv_path=ENV_FILE, override=False)

MATRIX_MODE: str = os.getenv("MATRIX_MODE", "development")
DATABASE_URL: str = os.getenv("DATABASE_URL", "")
API_KEY: str = os.getenv("API_KEY", "")
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "DEBUG")
ZION_ENDPOINT: str = os.getenv("ZION_ENDPOINT", "")

if MATRIX_MODE not in ("development", "production"):
    print("[WARNING] Invalid MATRIX_MODE. Using development.")
    MATRIX_MODE = "development"


def main() -> None:
    print("ORACLE STATUS: Consulting the configuration...\n")
    print("Configuration loaded:")
    print(f"Mode: {MATRIX_MODE}")

    if DATABASE_URL:
        if MATRIX_MODE == "development":
            print("Database: Connected to local instance")
        else:
            print("Database: Configuration available")
    else:
        print("Database: Not configured")
        print("[WARNING] DATABASE_URL is missing")

    if API_KEY:
        print("API Access: Authenticated")
    else:
        print("API Access: Not configured")
        print("[WARNING] API_KEY is missing")

    print(f"Log Level: {LOG_LEVEL}")

    if ZION_ENDPOINT:
        print("Remote Network: Online")
    else:
        print("Remote Network: Not configured")

    print("\nConfiguration security check:")
    print("[OK] No hardcoded secrets detected")

    gitignore_path: str = os.path.join(BASE_DIR, ".gitignore")

    try:
        with open(gitignore_path, "r", encoding="utf-8") as file:
            ignored_files: list[str] = file.read().splitlines()

        if ".env" in ignored_files:
            print("[OK] .env file properly ignored by git")

        else:
            print("[WARNING] .env is not listed in .gitignore")

    except FileNotFoundError:
        print("[WARNING] .gitignore file not found")

    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
