from ex0.Card import Card, CardRarity, CardType
from typing import Union


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: CardRarity, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = CardType.CREATURE

    def play(self, game_state: dict[str, Union[str,
                                               dict[str, Union[int, list:[Card]]], list[str]]]) -> dict[str, Union[str, int]]:
        game_state["player"]["mana"] -= self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: Card) -> dict[str, Union[str, bool, int]]:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> dict[str, Union[str, bool, int]]:
        info: dict[str, Union[str, bool, int]] = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info
