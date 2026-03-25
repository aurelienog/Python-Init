#!/usr/bin/env python3

def first_method() -> None:
    import alchemy.elements
    print("\nMethod 1 - Full module import:")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())


def second_method() -> None:
    print("\nMethod 2 - Specific function import:")
    from alchemy.elements import create_water
    print("create_water():", create_water())


def third_method() -> None:
    print("\nMethod 3 - Aliased import:")
    from alchemy.potions import healing_potion as heal
    print("heal():", heal())


def fourth_method() -> None:
    from alchemy.elements import create_fire, create_earth
    from alchemy.potions import strength_potion
    print("\nMethod 4 - Multiple imports:")
    print("create_earth():", create_earth())
    print("create_fire():", create_fire())
    print("strength_potion():", strength_potion())


def main():
    print("\n=== Import Transmutation Mastery ===")
    first_method()
    second_method()
    third_method()
    fourth_method()
    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    main()
