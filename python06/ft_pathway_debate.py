#!/usr/bin/env python3


def test_package_access() -> None:
    print("\nTesting Package Access")
    import alchemy.transmutation
    print("alchemy.transmutation.lead_to_gold():",
          alchemy.transmutation.lead_to_gold())
    print("alchemy.transmutation.philosophers_stone():",
          alchemy.transmutation.philosophers_stone())


def test_relative_imports() -> None:
    print("\nTesting Relative Imports (from advanced.py):")
    from alchemy.transmutation.advanced import (philosophers_stone,
                                                elixir_of_life)
    print("philosophers_stone():", philosophers_stone())
    print("elixir_of_life():", elixir_of_life())


def test_absolute_imports() -> None:
    print("\nTesting Absolute Imports (from basic.py):")
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    print("lead_to_gold()", lead_to_gold())
    print("stone_to_gem():", stone_to_gem())


def main() -> None:
    print("\n=== Pathway Debate Mastery ===")
    test_absolute_imports()
    test_relative_imports()
    test_package_access()
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
