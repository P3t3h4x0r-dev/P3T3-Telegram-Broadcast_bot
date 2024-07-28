#main.py

import telebot
from flask import Flask, request, jsonify
from cogs import register_handlers
from config import TOKEN

app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)

register_handlers(bot)

if __name__ == '__main__':
    bot.polling(none_stop=True)


