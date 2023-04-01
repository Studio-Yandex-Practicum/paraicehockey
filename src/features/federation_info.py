from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from src.core.prometheus import (counter_viewed_federation,
                                 counter_viewed_federation_activities,
                                 counter_viewed_federation_values)
from src.core.prometheus_constants import FEDERATION
from src.core.save_metrics import (create_table, get_metric_value,
                                   update_metric_value)

create_table()

federation_total = get_metric_value('user_viewed_federation_total')
if federation_total is not None:
    counter_viewed_federation.labels(group=FEDERATION).inc(federation_total)

federation_activities = get_metric_value(
    'user_viewed_federation_activities_total'
)
if federation_activities is not None:
    counter_viewed_federation_activities.labels(
        group=FEDERATION
    ).inc(federation_activities)

federation_values = get_metric_value('user_viewed_federation_values_total')
if federation_values is not None:
    counter_viewed_federation_values.labels(
        group=FEDERATION
    ).inc(federation_values)


def about_federation_keyboard():
    keyboard = [
        [InlineKeyboardButton('Ценности Федерации',
                              callback_data='fed_values')],
        [InlineKeyboardButton('Направления деятельности',
                              callback_data='fed_activities')],
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
    ]
    return InlineKeyboardMarkup(keyboard)


def go_back_keyboard_for_values():
    keyboard = [
        [InlineKeyboardButton('Направления деятельности',
                              callback_data='fed_activities')],
        [InlineKeyboardButton('Меню', callback_data='main_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)


def go_back_keyboard_for_activities():
    keyboard = [
        [InlineKeyboardButton('Ценности Федерации',
                              callback_data='fed_values')],
        [InlineKeyboardButton('Меню', callback_data='main_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)


def about_fed_main_page(update: Update, context: CallbackContext):
    """Функция для первого сообщения о Федерации, с меню."""
    counter_viewed_federation.labels(group=FEDERATION).inc()
    update_metric_value(
        'user_viewed_federation_total',
        int(counter_viewed_federation.labels(group=FEDERATION)._value.get()))
    context.bot.send_photo(update.effective_chat.id,
                           open('src/static/images/about_fed_1.png', 'rb'))
    context.bot.send_photo(update.effective_chat.id,
                           open('src/static/images/about_fed_2.png', 'rb'),
                           reply_markup=about_federation_keyboard())


def fed_values_page(update: Update, context: CallbackContext):
    """Функция для отображения 'ценности Федерации'."""
    counter_viewed_federation_values.labels(group=FEDERATION).inc()
    update_metric_value(
        'user_viewed_federation_values_total',
        int(counter_viewed_federation_values.labels(
            group=FEDERATION
        )._value.get())
    )
    context.bot.send_photo(update.effective_chat.id,
                           open('src/static/images/values.png', 'rb'),
                           reply_markup=go_back_keyboard_for_values())


def fed_activities_page(update: Update, context: CallbackContext):
    """Функция для отображения 'Направления деятельности'."""
    counter_viewed_federation_activities.labels(group=FEDERATION).inc()
    update_metric_value(
        'user_viewed_federation_activities_total',
        int(counter_viewed_federation_activities.labels(
            group=FEDERATION
        )._value.get())
    )
    context.bot.send_photo(update.effective_chat.id,
                           open('src/static/images/fed_activities.png', 'rb'),
                           reply_markup=go_back_keyboard_for_activities())
