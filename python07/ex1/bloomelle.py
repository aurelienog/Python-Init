from ex0.creature import Creature
from .capabilities import HealCapability
from typing import Optional, Any


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: Optional[Any]) -> str:
        if target is None:
            return f"{self.name} heals itself and others for a large amount"
        return f"{self.name} heals {target.name} and others for a large amount"
