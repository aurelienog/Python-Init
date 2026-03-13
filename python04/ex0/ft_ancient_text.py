#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        file = open("ancient_fragment.txt", "r")
        print("\nAccessing Storage Vault: ancient_fragment.txt")
        print("Connection established...\n")
        print(file.read())
        print("\nData recovery complete. Storage unit disconnected.")
        file.close()
    except FileNotFoundError:
        print("\nERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
