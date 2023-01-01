import logging
import sys

from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (CallbackQueryHandler, CommandHandler, Filters,
						  MessageHandler, Updater)


from src.core.settings import settings
from src.features.champion_way import redirect_to_champion_way_button, redirect_to_champion_way_command
from src.features.donations import make_donations, page_donations
from src.features.hockey_types import (redirect_adaptive_hockey_types,
									   start_hockey_types)
from src.features.who_is_fyrk import who_is_fyrk
from src.features.big_menu_page import big_menu_command_command, big_menu_button
from src.features.question import question_menu_button, question_menu_command
from src.features.aboutus import aboutus_menu_button, aboutus_menu_command
from src.features.our_values import values_page_button, values_page_command
from src.features.activities import activities_page_button, activities_page_command
from src.features.answer_page import answer_page_comand, answer_page_button


logger = logging.getLogger('paraicehockey_bot')
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

def start_command(bot, update):
	bot.message.reply_photo(open('src/static/images/картинка №6.png', 'rb'), reply_markup=start_menu_keyboard())

def start_menu_button(bot, update):
	bot.callback_query.message.reply_photo(
		open('src/static/images/картинка №6.png', 'rb'),
							reply_markup=start_menu_keyboard())

def wake_up(update, context):
	"""Handler with button."""
	chat = update.effective_chat
	name = update.message.chat.first_name
	reply_markup = ReplyKeyboardMarkup([
		['Задать вопрос', 'Узнать о Федерации', 'Сделать пожертвования'],
		['/hockey_types', '/champion_way', 'Атрибутика Федерации'],
		['Хоккейный инвентарь и экипировка', 'Кто такой Фырк?', 'Квиз']
	], resize_keyboard=True)
	context.bot.send_message(chat_id=chat.id,
							 text=f'Спасибо, {name}, что включил меня',
							 reply_markup=reply_markup)


def say_hi(update, context):
	"""Handler that intercept all messages."""
	chat = update.effective_chat
	name = update.message.chat.first_name
	context.bot.send_message(chat_id=chat.id,
							 text=f'Эй, {name}! Давай играть в хоккей!')

def start_menu_keyboard():
	keyboard = [[InlineKeyboardButton('Задать вопрос', callback_data='question')],
				[InlineKeyboardButton('Меню', callback_data='menu')]]
	return InlineKeyboardMarkup(keyboard)


def remove_keyboard_markup(update, context):
	update.message.reply_text('Окей',
							 reply_markup=ReplyKeyboardRemove())



def show_main_menu():
	updater = Updater(token=settings.bot_token)
	###########  COMMANDS / MENU ##############
	updater.dispatcher.add_handler(CommandHandler('start', start_command))
	updater.dispatcher.add_handler(CommandHandler('champion_way',
												  redirect_to_champion_way_command))
	# updater.dispatcher.add_handler(CommandHandler('hockey_types',
												#   start_hockey_types))
	updater.dispatcher.add_handler(CommandHandler('menu', big_menu_command_command))
	updater.dispatcher.add_handler(CommandHandler('question', question_menu_command))
	updater.dispatcher.add_handler(CommandHandler('answer', answer_page_comand))
	updater.dispatcher.add_handler(CommandHandler('aboutus', aboutus_menu_command))
	updater.dispatcher.add_handler(CommandHandler('values', values_page_command))
	updater.dispatcher.add_handler(CommandHandler('activities', activities_page_command))
	updater.dispatcher.add_handler(CommandHandler('champion_way', redirect_to_champion_way_command))


	############ BUTTONS #################
	# updater.dispatcher.add_handler(CallbackQueryHandler(
	# redirect_adaptive_hockey_types))

	updater.dispatcher.add_handler(CallbackQueryHandler(start_menu_button, pattern='home'))
	updater.dispatcher.add_handler(CallbackQueryHandler(big_menu_button, pattern='menu'))
	updater.dispatcher.add_handler(CallbackQueryHandler(question_menu_button, pattern='question'))
	updater.dispatcher.add_handler(CallbackQueryHandler(answer_page_button, pattern='answer'))
	updater.dispatcher.add_handler(CallbackQueryHandler(aboutus_menu_button, pattern='aboutus'))
	updater.dispatcher.add_handler(CallbackQueryHandler(values_page_button, pattern='values'))
	updater.dispatcher.add_handler(CallbackQueryHandler(activities_page_button, pattern='activities'))
	updater.dispatcher.add_handler(CallbackQueryHandler(redirect_to_champion_way_button, pattern='champion_way'))
	# updater.dispatcher.add_handler(CallbackQueryHandler(page_donations))
	updater.dispatcher.add_handler(CallbackQueryHandler(page_donations, pattern='donations'))
	updater.dispatcher.add_handler(CallbackQueryHandler(who_is_fyrk, pattern='who_is_fyrk'))
	updater.dispatcher.add_handler(CallbackQueryHandler(redirect_adaptive_hockey_types))
	
	############ MESSAGES   #################
	updater.dispatcher.add_handler(
		MessageHandler(Filters.text('На главную'), start_command))
	updater.dispatcher.add_handler(
		MessageHandler(Filters.text('Меню'), big_menu_command_command))
	updater.dispatcher.add_handler(
		MessageHandler(Filters.text('Кто такой Фырк?'), who_is_fyrk))
	updater.dispatcher.add_handler(
		MessageHandler(Filters.text('Сделать пожертвования'), page_donations))
	updater.dispatcher.add_handler(
		MessageHandler(Filters.text('Поддержать'), make_donations))
	updater.dispatcher.add_handler(
		MessageHandler(Filters.text('Убрать кнопки'), remove_keyboard_markup))
	updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
	updater.start_polling()
	updater.idle()
