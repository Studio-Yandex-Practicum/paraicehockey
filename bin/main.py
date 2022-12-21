import logging
import os
import sys

from dotenv import load_dotenv
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (CallbackQueryHandler, CommandHandler, Filters,
                          MessageHandler, Updater)

from champion_way import redirect_to_champion_way
from hokkey_types.hokkey_types import (redirect_adaptive_hokkey_types,
                                       start_hokkey_types)

load_dotenv()

token = os.getenv('BOT_TOKEN')

logger = logging.getLogger('paraicehokkey_bot')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)
formatter = logging.Formatter(
    '%(asctime)s [%(levelname)s] %(message)s'
)
handler.setFormatter(formatter)


def wake_up(update, context):
    """Handler with button."""
    chat = update.effective_chat
    name = update.message.chat.first_name
    keyboard = [[KeyboardButton('/hokkey_types')],
                [KeyboardButton('/champion_way')]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    context.bot.send_message(chat_id=chat.id,
                             text=f'Спасибо, {name}, что включил меня',
                             reply_markup=reply_markup)


def say_hi(update, context):
    """Handler that intercept all messages."""
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(chat_id=chat.id,
                             text=f'Эй, {name}! Давай играть в хоккей!')


def main():
    updater = Updater(token=token)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('champion_way',
                                                  redirect_to_champion_way))
    updater.dispatcher.add_handler(CommandHandler('hokkey_types',
                                                  start_hokkey_types))
    updater.dispatcher.add_handler(CallbackQueryHandler(
                                   redirect_adaptive_hokkey_types))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
