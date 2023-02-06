from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from src.core.constants import ALL_FOR_HOKKEY_MAIN_TEXT, HOCKEY_EQUIPMENT_URL


def all_for_hockey_keyboard():
    """Клавиатура для главного меню раздела 'Всё для хоккея'."""
    keyboard = [
        [InlineKeyboardButton('Хоккейный инвентарь и экипировка',
                              url=HOCKEY_EQUIPMENT_URL)],
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
    ]
    return InlineKeyboardMarkup(keyboard)


def start_all_for_hockey(update: Update, context: CallbackContext) -> None:
    """Функция для первого сообщения с меню раздела 'Всё для хоккея'."""
    context.bot.send_message(text=ALL_FOR_HOKKEY_MAIN_TEXT,
                             chat_id=update.effective_chat.id,
                             reply_markup=all_for_hockey_keyboard())
