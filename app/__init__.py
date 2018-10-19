from os import environ
from flask import Flask, request
import telebot
from flask_sqlalchemy import SQLAlchemy

bot = telebot.TeleBot(environ['token'])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL']
db = SQLAlchemy(app)

from app import core_bot, models
core_bot(bot)

@app.route("/"+environ['token'], methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


bot.remove_webhook()
bot.set_webhook(url=environ['app_url']+environ['token'])
print(environ.get('PORT', 5000))
app.run(host="0.0.0.0", port=int(environ.get('PORT', 5000)))