from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from src.core.constants import ABOUT_US_TEXT



def aboutus_menu_command(bot, update):
	bot.message.reply_text(ABOUT_US_TEXT,
							reply_markup=aboutus_keyboard())

def aboutus_menu_button(bot, update):
	bot.callback_query.message.edit_text(ABOUT_US_TEXT,
							reply_markup=aboutus_keyboard())


def aboutus_keyboard():
	keyboard = [[InlineKeyboardButton('Ценности Федерации', callback_data='values')],
				[InlineKeyboardButton('Направления деятельности', callback_data='activities')],
				[InlineKeyboardButton('Меню', callback_data='menu')],
				[InlineKeyboardButton('На главную', callback_data='home')]]
	return InlineKeyboardMarkup(keyboard)
