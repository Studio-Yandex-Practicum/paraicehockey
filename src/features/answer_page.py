
def answer_page_comand(bot, update):
	bot.message.reply_text("Напишите ваше сообщение")


def answer_page_button(bot, update):
	if bot.message is not None:
		user = bot.message.from_user.username
		text = bot.message.text
		update.bot.sendMessage(chat_id=243154734, text=f'Пользователь {user} через бот пишет Вам: {text}')
	elif bot.callback_query.message is not None:
		bot.callback_query.message.reply_text("Напишите ваше сообщение")
