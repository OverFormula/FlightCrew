from typing import List

from case.core.case import Case


# An example of creating a case - a small rule
# that can be used both as an answer to a question and executed according to a schedule (cron).
#
# To create a case, you need to extend the abstract class "Case" and override all abstract methods


class ExampleCase(Case):
  def tags(self) -> List[str]:
    return ['example', 'search phrase', 'case number one']

  def description(self) -> str:
    return 'example to show how to create a case'

  def process(self, query="") -> str:
    return ('here you need to return the response. \n'

            'If necessary, you can add additional logic depending on the request, time or some other parameters\n\n')

  def cron(self, schedule, callback):
    schedule.every().sunday.at("23:00").do(callback, self.process())
    schedule.every().tuesday.at("11:00").do(callback, self.process())

#     other possible options:
#         schedule.every().day.at("05:35").do(callback, self.process())
#         schedule.every(5).minutes.do(callback, self.process())
#         schedule.every(3).days.do(callback, self.process())
#         schedule.every().hour.at(":23").do(callback, self.process())
