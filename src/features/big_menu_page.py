
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from src.core.constants import BIG_MENU_PAGE_TEXT


def big_menu_command_command(bot, update):
	bot.message.reply_text(BIG_MENU_PAGE_TEXT,
							reply_markup=menu_page_keyboard())

def big_menu_button(bot, update):
	bot.callback_query.message.reply_text(BIG_MENU_PAGE_TEXT,
							reply_markup=menu_page_keyboard())


def menu_page_keyboard():
	keyboard = [[InlineKeyboardButton('Узнать о Федерации', callback_data='aboutus')],
				[InlineKeyboardButton('Адаптивные виды хоккея', callback_data='hockey_types')],
				[InlineKeyboardButton('Путь чемпиона', callback_data='champion_way')],
				[InlineKeyboardButton('Всё для хоккея', callback_data='menu_3')],
				[InlineKeyboardButton('Сделать пожертвования', callback_data='donations')],
				[InlineKeyboardButton('Кто такой Фырк', callback_data='who_is_fyrk')],
				[InlineKeyboardButton('Квиз', callback_data='menu_6')],
				[InlineKeyboardButton('Получить стикерпак', callback_data='menu_7')],
				[InlineKeyboardButton('Назад', callback_data='home')]]
	return InlineKeyboardMarkup(keyboard)