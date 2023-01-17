from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from src.core.constants import ABOUT_FED_TEXT, FED_ACTIVITIES_TEXT


def about_federation_keyboard():
    keyboard = [[InlineKeyboardButton('Ценности Федерации',
                                      callback_data='fed_values')],
                [InlineKeyboardButton('Направления деятельности',
                                      callback_data='fed_activities')],
                [InlineKeyboardButton('Меню', callback_data='main_menu')],
                [InlineKeyboardButton('На главную', callback_data='back')]]
    return InlineKeyboardMarkup(keyboard)


def go_back_keyboard():
    keyboard = [[InlineKeyboardButton('Меню', callback_data='main_menu')],
                [InlineKeyboardButton('На главную', callback_data='back')]]
    return InlineKeyboardMarkup(keyboard)


def about_fed_main_page(update: Update, context: CallbackContext):
    """Функция для первого сообщения о Федерации, с меню."""
    context.bot.send_message(update.effective_chat.id,
                             text=ABOUT_FED_TEXT,
                             reply_markup=about_federation_keyboard())


def fed_values_page(update: Update, context: CallbackContext):
    """Функция для отображения 'ценности Федерации'."""
    context.bot.send_photo(update.effective_chat.id,
                           open('src/static/images/ценности.png', 'rb'),
                           reply_markup=go_back_keyboard())


def fed_activities_page(update: Update, context: CallbackContext):
    """Функция для отображения 'Направления деятельности'."""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=FED_ACTIVITIES_TEXT,
                             reply_markup=go_back_keyboard())
