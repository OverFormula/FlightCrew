import threading
import time

import schedule

from config.crew_config import CrewConfig
from postman.postman import Postman
from tenet.core.tenet_registry import TenetRegistry

config = CrewConfig()
tenets = TenetRegistry.get_tenets()
postman = Postman()


def start():
  while True:
    try:
      schedule.run_pending()
      time.sleep(1)
    except Exception as e:
      print(f"Scheduler failed, {e}")


def send(message: str):
  postman.send_message(message)


daemon = threading.Thread(target=start)
for tenet in tenets:
  for case in tenet.cases():
    case.cron(schedule, send)

daemon.start()
