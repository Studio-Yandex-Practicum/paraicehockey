from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from src.core.settings import settings


def page_donations(update, context):
    """"  Функция для перехода  """
    keyboard = [
        [InlineKeyboardButton('Поддержать', callback_data='donate')],
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
        [InlineKeyboardButton(
            'На главную', callback_data='start_page')]]
    context.bot.send_photo(
        update.effective_chat.id,
        open('src/static/images/Пожертвование 1.png', 'rb'),
        reply_markup=InlineKeyboardMarkup(keyboard))


def make_donations(update, context):
    keyboard = [
        [InlineKeyboardButton('Поддержать', url=settings.url_donation)],
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
        [InlineKeyboardButton(
            'На главную', callback_data='start_page')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_photo(
        update.effective_chat.id,
        open('src/static/images/Пожертвование 2.png', 'rb'),
        reply_markup=reply_markup)
