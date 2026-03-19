#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    print("\nInitiating secure vault access...")
    try:
        with open("classified_data.txt", "r") as file:
            print("Vault connection established with failsafe protocols")
            print("\nSECURE EXTRACTION:")
            data = file.read()
            print(data)
    except (OSError, UnicodeDecodeError) as e:
        print(f"ERROR during secure extraction: {e}")
        return

    print("\nSECURE PRESERVATION:")
    try:
        with open("security_protocols.txt", "r") as security_file:
            security_data = security_file.read()

        with open("new_protocol.txt", "w") as security_file:
            security_file.write(security_data)

    except (UnicodeDecodeError, OSError) as e:
        print(f"ERROR during preservation: {e}")
        return

    print(security_data)
    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
