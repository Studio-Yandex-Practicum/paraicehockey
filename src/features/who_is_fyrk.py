from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from src.core.prometheus import counter_viewed_who_is_fyrk
from src.core.prometheus_constants import WHO_IS_FYRK
from src.core.save_metrics import (create_table, get_metric_value,
                                   update_metric_value)

create_table()

who_is_fyrk_total = get_metric_value('user_viewed_who_is_fyrk_total')
if who_is_fyrk_total is not None:
    counter_viewed_who_is_fyrk.labels(group=WHO_IS_FYRK).inc(who_is_fyrk_total)


def who_is_fyrk(update, context):
    """Функция для рассказа о Фырке и его семьи."""
    counter_viewed_who_is_fyrk.labels(group=WHO_IS_FYRK).inc()
    update_metric_value(
        'user_viewed_who_is_fyrk_total',
        int(counter_viewed_who_is_fyrk.labels(group=WHO_IS_FYRK)._value.get())
    )
    chat = update.effective_chat
    keyboard = [
        [InlineKeyboardButton('Меню', callback_data='main_menu')]
    ]
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет! Давай знакомиться. Это я и моя семья.')
    context.bot.send_photo(
        chat.id,
        open('src/static/images/picture_6.png', 'rb')
    )
    context.bot.send_photo(
        chat.id,
        open('src/static/images/picture_7.png', 'rb')
    )
    context.bot.send_photo(
        chat.id,
        open('src/static/images/picture_8.png', 'rb'),
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
