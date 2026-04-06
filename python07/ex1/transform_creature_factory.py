from ex0 import CreatureFactory
from .morphagon import Morphagon
from .shiftling import Shiftling


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
