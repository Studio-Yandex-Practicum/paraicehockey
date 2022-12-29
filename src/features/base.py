import logging
import sys

from telegram import ReplyKeyboardMarkup
from telegram.ext import (CallbackQueryHandler, CommandHandler, Filters,
                          MessageHandler, Updater)

from src.core.settings import settings
from src.features.all_for_hockey import show_product
from src.features.champion_way import redirect_to_champion_way
from src.features.donations import make_donations, page_donations
from src.features.hockey_types import (redirect_adaptive_hockey_types,
                                       start_hockey_types)
from src.features.who_is_fyrk import who_is_fyrk

logger = logging.getLogger('paraicehockey_bot')
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)


def wake_up(update, context):
    """Handler with button."""
    chat = update.effective_chat
    name = update.message.chat.first_name
    reply_markup = ReplyKeyboardMarkup([
        ['Задать вопрос', 'Узнать о Федерации', 'Сделать пожертвования'],
        ['/hockey_types', '/champion_way', 'Атрибутика Федерации'],
        ['Хоккейный инвентарь и экипировка', 'Кто такой Фырк?', 'Квиз']
    ], resize_keyboard=True)
    context.bot.send_message(chat_id=chat.id,
                             text=f'Спасибо, {name}, что включил меня',
                             reply_markup=reply_markup)


def say_hi(update, context):
    """Handler that intercept all messages."""
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(chat_id=chat.id,
                             text=f'Эй, {name}! Давай играть в хоккей!')


def show_main_menu():
    updater = Updater(token=settings.bot_token)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('champion_way',
                                                  redirect_to_champion_way))
    updater.dispatcher.add_handler(CommandHandler('hockey_types',
                                                  start_hockey_types))
    updater.dispatcher.add_handler(CallbackQueryHandler(
                                   redirect_adaptive_hockey_types))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.text('Кто такой Фырк?'), who_is_fyrk))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.text('Сделать пожертвования'), page_donations))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.text('Поддержать'), make_donations))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
    updater.dispatcher.add_handler(CommandHandler('all_for_hockey',
                                                  show_product))
    updater.start_polling()
    updater.idle()
