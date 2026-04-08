#!/usr/bin/env python3

import os


def print_env() -> None:
    try:
        from dotenv import load_dotenv
        load_dotenv(".env")
    except ModuleNotFoundError:
        print("[KO] dotenv is not installed")
        print("Please run: pip install -r requirements.txt")
        return
    print("\nORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print(f"Mode: {os.getenv('MATRIX_MODE')}")
    print(f"Database: {os.getenv('DATABASE_URL')}")
    if os.getenv('API_KEY'):
        print("API Access: Authenticated")
    else:
        print("API Access: Unauthenticated")
    print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    print(f"Zion Network: {os.getenv('ZION_ENDPOINT')}")
    print("\nThe Oracle sees all configurations")


def main() -> None:
    print_env()


if __name__ == "__main__":
    main()
