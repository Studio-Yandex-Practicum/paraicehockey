import os
from dotenv import load_dotenv

from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import ReplyKeyboardMarkup

load_dotenv()

token = os.getenv('TOKEN')

updater = Updater(token=token) 


def wake_up(update, context):
    '''handler whith button'''
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['start']], resize_keyboard=True)
    context.bot.send_message(chat_id=chat.id, 
                             text=f'Спасибо, {name}, что включил меня', reply_markup=button)

def say_hi(update, context):
    '''handler that intercept all messages'''
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(chat_id=chat.id, text=f'Эй, {name}! Давай играть в хоккей!')
    
    
def main():
    updater = Updater(token=token) 

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main() 
