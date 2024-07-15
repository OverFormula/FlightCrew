from abc import ABC, abstractmethod
from typing import List


class Case(ABC):

  @abstractmethod
  def tags(self) -> List[str]:
    pass

  @abstractmethod
  def description(self) -> str:
    pass

  @abstractmethod
  def process(self, query="") -> str:
    pass

  @abstractmethod
  def cron(self, schedule, callback):
    pass

