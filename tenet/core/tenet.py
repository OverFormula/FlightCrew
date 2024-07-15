from abc import ABC, abstractmethod
from typing import List

from case.core.case import Case


class Tenet(ABC):

    @abstractmethod
    def cases(self) -> List[Case]:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


