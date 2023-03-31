import logging
import sys

from telegram.ext import (CallbackQueryHandler, CommandHandler, PollHandler,
                          Updater)

from src.core.settings import settings
from src.features.export_to_excel import (export_for_all, export_for_day,
                                          export_for_week)
from src.features.main_menu import redirect_main_menu, start_bot
from src.quiz.quiz import poll_handler

logger = logging.getLogger('paraicehockey_bot')
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)


def show_main_menu():
    updater = Updater(token=settings.bot_token)
    updater.dispatcher.add_handler(
        PollHandler(
            poll_handler,
            pass_chat_data=True,
            pass_user_data=True
        ))
    updater.dispatcher.add_handler(CommandHandler('start', start_bot))
    updater.dispatcher.add_handler(
        CommandHandler('export_for_day', export_for_day))
    updater.dispatcher.add_handler(
        CommandHandler('export_for_week', export_for_week))
    updater.dispatcher.add_handler(
        CommandHandler('export_for_all', export_for_all))
    updater.dispatcher.add_handler(CallbackQueryHandler(
        redirect_main_menu))
    updater.start_polling()
    updater.idle()
