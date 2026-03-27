#!/usr/bin/env python3

from ex0.Card import Card, CardRarity
from ex0.CreatureCard import CreatureCard
from typing import Union


def test_abstract_design(card: Card) -> None:
    print("\nTesting Abstract Base Class Design:")
    print("\nCreatureCard Info:")
    print(card.get_card_info())


def play_creature(creature: CreatureCard,
                  game_state: dict[str, Union[str,
                                              dict[str, int | Card], list[str]]]):
    print(f"\nPlaying {creature.name} with {game_state["player"]["mana"]} mana available")
    if creature.is_playable(game_state["player"]["mana"]):
        print("Playable: True")
        game_state["battlefield"] = [*game_state["battlefield"], creature]
        print("Play result:", creature.play(game_state))


def attack(attacker: CreatureCard, target: Card):
    print(f"\n{attacker.name} attacks {target.name}")
    print("Attack result:", attacker.attack_target(target))


def main() -> None:
    print("\n=== DataDeck Card Foundation ===")
    creature = CreatureCard("Fire Dragon", 5, CardRarity.LEGENDARY, 7, 5)
    game_state: dict[str, Union[str,
                                dict[str, int], list[str]]] = {
        "player": {
            "mana": 6,
            "health": 20
        },
        "enemy": {
            "health": 15
        },
        "battlefield": []
    }
    test_abstract_design(creature)
    play_creature(creature, game_state)
    goblin = CreatureCard("Goblin Warrior", 3, CardRarity.COMMON, 3, 4)
    attack(creature, goblin)
    print("\nTesting insufficient mana (3 available):")
    print(creature.is_playable(game_state["player"]["mana"]))
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
