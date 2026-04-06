from abc import ABC, abstractmethod
from ex0.creature import Creature
from typing import Protocol, Any, runtime_checkable, cast


@runtime_checkable
class HealingCreature(Protocol):
    def describe(self) -> str: ...
    def attack(self) -> str: ...
    def heal(self, target: Any | None) -> str: ...


@runtime_checkable
class TransformingCreature(Protocol):
    def describe(self) -> str: ...
    def attack(self) -> str: ...
    def transform(self) -> str: ...
    def revert(self) -> str: ...


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        try:
            creature.describe()
            creature.attack()
            return True
        except Exception:
            return False

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise Exception("Invalid Creature for this normal strategy")
        return creature.attack()


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformingCreature):
            return True
        return False

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise Exception(f"Invalid Creature {creature.name} for this"
                            " aggressive strategy")
        actor: TransformingCreature = cast(TransformingCreature, creature)
        return (f"{actor.transform()}\n"
                f"{actor.attack()}\n"
                f"{actor.revert()}")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealingCreature):
            return True
        return False

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise Exception(f"Invalid Creature {creature.name} for this"
                            "defensive strategy")
        actor: HealingCreature = cast(HealingCreature, creature)
        return (f"{actor.attack()}\n"
                f"{actor.heal(None)}")
