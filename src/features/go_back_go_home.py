from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def go_back_keyboard():
	keyboard = [
		[InlineKeyboardButton('Меню', callback_data='menu')],
		[InlineKeyboardButton('На главную', callback_data='home')]
	]
	return InlineKeyboardMarkup(keyboard)