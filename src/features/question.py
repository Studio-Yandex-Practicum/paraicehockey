from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from src.core.constants import QUESTION_TEXT
from src.core.prometheus import counter_viewed_question
from src.core.prometheus_constants import QUESTION
from src.core.save_metrics import (create_table, get_metric_value,
                                   update_metric_value)

create_table()

question_total = get_metric_value('user_viewed_question_total')
if question_total is not None:
    counter_viewed_question.labels(group=QUESTION).inc(question_total)


def question_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Получить ответ',
                                      url='https://t.me/Parahockey')],
                [InlineKeyboardButton('Меню', callback_data='main_menu')]]
    return InlineKeyboardMarkup(keyboard)


def question_menu_page(update: Update, context: CallbackContext):
    counter_viewed_question.labels(group=QUESTION).inc()
    update_metric_value(
        'user_viewed_question_total',
        int(counter_viewed_question.labels(group=QUESTION)._value.get()))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=QUESTION_TEXT,
                             reply_markup=question_menu_keyboard())
