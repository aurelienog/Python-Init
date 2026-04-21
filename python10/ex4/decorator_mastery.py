#!/usr/bin/env python3

from functools import wraps
from typing import Callable, Any
import time
import random


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {(end_time - start_time):.4f} seconds")
        return result

    return wrapper


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Result: Fireball cast!"


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any | str:
            power = args[-1]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempts += 1

                    if attempts < max_attempts:
                        print("Spell failed, retrying..."
                              f" (attempt {attempts}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper
    return decorator


@retry_spell(3)
def spelled() -> str:
    time.sleep(0.1)
    if random.random() < 0.8:
        raise ValueError("Spell fizzled")
    return "Waaaaaaagh spelled !"


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (isinstance(name, str)
                and name.replace(" ", "").isalpha()
                and len(name) >= 3)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")
    print(fireball())

    print("\nTesting retrying spell...")
    print(spelled())

    mage = MageGuild()
    print("\nTesting MageGuild...")
    print(mage.validate_mage_name("henry7"))
    print(mage.validate_mage_name("5s"))
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Fireball", 5))


if __name__ == "__main__":
    main()
