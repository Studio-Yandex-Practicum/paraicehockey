from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from src.core.constants import QUESTION_TEXT
from src.core.prometheus import counter_viewed_question


# TODO: Логирование нажатия кнопки-ссылки 'Получить ответ'
#  (кол-во пользователей которые нажимаю кнопку, задают вопрос)


def question_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Получить ответ',
                                      url='https://t.me/Parahockey')],
                [InlineKeyboardButton('Меню', callback_data='main_menu')]]
    return InlineKeyboardMarkup(keyboard)


def question_menu_page(update: Update, context: CallbackContext):
    counter_viewed_question.inc()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=QUESTION_TEXT,
                             reply_markup=question_menu_keyboard())
