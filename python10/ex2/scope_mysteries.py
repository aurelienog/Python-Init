#!/usr/bin/env python3

from typing import Callable, Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    base = initial_power

    def accumulate(num: int) -> int:
        nonlocal base
        base += num
        return base

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")

    vault: dict[str, Callable] = {
        "store": store,
        "recall": recall
    }
    return vault


def print_mage_counter() -> None:
    print("\nTesting mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f'counter_a call 1: {counter_a()}')
    print(f'counter_a call 2: {counter_a()}')
    print(f'counter_b call 1: {counter_b()}')


def print_accumulator() -> None:
    print("\nTesting spell accumulator...")
    accumulator1 = spell_accumulator(100)
    print(f'Base 100, add 20: {accumulator1(20)}')
    print(f'Base 100, add 30: {accumulator1(30)}')


def print_factory() -> None:
    print("\nTesting enchantment factory..")
    flaming_factory = enchantment_factory("Flaming")
    frozen_factory = enchantment_factory("Frozen")
    print(flaming_factory("Sword"))
    print(frozen_factory("Shield"))


def print_memory() -> None:
    print("\nTesting memory vault...")
    vault = memory_vault()
    data = [{"secret": 42}]
    # data = [{"secret": 42}, {"pwd": "secreto"}, {"sec": "Oops"}]
    for item in data:
        for key, value in item.items():
            print(f"Store '{key}' = {value}")
            vault["store"](f"{key}", value)

    for item in data:
        for key, value in item.items():
            print(f"Recall '{key}': {vault['recall'](key)}")

    print(f"Recall 'unknown': {vault['recall']('unknown')}")


def main() -> None:
    print_mage_counter()
    print_accumulator()
    print_factory()
    print_memory()


if __name__ == "__main__":
    main()
