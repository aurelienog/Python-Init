from ex0 import CreatureFactory
from .bloomelle import Bloomelle
from .sproutling import Sproutling


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()
