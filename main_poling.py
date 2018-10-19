import core_bot
import telebot
from os import environ

bot = telebot.TeleBot(environ['token'])

core_bot.main_check(bot)

if __name__ == '__main__':
    bot.polling(none_stop=True)