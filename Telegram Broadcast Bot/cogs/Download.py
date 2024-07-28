#cogs/Download.py

from config import CHAT_ID
import os 

FILES_DIR = 'files' 

def list_files():

    return os.listdir(FILES_DIR)


def register_handlers(bot):
    @bot.message_handler(commands=['file'])
    def get_file_handler(message):
            if message.chat.id != CHAT_ID:
                bot.reply_to(message, "This command can only be used in the authorized group.")
                return
    
            try:
                _, file_number = message.text.split()
                file_number = int(file_number) - 1
                files = list_files()
                if 0 <= file_number < len(files):
                    file_name = files[file_number]
                    file_path = os.path.join(FILES_DIR, file_name)
                    with open(file_path, 'rb') as file:
                        bot.send_document(message.chat.id, file)
                else:
                    bot.reply_to(message, "Invalid file number.")
            except (IndexError, ValueError):
                bot.reply_to(message, "Incorrect use of the command. Use /file <number> to request a file.")