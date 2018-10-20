import tele_bot_tools as tbt
from os import environ
from app import bot
from app import db
from app import models


#Рандомно выбираем куда пойдет рынок и выдаем нужную фразу
def market_wizard():
    #TODO Выбрать направление
    #TODO Посмотреть прошлое направление
    #TODO Выбрать соответствующую фразу из БД и отдать
    return models.answ.query.all()


@bot.message_handler(commands=['start'])
def hi_msg(message):
    bot.send_message(environ['channel_name'], market_wizard())
    bot.send_message(message.chat.id, 'Start', reply_markup=tbt.order_row_keyboard(['a', 'b', 'c', 'd']))

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data:
        pass