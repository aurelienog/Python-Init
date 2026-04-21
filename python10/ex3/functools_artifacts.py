#!/usr/bin/env python3

from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    match operation:
        case "add":
            return reduce(add, spells)
        case "multiply":
            return reduce(mul, spells)
        case "max":
            return max(spells)
        case "min":
            return min(spells)
        case _:
            raise ValueError(f"Unknown operation: {operation}")


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{power} {element} {target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "earth": partial(base_enchantment, 50, "earth")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatcher(value: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @dispatcher.register(str)
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @dispatcher.register(list)
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    return dispatcher


def print_dispatcher() -> None:
    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, "es", 8]))
    print(dispatcher({"name": "unknown"}))


def print_fibonacci() -> None:
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(memoized_fibonacci.cache_info())
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(memoized_fibonacci.cache_info())


def print_partial_enchanter() -> None:
    print("\nTesting partial_enchanter...")
    enchanter = partial_enchanter(base_enchantment)
    print(enchanter["fire"]("sword"))


def print_reducer() -> None:
    print("\nTesting spell reducer...")
    print(f'Sum: {spell_reducer([80, 20], "add")}')
    print(f'Product: {spell_reducer([24, 10000], "multiply")}')
    print(f'Max: {spell_reducer([10, 40, 2, 36], "max")}')


def main() -> None:
    print_reducer()
    print_partial_enchanter()
    print_fibonacci()
    print_dispatcher()


if __name__ == "__main__":
    main()
