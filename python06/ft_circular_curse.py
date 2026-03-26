#!/usr/bin/env python3

def testing_late_import() -> None:
    import alchemy.grimoire
    print("\nTesting late import technique:")
    print('record_spell("Lightning", "air"):',
          alchemy.grimoire.record_spell("Lightning", "air"))


def testing_spell_recording() -> None:
    from alchemy.grimoire.spellbook import record_spell
    print("\nTesting spell recording with validation:")
    print('record_spell("Fireball", "fire air"):',
          record_spell("Fireball", "fire air"))
    print('record_spell("Dark Magic", "shadow"):',
          record_spell("Dark Magic", "shadow"))


def testing_ingredients_validation() -> None:
    print("\nTesting ingredient validation:")
    from alchemy.grimoire.validator import validate_ingredients
    print('validate_ingredients("fire air"):',
          validate_ingredients("fire air"))
    print('validate_ingredients("dragon scales"):',
          validate_ingredients("dragon scales"))


def main() -> None:
    print("\n=== Circular Curse Breaking ===")
    testing_ingredients_validation()
    testing_spell_recording()
    testing_late_import()
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
