from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from src.core.constants import QUESTION_TEXT


def question_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Назад', callback_data='back')],
                [InlineKeyboardButton('Получить ответ',
                                      url='https://t.me/@Kot_in')]]
    return InlineKeyboardMarkup(keyboard)


def question_menu_page(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=QUESTION_TEXT,
                             reply_markup=question_menu_keyboard())
