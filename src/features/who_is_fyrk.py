from telegram import ReplyKeyboardMarkup

from src.core.constants import IMAGE_FYRK, IMAGE_FANY, IMAGE_FEDOR


def who_is_fyrk(update, context):
    chat = update.effective_chat
    reply_markup = ReplyKeyboardMarkup([
        ['Меню', 'На главную']
    ], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет! Давай знакомиться. Это я и моя семья.',
        reply_markup=reply_markup)
    context.bot.send_photo(chat.id, IMAGE_FYRK)
    context.bot.send_photo(chat.id, IMAGE_FANY)
    context.bot.send_photo(chat.id, IMAGE_FEDOR)
