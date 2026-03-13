#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")
    with open("classified_data.txt", "r") as file:
        print("Vault connection established with failsafe protocols")
        print("\nSECURE EXTRACTION:")
        data = file.read()
        print(data)
    print("\nSECURE PRESERVATION:")
    with open("security_protocols.txt", "r") as security_file:
        security_data = security_file.read()
    with open("new_protocol.txt", "w") as security_file:
        security_file.write(security_data)
        print(security_data)
        print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
