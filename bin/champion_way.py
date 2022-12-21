from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

URL = 'https://paraicehockey.ru/mobilnoe-prilozhenie/'


def redirect_to_champion_way(update: Update, context: CallbackContext) -> None:
    """Кнопка для перехода на страницу сайта с приложением 'Путь чемпиона'."""
    keyboard = [[InlineKeyboardButton('Путь чемпиона', url=URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Переход на страницу сайта с приложением',
                              reply_markup=reply_markup)
