from src.core.constants import VALUES_TEXT
from src.features.go_back_go_home import go_back_keyboard


def values_page_command(bot, update):
	bot.message.reply_text(
		VALUES_TEXT,
		reply_markup=go_back_keyboard()
	)

def values_page_button(bot, update):
	bot.callback_query.message.edit_text(
		VALUES_TEXT,
		reply_markup=go_back_keyboard()
	)