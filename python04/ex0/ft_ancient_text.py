#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        file = open("ancient_fragment.txt", "r")
        print("\nAccessing Storage Vault: ancient_fragment.txt")
        print("Connection established...\n")

    except FileNotFoundError:
        print("\nERROR: Storage vault not found. Run data generator first.")
        return
    except PermissionError:
        print("\nERROR: access denied")
        return
    except IsADirectoryError:
        print("\nERROR: target is a directory, not a file")
        return
    except OSError as e:
        print(f"\nERROR: system failure ({e})")
        return

    try:
        content = file.read()
        print("RECOVERED DATA:")
        print(content)
        print("\nData recovery complete.", end=" ")
    except UnicodeDecodeError:
        print("\nERROR: corrupted or incompatible encoding")
    except OSError as e:
        print(f"\nERROR: read failure ({e})")
    finally:
        file.close()
        print("Storage unit disconnected.")


if __name__ == "__main__":
    main()
