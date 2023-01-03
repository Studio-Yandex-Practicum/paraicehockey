from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext


def wake_up(update: Update, context: CallbackContext) -> None:
    """Стартовое меню."""
    chat = update.effective_chat
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton('Задать вопрос', callback_data='ask_question'),
          InlineKeyboardButton('Меню',
                               callback_data='main_menu')]])
    # context.bot.send_video(chat_id=chat.id,
    #                        video=open(
    #                        'src/static/images/Sledge_hockey_Logo_Rus.mpeg',
    #                        'rb'),
    #                        supports_streaming=True)
    context.bot.send_sticker(chat_id=chat.id,
                             sticker=open('src/static/images/fyrk_smile.webp',
                                          'rb'))
    # context.bot.send_photo(chat_id=chat.id,
    #                        photo=open(
    # 'src/static/images/fyrk_smile.webp', 'rb'))
    context.bot.send_message(chat_id=chat.id,
                             text='Выбери раздел меню.',
                             reply_markup=keyboard)
