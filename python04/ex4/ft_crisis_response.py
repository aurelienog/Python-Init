#!/usr/bin/env python3

def report_crisis() -> None:
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("new_discovery.txt", "w") as file:
            file.write(
                "[ENTRY 001] New quantum algorithm discovered"
                "\n[ENTRY 002] Efficiency increased by 347%"
                "\n[ENTRY 003] Archived by Data Archivist trainee"
                )
            print("Data inscription complete. Storage unit sealed.")
            print("Archive 'new_discovery.txt' ready for long-term",
                  "preservation.")
    except PermissionError:
        print("ERROR writing file: Permission denied")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    report_crisis()


if __name__ == "__main__":
    main()
