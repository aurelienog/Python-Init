#!/usr/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from typing import Protocol, Any


class HealingCreature(Protocol):
    def describe(self) -> str: ...
    def attack(self) -> str: ...
    def heal(self, target: Any | None) -> str: ...


class TransformingCreature(Protocol):
    def describe(self) -> str: ...
    def attack(self) -> str: ...
    def transform(self) -> str: ...
    def revert(self) -> str: ...


def transformed_demo(factory: TransformCreatureFactory) -> None:
    print("\nTesting Creature with transform capability")
    try:
        base: TransformingCreature = factory.create_base()
        evolved: TransformingCreature = factory.create_evolved()
    except Exception as e:
        print("creation error:", e)
        return
    print(" base:\n"
          f"{base.describe()}\n"
          f"{base.attack()}\n"
          f"{base.transform()}\n"
          f"{base.attack()}\n"
          f"{base.revert()}")
    print(" evolved:\n"
          f"{evolved.describe()}\n"
          f"{evolved.attack()}\n"
          f"{evolved.transform()}\n"
          f"{evolved.attack()}\n"
          f"{evolved.revert()}")


def healing_demo(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    try:
        base: HealingCreature = factory.create_base()
        evolved: HealingCreature = factory.create_evolved()
    except Exception as e:
        print("creation error:", e)
        return
    print(" base:\n"
          f"{base.describe()}\n"
          f"{base.attack()}\n"
          f"{base.heal(None)}")
    print(" evolved:\n"
          f"{evolved.describe()}\n"
          f"{evolved.attack()}\n"
          f"{evolved.heal(None)}")


def main() -> None:
    healers_factory = HealingCreatureFactory()
    healing_demo(healers_factory)
    transformers_factory = TransformCreatureFactory()
    transformed_demo(transformers_factory)


if __name__ == "__main__":
    main()
