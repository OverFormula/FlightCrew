from telegram.ext import Application, ContextTypes, CommandHandler
from telegram import Update


class CrewCommandHandler:
  field: str

  def __init__(self):
    self.field = 'command'

  def add_command_handlers(self, app: Application):
    app.add_handler(CommandHandler('start', self.start_command))
    app.add_handler(CommandHandler('help', self.help_command))

  async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!")

  async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Help!")
