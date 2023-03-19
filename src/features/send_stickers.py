from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from src.core.constants import STICKERS_URL
from src.core.prometheus import counter_viewed_sticker
from src.core.prometheus_constants import STICKER


def sending_stickers(update: Update, context: CallbackContext) -> None:
    """Функция для отправки пользователю стикера."""
    counter_viewed_sticker.labels(group=STICKER).inc()
    keyboard = [
        [InlineKeyboardButton('Получить стикерпак', url=STICKERS_URL)],
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_sticker(chat_id=update.effective_chat.id,
                             sticker=open('src/static/images/picture_1.webp',
                                          'rb'),
                             reply_markup=reply_markup)
