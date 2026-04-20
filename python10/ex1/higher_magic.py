#!/usr/bin/env python3


from typing import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def spells_caster(target: str, power: int) -> list[str]:
        casted: list[str] = []
        for spell in spells:
            casted.append(spell(target, power))
        return casted

    return spells_caster


def print_combiner() -> None:
    combiner = spell_combiner(fireball, heal)
    s1, s2 = combiner("dragon", 23)
    print("\nTesting spell combiner...")
    print(f"Combined spell result: {s1}, {s2}")


def print_amplifier() -> None:
    print("\nTesting power amplifier...")
    print("Original: 10, Amplified: 30")
    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball('Goblin', 10))


def print_conditional() -> None:
    def strong_enough(target: str, power: int) -> bool:
        return power > 10

    print("\nTesting conditional caster...")

    safe_fireball = conditional_caster(strong_enough, fireball)
    print(f'Failure: {safe_fireball("Goblin", 5)}')
    print(f'Success:{safe_fireball("Wizard", 20)}')


def print_sequence() -> None:
    print("\nTesting spell sequence...")
    caster = spell_sequence([fireball, heal])
    spells = caster("knight", 15)
    for spell in spells:
        print(spell)


def main() -> None:
    print_combiner()
    print_amplifier()
    print_conditional()
    print_sequence()


if __name__ == "__main__":
    main()
