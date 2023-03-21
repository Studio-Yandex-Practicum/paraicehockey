from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from src.core.constants import QUESTION_TEXT
from src.core.prometheus import counter_viewed_question
from src.core.prometheus_constants import QUESTION


def question_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Получить ответ',
                                      url='https://t.me/Parahockey')],
                [InlineKeyboardButton('Меню', callback_data='main_menu')]]
    return InlineKeyboardMarkup(keyboard)


def question_menu_page(update: Update, context: CallbackContext):
    counter_viewed_question.labels(group=QUESTION).inc()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=QUESTION_TEXT,
                             reply_markup=question_menu_keyboard())
