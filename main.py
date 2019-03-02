from os import listdir
from os.path import isfile, join
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import urllib2

APItoken = '563443635:AAG6OG4T3fhY_qpYJLMfCL7k6TsPjc_Syl4'
bot = telebot.TeleBot(APItoken)
print ('starting tool')
bot_chat_id= -272117205


def send_message():

    try:
            bot.send_photo(bot_chat_id, get_photo_file)
    except:
        print("failed to send")

def get_new_chat_id():
    print("enter new group ID")
    #read in new id to file

def get_chat_id():
    print("accessing file for id")

def get_photo_file():
    return "https://drive.google.com/file/d/0B9s05X824aYlcnJVOTl0R2hNOGM/view?usp=sharing"


#starts bot
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):

    print("chat_id: "+ str(bot_chat_id))

    bot.send_message(bot_chat_id, "starting shit")

    send_message()
    pass

bot.polling()