from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from src.core.constants import (ADAPTIVE_HOKKEY_MAIN_TEXT,
                                ADAPTIVE_HOKKEY_PAGES_TEXT_URLS)


def adaptive_hockey_keyboard():
    """Клавиатура для главного меню Адаптивные виды хоккея."""
    keyboard = [
        [InlineKeyboardButton('Следж-хоккей', callback_data='sledzh_hockey')],
        [InlineKeyboardButton('Специальный хоккей',
                              callback_data='special_hockey')],
        [InlineKeyboardButton('Хоккей для незрячих',
                              callback_data='hockey_for_blind')],
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
        [InlineKeyboardButton('На главную', callback_data='start_page')],
    ]
    return InlineKeyboardMarkup(keyboard)


def start_hockey_types(update: Update, context: CallbackContext) -> None:
    """Функция для первого сообщения с меню 'Адаптивные виды хоккея'."""
    update.message.reply_text(ADAPTIVE_HOKKEY_MAIN_TEXT,
                              parse_mode='HTML',
                              reply_markup=adaptive_hockey_keyboard())


def redirect_adaptive_hockey_types(update: Update,
                                   context: CallbackContext) -> None:
    """Функция для обработки сигнала от кнопок главного меню раздела.
    Изменяет текстовое сообщение и кнопки к нему или направляет на
    страницы сайта с командами.
    """
    query = update.callback_query
    query.answer()
    if query.data in ADAPTIVE_HOKKEY_PAGES_TEXT_URLS:
        keyboard = [
            [InlineKeyboardButton('Адаптивные виды хоккея',
                                  callback_data='adaptive_hockey_types')],
            [InlineKeyboardButton('Команды',
                                  url=ADAPTIVE_HOKKEY_PAGES_TEXT_URLS[
                                      query.data][0])],
        ]
        keybord = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text=ADAPTIVE_HOKKEY_PAGES_TEXT_URLS[
                                query.data][1],
                                parse_mode='HTML')
        query.edit_message_reply_markup(reply_markup=keybord)
    elif query.data == 'adaptive_hockey_types':
        query.edit_message_text(text=ADAPTIVE_HOKKEY_MAIN_TEXT,
                                parse_mode='HTML')
        query.edit_message_reply_markup(
            reply_markup=adaptive_hockey_keyboard())
    elif ((query.data == 'start_page') or (query.data == 'main_menu')):
        query.delete_message()
        # TODO: Сделать переход на стартовую страницу
        # TODO: Сделать переход на главное меню
    # else:
    #     query.edit_message_text(text=f'Selected option: {query.data}')
