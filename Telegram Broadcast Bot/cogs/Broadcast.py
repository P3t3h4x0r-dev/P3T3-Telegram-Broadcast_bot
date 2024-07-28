# cogs/Broadcast.py

import json
import os
from telebot import TeleBot
from telebot.types import Message
from config import ADMIN_USER_ID, CHAT_ID

SUBSCRIBERS_FILE = 'data/subscribers.json'
FILES_DIR = 'files'

def load_subscribers():
    if os.path.exists(SUBSCRIBERS_FILE):
        with open(SUBSCRIBERS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_subscribers(subscribers):
    with open(SUBSCRIBERS_FILE, 'w') as file:
        json.dump(subscribers, file)

def add_subscriber(user_id):
    subscribers = load_subscribers()
    if user_id not in subscribers:
        subscribers.append(user_id)
        save_subscribers(subscribers)

def remove_subscriber(user_id):
    subscribers = load_subscribers()
    if user_id in subscribers:
        subscribers.remove(user_id)
        save_subscribers(subscribers)

def register_handlers(bot: TeleBot):
    @bot.message_handler(commands=['broadcast'])
    def broadcast_handler(message: Message):
        if message.chat.id == CHAT_ID and message.from_user.id == ADMIN_USER_ID:
        
            if len(message.text.split()) < 2:
                bot.reply_to(message, "Please provide the name of the file to be uploaded. Example: /broadcast filename")
                return

            file_name = message.text.split()[1]
            file_path = os.path.join(FILES_DIR, file_name)

            if not os.path.exists(file_path):
                bot.reply_to(message, f"File '{file_name}' not found.")
                return

            subscribers = load_subscribers()
            for subscriber in subscribers:
                try:
                    with open(file_path, 'rb') as file:
                        bot.send_document(subscriber, file)
                except Exception as e:
                    print(f"Could not send to {subscriber}: {e}")

            bot.reply_to(message, "Broadcast sent.")