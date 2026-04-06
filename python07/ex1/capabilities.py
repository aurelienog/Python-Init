from abc import ABC, abstractmethod
from typing import Optional, Any


class HealCapability(ABC):

    @abstractmethod
    def heal(self, target: Optional[Any]) -> str:
        pass


class TransformCapability(ABC):

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
