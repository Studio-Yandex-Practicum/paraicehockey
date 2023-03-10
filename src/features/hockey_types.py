from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from src.core.constants import (ADAPTIVE_HOKKEY_MAIN_TEXT,
                                ADAPTIVE_HOKKEY_PAGES_TEXT_URLS)
from src.core.prometheus import (ADAPTIVE_HOKKEY_PROMETHEUS,
                                 counter_viewed_adaptive_hockey)


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
    counter_viewed_adaptive_hockey.labels(group='AdaptiveHockey').inc()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=ADAPTIVE_HOKKEY_MAIN_TEXT,
                             parse_mode='HTML',
                             reply_markup=adaptive_hockey_keyboard())


# TODO: Логирование нажатия кнопки-ссылки 'Команды'
#  (кол-во пользователей переходящих на сайт через кнопку, во всех 3
#  подразделах)

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
            group='AdaptiveHockey').inc()
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
