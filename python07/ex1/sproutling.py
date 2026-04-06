from ex0.creature import Creature
from .capabilities import HealCapability
from typing import Optional, Any


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: Optional[Any]) -> str:
        if target is None:
            return f"{self.name} heals itself for a small amount"
        return f"{self.name} heals {target.name} for a small amount"
