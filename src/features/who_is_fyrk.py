from telegram import ReplyKeyboardMarkup


def who_is_fyrk(update, context):
    chat = update.effective_chat
    reply_markup = ReplyKeyboardMarkup([
        ['Меню', 'На главную']
    ], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет! Давай знакомиться. Это я и моя семья.',
        reply_markup=reply_markup)
    context.bot.send_photo(
        chat.id,
        open('src/static/images/картинка №6.png', 'rb')
    )
    context.bot.send_photo(
        chat.id,
        open('src/static/images/картинка №7.png', 'rb')
    )
    context.bot.send_photo(
        chat.id,
        open('src/static/images/картинка №8.png', 'rb')
    )
