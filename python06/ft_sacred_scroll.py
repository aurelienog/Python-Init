#!/usr/bin/env python3

import alchemy


def access_module() -> None:
    print("Testing direct module access:")
    print("alchemy.elements.create_fire():", end=" ")
    print(alchemy.elements.create_fire())
    print("alchemy.elements.create_water():", end=" ")
    print(alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", end=" ")
    print(alchemy.elements.create_earth())
    print("alchemy.elements.create_air():", end=" ")
    print(alchemy.elements.create_air())


def access_package_level() -> None:
    print("\nTesting package-level access (controlled by __init__.py):")

    print("alchemy.create_fire():", end=" ")
    print(alchemy.create_fire())
    print("alchemy.create_water():", end=" ")
    print(alchemy.create_water())
    print("alchemy.create_earth():", end=" ")
    try:
        print(alchemy.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")

    print("alchemy.create_air():", end=" ")
    try:
        print(alchemy.create_air())
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nPackage metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


def main() -> None:
    print("\n=== Sacred Scroll Mastery ===\n")
    try:
        access_module()
    except Exception as e:
        print(f"direct access error: {e}")
    access_package_level()


if __name__ == "__main__":
    main()
