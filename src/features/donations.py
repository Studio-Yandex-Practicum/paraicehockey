from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from src.core.settings import settings


def page_donations(update, context):
    """Функция для перехода к меню и выдаче скрина с тратами организации."""
    keyboard = [
        [InlineKeyboardButton('Поддержать', url=settings.url_donation)],
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_photo(
        update.effective_chat.id,
        open('src/static/images/Donate_1.png', 'rb'))
    context.bot.send_photo(
        update.effective_chat.id,
        open('src/static/images/donations.png', 'rb'),
        reply_markup=reply_markup)
