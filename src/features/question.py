from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from src.core.constants import QUESTION_TEXT


def question_menu_command(bot, update):
	bot.message.reply_text(QUESTION_TEXT,
							reply_markup=question_menu_keyboard())


def question_menu_button(bot, update):
	bot.callback_query.message.edit_text(QUESTION_TEXT,
							reply_markup=question_menu_keyboard())

def question_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Назад', callback_data='home')],
				[InlineKeyboardButton('Получить ответ', callback_data='answer')]]
	return InlineKeyboardMarkup(keyboard)
