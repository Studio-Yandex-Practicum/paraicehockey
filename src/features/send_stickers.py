from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from src.core.constants import STICKERS_URL
from src.core.prometheus import counter_viewed_sticker
from src.core.prometheus_constants import STICKER
from src.core.save_metrics import (create_table, get_metric_value,
                                   update_metric_value)

create_table()

sticker_total = get_metric_value('user_viewed_sticker_total')
if sticker_total is not None:
    counter_viewed_sticker.labels(group=STICKER).inc(sticker_total)


def sending_stickers(update: Update, context: CallbackContext) -> None:
    """Функция для отправки пользователю стикера."""
    counter_viewed_sticker.labels(group=STICKER).inc()
    update_metric_value(
        'user_viewed_sticker_total',
        int(counter_viewed_sticker.labels(group=STICKER)._value.get())
    )
    keyboard = [
        [InlineKeyboardButton('Получить стикерпак', url=STICKERS_URL)],
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_sticker(chat_id=update.effective_chat.id,
                             sticker=open('src/static/images/picture_1.webp',
                                          'rb'),
                             reply_markup=reply_markup)
