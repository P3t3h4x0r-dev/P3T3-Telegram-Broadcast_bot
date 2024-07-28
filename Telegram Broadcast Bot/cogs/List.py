# cogs/list.py

import os
from telebot import TeleBot
from config import CHAT_ID

FILES_DIR = 'files'  

def list_files():

    return os.listdir(FILES_DIR)

def register_handlers(bot: TeleBot):
    @bot.message_handler(commands=['list'])
    def list_files_handler(message):
        if message.chat.id != CHAT_ID:
            bot.reply_to(message, "This command can only be used in the authorized group.")
            return
 
        files = list_files()
        if files:
            file_list = "\n".join([f"{idx + 1}. {file}" for idx, file in enumerate(files)])
            response = (
                "Available files:\n"
                f"{file_list}\n\n"
                "Use the /file <number> command to request a file."
            )
            bot.reply_to(message, response)
        else:
            bot.reply_to(message, "Nenhum arquivo disponível no momento.")

