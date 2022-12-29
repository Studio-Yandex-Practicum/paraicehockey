from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, Update,
                      WebAppInfo)
from telegram.ext import CallbackContext

from src.core.constants import ALL_FOR_HOKKEY_MAIN_TEXT, HOCKEY_EQUIPMENT_URL


def all_for_hockey_keyboard():
    """Клавиатура для главного меню 'Всё для хоккея'."""
    web_app_test = WebAppInfo('https://kolosova411.pythonanywhere.com/')
    keyboard = [
        [InlineKeyboardButton('Хоккейный инвентарь и экипировка',
                              url=HOCKEY_EQUIPMENT_URL)],
        [InlineKeyboardButton('Атрибутика Федерации', web_app=web_app_test)],
        [InlineKeyboardButton('Меню', callback_data='main_menu')],
        [InlineKeyboardButton('На главную', callback_data='start_page')],
    ]
    return InlineKeyboardMarkup(keyboard)


# def start_all_for_hockey():
#     #создание клавиатуры с webapp кнопкой
#     # keyboard = ReplyKeyboardMarkup() #создаем клавиатуру
#     # webAppTest = WebAppInfo("https://hockey-family.com/shop")
#     webAppTest = WebAppInfo('https://codepen.io/ekolosova/full/jOpbbOP')
#     one_butt = [[KeyboardButton('Нажми, чтобы открыть магазин',
#                                 web_app=webAppTest)]]
#     # keyboard.add(one_butt) #добавляем кнопки в клавиатуру
#     # setChatMenuButton()

#     return ReplyKeyboardMarkup(one_butt) #возвращаем клавиатуру
#     """Функция для первого сообщения с меню 'Всё для хоккея'."""
#     # update.message.reply_photo(photo=open('src/static/шайба.jpg', 'rb'))
#     update.message.reply_text(ALL_FOR_HOKKEY_MAIN_TEXT,
#                               parse_mode='HTML',
#                               reply_markup=all_for_hockey_keyboard())

def show_product(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(text=ALL_FOR_HOKKEY_MAIN_TEXT,
                             chat_id=update.message.chat.id,
                             reply_markup=all_for_hockey_keyboard())
    # keyboard = [
    #     [InlineKeyboardButton('Предыдущий', callback_data='previous'),
    #     InlineKeyboardButton('Купить',
    #      url='https://hockey-family.com/shop#!/tproduct/171831854-1500389007550'),
    #     InlineKeyboardButton('Следующий', callback_data='next')]
    # ]
    # sell_keyboard = InlineKeyboardMarkup(keyboard)
    # update.message.reply_photo(photo=open('src/static/шайба.jpg', 'rb'),
    #                            reply_markup=ReplyKeyboardRemove())
    # update.message.reply_text('Шайба сувенирная - 450 руб.',
    #                           parse_mode='HTML',
    #                           reply_markup=sell_keyboard)
# @bot.message_handler(content_types="web_app_data")
# def shop_answer(update, context):
#     # query = update.callback_query
#     # query.answer()
#     data = update.effective_message.web_app_data.data
#     update.message.reply_html(
#         text=f"You selected the color with the HEX value
#          <code>{data['hex']}</code>. The "
#         f"corresponding RGB value is <code>{data}</code>.",
#         reply_markup=ReplyKeyboardRemove(),
#     )
#     if query.data == 'web_app_data':
#         # print(webAppMes) #вся информация о сообщении
#         # print(webAppMes.web_app_data.data)
#         #конкретно то что мы передали в бота
#         # update.message.reply_html(reply_markup=ReplyKeyboardRemove())
#         context.bot.send_message(webAppMes.chat.id,
#               f"получили инофрмацию из веб-приложения: {webAppMes.data}")
#    отправляем сообщение в ответ на отправку данных из веб-приложения


# def redirect_all_for_hockey(update: Update, context: CallbackContext):
#     """Функция для обработки сигнала от кнопок главного меню раздела.
#     Изменяет текстовое сообщение и кнопки к нему или направляет на
#     страницы сайта с командами.
#     """
#     query = update.callback_query
#     query.answer()
#     if query.data == 'next':
#         pass
#         # query.edit_message_text(reply_markup=show_product(update, context))
#         # query.(media=open('src/static/термостакан.jpg', 'rb'))
#         # chat = update.effective_chat
#         # context.bot.send_photo(
#         # chat.id,
#         'https://static.tildacdn.com/
#          tild6638-3832-4330-b133-656134313361/AASH8940.jpg')
#         # update.message.reply_document(
#         # 'https://static.tildacdn.com/
#            tild6638-3832-4330-b133-656134313361/AASH8940.jpg')
#         # query.bot.send_photo(photo=open('src/static/шайба.jpg', 'r'))
#         # context.bot.send_photo(photo=open('src/static/шайба.jpg', 'r'))
#         # update.message.reply_photo(photo='src/static/шайба.jpg')
#         # keyboard = [
#         #     [InlineKeyboardButton('Предыдущий', callback_data='previous')],
#         #     [InlineKeyboardButton('Купить',
#         #     url='https://hockey-family.com/shop#!/
#                    tproduct/171831854-1500389007550')],
#         #     [InlineKeyboardButton('Следующий', callback_data='next')]
#         # ]
#         # keybord = InlineKeyboardMarkup(keyboard)
#         # query.edit_message_text(text='название товара',
#         #                         parse_mode='HTML', reply_markup=keybord)
#         # query.edit_message_reply_markup(reply_markup=keybord)
#     # elif query.data == 'adaptive_hockey_types':
#     #     query.edit_message_text(text=ADAPTIVE_HOKKEY_MAIN_TEXT,
#     #                             parse_mode='HTML')
#     #     query.edit_message_reply_markup(
#     #         reply_markup=adaptive_hockey_keyboard())
#     elif ((query.data == 'start_page') or (query.data == 'main_menu')):
#         query.delete_message()
#         # TODO: Сделать переход на стартовую страницу
#         # TODO: Сделать переход на главное меню
#     # else:
#     #     query.edit_message_text(text=f'Selected option: {query.data}')
