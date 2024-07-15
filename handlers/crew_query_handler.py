from telegram import Update, Message
from telegram.ext import Application, ContextTypes, MessageHandler, filters

from config.crew_config import CrewConfig
from processor.query_processor import QueryProcessor

crew_config = CrewConfig()
query_processor = QueryProcessor()


class CrewQueryHandler:

  def __init__(self):
    self.something = self

  def add_query_handlers(self, app: Application):
    app.add_handler(MessageHandler(filters.TEXT, self.handle_message))

  async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    self.extract_user_info(message)
    response = query_processor.process_query(message.text)
    self.log_crew_response(response)

    await update.message.reply_text(response)

  def extract_user_info(self, message: Message):
    user = message.from_user

    first_name: str = user.first_name
    last_name: str = user.last_name
    username: str = user.username

    print('chat_id: ' + str(message.chat_id))

    message_text = message.text
    self.log_message(first_name, last_name, username, message_text)

  def log_message(self, first_name: str, last_name: str, username: str, message_text: str):
    print(f'{first_name} {last_name} (@{username}): {message_text}')

  def log_crew_response(self, response: str):
    print('Flight Crew: ', response)
