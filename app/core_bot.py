import tele_bot_tools as tbt
from os import environ
from app import bot
from app import db
from app import models
import random
import time


#Рандомно выбираем куда пойдет рынок и выдаем нужную фразу
def market_wizard(tempdb):
    #TODO Выбрать направление
    buysell = random.randrange(-3,4)

    #TODO Посмотреть прошлое направление
    lastdir = tempdb.Lastpos

    #TODO Выбрать соответствующую фразу из БД и отдать
    rand = random.randrange(0,models.answ.query.count())
    message = models.answ.query.get(rand)

    an = ''
    
    while True:
        if buysell > 0:
            if buysell == lastdir:
                    an = message.Buy
            else:
                an = message.Buych
        elif buysell < 0:
            if buysell == lastdir:
                an = message.Sell
            else:
                an = message.Sellch
        else:
            if buysell == lastdir:
                buysell = random.randrange(-3,4)
                continue
            else:
                an = message.Stop
        
        tempdb.Lastpos = buysell
        db.session.add(tempdb)
        db.session.commit()
        return an

tempdb = models.answ.query.get(0)
lasttime = tempdb.Lasttime
curtime = int(time.time())
divtime = curtime - lasttime
if divtime > 1800:
        if random.randrange(divtime/100,100) > 80:
                tempdb.Lasttime = curtime
                bot.send_message(environ['channel_name'], market_wizard(tempdb))
                



@bot.message_handler(commands=['start'])
def hi_msg(message):
    pass
    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data:
        pass