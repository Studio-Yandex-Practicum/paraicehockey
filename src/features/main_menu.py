from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from src.core.constants import ADAPTIVE_HOKKEY_PAGES_TEXT_URLS
from src.features.all_for_hockey import start_all_for_hockey
from src.features.champion_way import redirect_to_champion_way
from src.features.donations import make_donations, page_donations
from src.features.federation_info import (about_fed_main_page,
                                          fed_activities_page, fed_values_page)
from src.features.hockey_types import (redirect_adaptive_hockey_types,
                                       start_hockey_types)
from src.features.question import question_menu_page
from src.features.send_stickers import sending_stickers
from src.features.start import wake_up
from src.features.who_is_fyrk import who_is_fyrk
from src.quiz.quiz import quiz, quiz_menu


def main_menu_keyboard():
    """Клавиатура для главного меню."""
    keyboard = [

        [InlineKeyboardButton('Задать вопрос', callback_data='ask_question'),
         InlineKeyboardButton('🏆 Путь чемпиона 🏅',
                              callback_data='champion_way')],
        [InlineKeyboardButton('ℹ Узнать о Федерации',
                              callback_data='about_federation')],
        [InlineKeyboardButton('Сделать пожертвования',
                              callback_data='make_donation')],
        [InlineKeyboardButton('Адаптивные виды хоккея',
                              callback_data='adaptive_hokkey_types')],
        [InlineKeyboardButton('🏒 Всё для хоккея',
                              callback_data='all_for_hockey'),
         InlineKeyboardButton('Получить стикерпаки',
                              callback_data='get_stickers')],
        [InlineKeyboardButton('🦝 Кто такой Фырк?',
                              callback_data='who_is_fyrk')],
        [InlineKeyboardButton('Квиз', callback_data='quiz'),
         InlineKeyboardButton('Назад', callback_data='back')],
    ]
    return InlineKeyboardMarkup(keyboard)


def main_menu(update: Update, context: CallbackContext) -> None:
    """Функция для первого сообщения с меню."""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Я могу помочь в этих вопросах',
                             reply_markup=main_menu_keyboard())


MAIN_MENU_COMMANDS = {
    'champion_way': redirect_to_champion_way,
    'make_donation': page_donations,
    'donate': make_donations,
    'back': wake_up,
    'who_is_fyrk': who_is_fyrk,
    'main_menu': main_menu,
    'about_federation': about_fed_main_page,
    'fed_values': fed_values_page,
    'fed_activities': fed_activities_page,
    'ask_question': question_menu_page,
    'all_for_hockey': start_all_for_hockey,
    'get_stickers': sending_stickers,
    'start_page': wake_up,
    'adaptive_hokkey_types': start_hockey_types,
    'adaptive_types': start_hockey_types,
    'quiz': quiz_menu,
    'quiz_questions': quiz
}


def redirect_main_menu(update: Update,
                       context: CallbackContext) -> None:
    """Функция для обработки сигнала от кнопок главного меню раздела."""
    query = update.callback_query
    query.answer()
    if query.data in MAIN_MENU_COMMANDS:
        query.delete_message()
        MAIN_MENU_COMMANDS[query.data](update, context)
    # if query.data == 'champion_way':
    #     query.delete_message()
    #     redirect_to_champion_way(update, context)
    # elif query.data == 'make_donation':
    #     query.delete_message()
    #     page_donations(update, context)
    # elif query.data == 'back':
    #     query.delete_message()
    #     wake_up(update, context)
    # elif query.data == 'who_is_fyrk':
    #     query.delete_message()
    #     who_is_fyrk(update, context)
    # elif query.data == 'main_menu':
    #     query.delete_message()
    #     main_menu(update, context)
    # elif query.data == 'all_for_hockey':
    #     query.delete_message()
    #     start_all_for_hockey(update, context)
    # elif query.data == 'get_stickers':
    #     query.delete_message()
    #     sending_stickers(update, context)
    # elif query.data == 'start_page':
    #     query.delete_message()
    #     wake_up(update, context)
    # elif query.data == 'adaptive_hokkey_types':
    #     query.delete_message()
    #     start_hockey_types(update, context)
        # redirect_adaptive_hockey_types(update, context)
    elif query.data in ADAPTIVE_HOKKEY_PAGES_TEXT_URLS:
        query.delete_message()
        redirect_adaptive_hockey_types(update, context)
        # chat_id=update.effective_chat.id
        # keyboard = [
        #     [InlineKeyboardButton('Адаптивные виды хоккея',
        #                           callback_data='adaptive_types')],
        #     [InlineKeyboardButton('Команды',
        #                           url=ADAPTIVE_HOKKEY_PAGES_TEXT_URLS[
        #                               query.data][0])],
        # ]
        # keybord = InlineKeyboardMarkup(keyboard)
        # context.bot.send_message(chat_id=chat_id,
        #                          text=ADAPTIVE_HOKKEY_PAGES_TEXT_URLS[query.data][1],
        #                          parse_mode='HTML',
        #                          reply_markup=keybord)
        # query.edit_message_text(text=ADAPTIVE_HOKKEY_PAGES_TEXT_URLS[
        #                         query.data][1],
        #                         parse_mode='HTML')
        # query.edit_message_reply_markup(reply_markup=keybord)
    # elif query.data == 'sledzh_hockey':
    #     query.delete_message()
    #     keyboard = [
    #         [InlineKeyboardButton('Адаптивные виды хоккея',
    #                               callback_data='adaptive_hockey_types')],
    #         [InlineKeyboardButton('Команды',
    #                               url=SLEDZH_TEAMS_URL)],
    #     ]
    #     keybord = InlineKeyboardMarkup(keyboard)
    #     query.message.reply_photo(photo=open('src/static/images/1.png',
    #                                          'rb'))
    #     query.message.reply_photo(photo=open('src/static/images/2.png',
    #                                          'rb'),
    #                               reply_markup=keybord)
    # elif query.data == 'adaptive_types':
    #     query.delete_message()
    #     context.bot.send_message(chat_id=chat_id,
    #                              text=ADAPTIVE_HOKKEY_MAIN_TEXT,
    #                              parse_mode='HTML',
    #                              reply_markup=adaptive_hockey_keyboard())

        # redirect_adaptive_hockey_types(update, context)
    #     keyboard = [
    #         [InlineKeyboardButton('Адаптивные виды хоккея',
    #                               callback_data='adaptive_hockey_types')],
    #         [InlineKeyboardButton('Команды',
    #                               url=ADAPTIVE_HOKKEY_PAGES_TEXT_URLS[
    #                                   query.data][0])],
    #     ]
    #     keybord = InlineKeyboardMarkup(keyboard)
    #     query.edit_message_text(text=ADAPTIVE_HOKKEY_PAGES_TEXT_URLS[
    #                             query.data][1],
    #                             parse_mode='HTML')
    #     query.edit_message_reply_markup(reply_markup=keybord)
    # elif query.data == 'sledzh_hockey':
    #     query.delete_message()
    #     keyboard = [
    #         [InlineKeyboardButton('Адаптивные виды хоккея',
    #                               callback_data='adaptive_hockey_types')],
    #         [InlineKeyboardButton('Команды',
    #                               url=SLEDZH_TEAMS_URL)],
    #     ]
    #     keybord = InlineKeyboardMarkup(keyboard)
    #     query.message.reply_photo(photo=open('src/static/images/1.png',
    #                                          'rb'))
    #     query.message.reply_photo(photo=open('src/static/images/2.png',
    #                                          'rb'),
    #                               reply_markup=keybord)
    # elif query.data == 'adaptive_hockey_types':
    #     query.delete_message()
    #     query.message.reply_text(ADAPTIVE_HOKKEY_MAIN_TEXT,
    #                              parse_mode='HTML',
    #                              reply_markup=adaptive_hockey_keyboard())
