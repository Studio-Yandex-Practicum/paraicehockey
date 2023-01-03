import logging
import sys

from telegram.ext import CallbackQueryHandler, CommandHandler, Updater

from src.core.settings import settings
from src.features.donations import page_donations
from src.features.main_menu import redirect_main_menu
from src.features.start import wake_up

logger = logging.getLogger('paraicehockey_bot')
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)


def show_main_menu():
    updater = Updater(token=settings.bot_token)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('donate',
                                                  page_donations))
    updater.dispatcher.add_handler(CallbackQueryHandler(
                                   redirect_main_menu))
    updater.start_polling()
    updater.idle()
