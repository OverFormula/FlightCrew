from telegram.ext import Application

from handlers.crew_command_handler import CrewCommandHandler
from config.crew_config import CrewConfig
from handlers.crew_query_handler import CrewQueryHandler
from tenet.implementations import tenet_factory
from cron import scheduler

crew_query_handler = CrewQueryHandler()
crew_command_handler = CrewCommandHandler()
crew_config = CrewConfig()


def build_app() -> Application:
  token = crew_config.get_token()
  return Application.builder().token(token).build()


def add_handlers(app: Application):
  crew_command_handler.add_command_handlers(app)
  crew_query_handler.add_query_handlers(app)
  app.run_polling(poll_interval=crew_config.get_poll_interval())


def main():
  print('Starting bot...\n\n')
  app = build_app()
  add_handlers(app)


if __name__ == '__main__':
  main()
