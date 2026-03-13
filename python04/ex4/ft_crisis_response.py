#!/usr/bin/env python3


def handle_crisis(documents: list) -> None:
    for doc in documents:
        try:
            with open(doc, "r") as file:
                content = file.read()
            print(f"ROUTINE ACCESS: Attempting access to '{doc}'...")
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed\n")
        except FileNotFoundError:
            print(f"CRISIS ALERT: Attempting access to '{doc}'...")
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable\n")
        except PermissionError:
            print(f"CRISIS ALERT: Attempting access to '{doc}'...")
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained\n")
        except Exception:
            print(f"CRISIS ALERT: Attempting access to '{doc}'...")
            print("RESPONSE: Unexpected system anomaly")
            print("STATUS: Crisis handled, system stable\n")


def main() -> None:
    documents = ["lost_archive.txt", "classified_vault.txt",
                 "standard_archive.txt"]
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    handle_crisis(documents)
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
