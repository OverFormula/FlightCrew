import asyncio

import telegram
from telegram import Bot
from telegram.request import HTTPXRequest

from config.crew_config import CrewConfig

config = CrewConfig()


class Postman:
  bot: Bot

  def __init__(self):
    request = HTTPXRequest(connection_pool_size=config.get_connection_pool_size())
    self.bot = telegram.Bot(token=config.get_token(), request=request)

  def send_message(self, message: str):
    asyncio.run(self.bot.send_message(chat_id=config.get_chat_id(), text=message))
