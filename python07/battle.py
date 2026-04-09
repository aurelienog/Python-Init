#!/usr/bin/env python3
from ex0 import CreatureFactory, FlameFactory, AquaFactory


def create_fighting_creatures(factory1: CreatureFactory,
                              factory2: CreatureFactory) -> None:
    print("Testing battle")
    try:
        creature1 = factory1.create_base()
        creature2 = factory2.create_base()
    except Exception as e:
        print(f"Error creating creatures: {e}")
        return
    print(f"{creature1.describe()}\n vs.\n{creature2.describe()}\n fight!")
    print(creature1.attack())
    print(creature2.attack())


def create_creatures(factory: CreatureFactory) -> None:
    print("Testing factory")
    try:
        base = factory.create_base()
        print(base.describe())
        print(base.attack())
    except Exception as e:
        print(f"Error creating base creatures: {e}")

    try:
        evolved = factory.create_evolved()
    except Exception as e:
        print(f"Error creating evolved creatures: {e}")
        return
    print(evolved.describe())
    print(evolved.attack())
    print("")


def main() -> None:
    flameling = FlameFactory()
    aquabub = AquaFactory()
    create_creatures(flameling)
    create_creatures(aquabub)
    create_fighting_creatures(flameling, aquabub)


if __name__ == "__main__":
    main()
