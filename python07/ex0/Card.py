from abc import ABC, abstractmethod
from typing import Union
from enum import Enum


class CardType(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"


class CardRarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: CardRarity) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict[str, Union[str,
                                               dict[str, int], list[str]]]) -> dict[str, Union[str, bool, int]]:
        pass

    def get_card_info(self) -> dict[str, Union[str, bool, int, CardRarity]]:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
            }

    def is_playable(self, available_mana: int) -> bool:
        if available_mana > 3:
            return True
        return False
