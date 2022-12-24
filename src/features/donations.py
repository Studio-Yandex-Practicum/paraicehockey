from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    ReplyKeyboardMarkup
)

from src.core.constants import TEXT_DONATION, URL_DONATION


def page_donations(update, context):
    chat = update.effective_chat
    reply_markup = ReplyKeyboardMarkup([
        ['Поддержать', 'Меню', 'На главную']
    ], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Все дети могут заниматься спортом, их нужно только поддержать!',
        reply_markup=reply_markup)
    context.bot.send_message(
        chat_id=chat.id,
        text='\n'.join(TEXT_DONATION),
        parse_mode=ParseMode.MARKDOWN)


def make_donations(update, context):
    keyboard = [
        [InlineKeyboardButton('Поддержать', url=URL_DONATION),]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Нажмите на кнопку ниже 🔽',
        reply_markup=reply_markup)
