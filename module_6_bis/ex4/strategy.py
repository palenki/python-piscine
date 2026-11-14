from abc import ABC, abstractmethod
from ex3.creature import Creature
from ex3.capability import TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                    f"Invalid Creature '{creature.name}'"
                    " for this normal strategy"
                    )
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                    f"Invalid Creature '{creature.name}'"
                    " for this agressive strategy"
                    )
        return [
            creature.transform(),
            creature.attack(),
            creature.revert(),
                ]
