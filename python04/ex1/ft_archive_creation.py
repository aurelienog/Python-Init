#!/usr/bin/env python3

def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    print("\nInitializing new storage unit: new_discovery.txt")
    try:
        new_file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...")
    except FileNotFoundError:
        print("\nERROR: Storage vault not found. Run data generator first.")
        return
    except (IsADirectoryError, PermissionError, OSError) as e:
        print(f"System error during open: {e}")
        return

    try:
        new_file.write(
            "[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee")
        print("\nInscribing preservation data...")
        write_success = True
    except (ValueError, TypeError, OSError) as e:
        print(f"System error during write: {e}")
    finally:
        new_file.close()

    if write_success:
        try:
            new_file = open("new_discovery.txt", "r")
            print(new_file.read())
        except (UnicodeDecodeError, OSError) as e:
            print(f"\nERROR: read failure ({e})")
        finally:
            new_file.close()
            print("\nData inscription complete. Storage unit sealed.")
            print("Archive 'new_discovery.txt' ready for long-term",
                  "preservation.")


if __name__ == "__main__":
    main()
