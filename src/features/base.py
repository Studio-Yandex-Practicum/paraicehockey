import logging
import sys

from telegram.ext import (CallbackQueryHandler, CommandHandler, PollHandler,
                          Updater)

from src.core.prometheus import OWNER, counter_start_app
from src.core.settings import settings
from src.features.main_menu import main_menu, redirect_main_menu
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
    updater.dispatcher.add_handler(CommandHandler('start', main_menu))
    updater.dispatcher.add_handler(
        CommandHandler('start', counter_start_app.labels(group=OWNER).inc()))
    updater.dispatcher.add_handler(CallbackQueryHandler(
        redirect_main_menu))
    updater.start_polling()
    updater.idle()
