from typing import List

from case.core.case import Case
from case.implementations.example_case import ExampleCase
from tenet.core.tenet import Tenet

example_case = ExampleCase()


# Example Tenet, entity that collects cases on similar topics
#
# To create a tenet, you need to extend the abstract class "Tenet" and override all abstract methods
# and add to the tenet factory
#

class ExampleTenet(Tenet):
  def cases(self) -> List[Case]:
    return [example_case,
            # example_case2,
            # example_case3
            ]

  def description(self) -> str:
    return 'tenet containing example cases'
