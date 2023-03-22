from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from src.core.constants import (ADAPTIVE_HOKKEY_PAGES_TEXT_URLS,
                                CHAMPION_WAY_URL)
from src.core.prometheus import counter_start_app
from src.core.prometheus_constants import OWNER
from src.features.all_for_hockey import start_all_for_hockey
from src.features.donations import page_donations
from src.features.federation_info import (about_fed_main_page,
                                          fed_activities_page, fed_values_page)
from src.features.hockey_types import (redirect_adaptive_hockey_types,
                                       start_hockey_types)
from src.features.question import question_menu_page
from src.features.send_stickers import sending_stickers
from src.features.who_is_fyrk import who_is_fyrk
from src.quiz.quiz import quiz, quiz_menu


def main_menu_keyboard():
    """Клавиатура для главного меню."""
    keyboard = [
        [InlineKeyboardButton('Задать вопрос', callback_data='ask_question'),
         InlineKeyboardButton('🏆 Путь чемпиона 🏅',
                              url=CHAMPION_WAY_URL)],
        [InlineKeyboardButton('ℹ Узнать о Федерации',
                              callback_data='about_federation')],
        [InlineKeyboardButton('Сделать пожертвования',
                              callback_data='make_donation')],
        [InlineKeyboardButton('Адаптивные виды хоккея',
                              callback_data='adaptive_hokkey_types')],
        [InlineKeyboardButton('🏒 Всё для хоккея',
                              callback_data='all_for_hockey'),
         InlineKeyboardButton('Получить стикерпаки',
                              callback_data='get_stickers')],
        [InlineKeyboardButton('🦝 Кто такой Фырк?',
                              callback_data='who_is_fyrk')],
        [InlineKeyboardButton('Квиз', callback_data='quiz')],
    ]
    return InlineKeyboardMarkup(keyboard)


def main_menu(update: Update, context: CallbackContext) -> None:
    """Функция для первого сообщения с меню."""
    chat = update.effective_chat
    context.bot.send_photo(
        chat_id=chat.id,
        photo=open('src/static/images/fyrk_smile.webp', 'rb'),
        caption='Выбери раздел меню.',
        reply_markup=main_menu_keyboard()
    )


def start_bot(update: Update, context: CallbackContext) -> None:
    """Функция первого сообщения и логирования нажатия команды '/start'."""
    counter_start_app.labels(group=OWNER).inc()
    main_menu(update, context)


MAIN_MENU_COMMANDS = {
    'make_donation': page_donations,
    'who_is_fyrk': who_is_fyrk,
    'main_menu': main_menu,
    'about_federation': about_fed_main_page,
    'fed_values': fed_values_page,
    'fed_activities': fed_activities_page,
    'ask_question': question_menu_page,
    'all_for_hockey': start_all_for_hockey,
    'get_stickers': sending_stickers,
    'adaptive_hokkey_types': start_hockey_types,
    'adaptive_types': start_hockey_types,
    'quiz': quiz_menu,
    'quiz_questions': quiz
}


def redirect_main_menu(update: Update,
                       context: CallbackContext) -> None:
    """Функция для обработки сигнала от кнопок главного меню раздела."""
    query = update.callback_query
    query.answer()
    if query.data in MAIN_MENU_COMMANDS:
        query.delete_message()
        MAIN_MENU_COMMANDS[query.data](update, context)
    elif query.data in ADAPTIVE_HOKKEY_PAGES_TEXT_URLS:
        query.delete_message()
        redirect_adaptive_hockey_types(update, context)
