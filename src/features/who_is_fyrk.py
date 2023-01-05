from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def who_is_fyrk(update, context):
    chat = update.effective_chat

    keyboard = [[InlineKeyboardButton('Меню', callback_data='main_menu')],
                [InlineKeyboardButton(
                    'На главную', callback_data='start_page')]]
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет! Давай знакомиться. Это я и моя семья.')
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
        open('src/static/images/картинка №8.png', 'rb'),
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
