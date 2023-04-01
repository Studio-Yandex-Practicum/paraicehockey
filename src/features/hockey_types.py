from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from src.core.constants import (ADAPTIVE_HOKKEY_MAIN_TEXT,
                                ADAPTIVE_HOKKEY_PAGES_TEXT_URLS)
from src.core.prometheus import (ADAPTIVE_HOKKEY_PROMETHEUS,
                                 counter_viewed_adaptive_hockey,
                                 counter_viewed_hockey_for_blind,
                                 counter_viewed_sledzh_hockey,
                                 counter_viewed_special_hockey)
from src.core.prometheus_constants import ADAPTIVE_HOKKEY
from src.core.save_metrics import (create_table, get_metric_value,
                                   update_metric_query_value,
                                   update_metric_value)

create_table()

adaptive_hockey_total = get_metric_value('user_viewed_adaptive_hockey_total')
if adaptive_hockey_total is not None:
    counter_viewed_adaptive_hockey.labels(
        group=ADAPTIVE_HOKKEY).inc(adaptive_hockey_total)

sledzh_hockey_total = get_metric_value('user_viewed_sledzh_hockey_total')
if sledzh_hockey_total is not None:
    counter_viewed_sledzh_hockey.labels(
        group=ADAPTIVE_HOKKEY).inc(sledzh_hockey_total)

special_hockey_total = get_metric_value('user_viewed_special_hockey_total')
if special_hockey_total is not None:
    counter_viewed_special_hockey.labels(
        group=ADAPTIVE_HOKKEY).inc(special_hockey_total)

hockey_for_blind_total = get_metric_value('user_viewed_hockey_for_blind_total')
if hockey_for_blind_total is not None:
    counter_viewed_hockey_for_blind.labels(
        group=ADAPTIVE_HOKKEY).inc(hockey_for_blind_total)


def adaptive_hockey_keyboard():
    """Клавиатура для главного меню Адаптивные виды хоккея."""
    keyboard = [
        [InlineKeyboardButton('Следж-хоккей', callback_data='sledzh_hockey')],
        [InlineKeyboardButton('Специальный хоккей',
                              callback_data='special_hockey')],
        [InlineKeyboardButton('Хоккей для незрячих',
                              callback_data='hockey_for_blind')],
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
    ]
    return InlineKeyboardMarkup(keyboard)


def start_hockey_types(update: Update, context: CallbackContext) -> None:
    """Функция для первого сообщения с меню 'Адаптивные виды хоккея'."""
    counter_viewed_adaptive_hockey.labels(group=ADAPTIVE_HOKKEY).inc()
    update_metric_value(
        'user_viewed_adaptive_hockey_total',
        int(counter_viewed_adaptive_hockey.labels(
            group=ADAPTIVE_HOKKEY
        )._value.get())
    )
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=ADAPTIVE_HOKKEY_MAIN_TEXT,
                             parse_mode='HTML',
                             reply_markup=adaptive_hockey_keyboard())


def redirect_adaptive_hockey_types(update: Update,
                                   context: CallbackContext) -> None:
    """Функция для обработки сигнала от кнопок главного меню раздела.
    Изменяет текстовое сообщение и кнопки к нему или направляет на
    страницы сайта с командами.
    """
    query = update.callback_query
    chat_id = update.effective_chat.id
    if query.data in ADAPTIVE_HOKKEY_PAGES_TEXT_URLS:
        ADAPTIVE_HOKKEY_PROMETHEUS[query.data].labels(
            group=ADAPTIVE_HOKKEY).inc()
        names = [
            'user_viewed_sledzh_hockey_total',
            'user_viewed_special_hockey_total',
            'user_viewed_hockey_for_blind_total'
        ]
        values = []
        for metric_name in ADAPTIVE_HOKKEY_PROMETHEUS:
            values.append(ADAPTIVE_HOKKEY_PROMETHEUS[metric_name].labels(
                group=ADAPTIVE_HOKKEY
            )._value.get()
            )
        update_metric_query_value(names, values)
        keyboard = [
            [InlineKeyboardButton('Адаптивные виды хоккея',
                                  callback_data='adaptive_types')],
            [InlineKeyboardButton('Команды',
                                  url=ADAPTIVE_HOKKEY_PAGES_TEXT_URLS[
                                      query.data][0])],
            [InlineKeyboardButton('Меню', callback_data='main_menu')]
        ]
        keybord = InlineKeyboardMarkup(keyboard)
        context.bot.send_photo(
            chat_id,
            open(ADAPTIVE_HOKKEY_PAGES_TEXT_URLS[query.data][1], 'rb'))
        context.bot.send_photo(
            chat_id,
            open(ADAPTIVE_HOKKEY_PAGES_TEXT_URLS[query.data][2], 'rb'),
            reply_markup=keybord)
