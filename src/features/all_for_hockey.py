from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from src.core.constants import ALL_FOR_HOKKEY_MAIN_TEXT, HOCKEY_EQUIPMENT_URL
from src.core.prometheus import counter_viewed_all_for_hockey
from src.core.prometheus_constants import ALL_FOR_HOCKEY
from src.core.save_metrics import (create_table, get_metric_value,
                                   update_metric_value)

create_table()

all_for_hockey_total = get_metric_value('user_viewed_all_for_hockey_total')
if all_for_hockey_total is not None:
    counter_viewed_all_for_hockey.labels(
        group=ALL_FOR_HOCKEY
    ).inc(all_for_hockey_total)


def all_for_hockey_keyboard():
    """Клавиатура для главного меню раздела 'Всё для хоккея'."""
    keyboard = [
        [InlineKeyboardButton('Хоккейный инвентарь и экипировка',
                              url=HOCKEY_EQUIPMENT_URL)],
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
    ]
    return InlineKeyboardMarkup(keyboard)


def start_all_for_hockey(update: Update, context: CallbackContext) -> None:
    """Функция для первого сообщения с меню раздела 'Всё для хоккея'."""
    counter_viewed_all_for_hockey.labels(group=ALL_FOR_HOCKEY).inc()
    update_metric_value(
        'user_viewed_all_for_hockey_total',
        int(counter_viewed_all_for_hockey.labels(
            group=ALL_FOR_HOCKEY
        )._value.get())
    )
    context.bot.send_message(text=ALL_FOR_HOKKEY_MAIN_TEXT,
                             chat_id=update.effective_chat.id,
                             reply_markup=all_for_hockey_keyboard())
