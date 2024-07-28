#cogs/Delete.py

import logging
import os 
from config import ADMIN_USER_ID
def register_handlers(bot):
    @bot.message_handler(commands=['delete'])
    def delete_file(message):
        if message.chat.type == 'private' and message.from_user.id == ADMIN_USER_ID:
            FILE_DIR = 'files'

            logging.basicConfig(level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[logging.FileHandler('bot.log', encoding='utf-8'),
            logging.StreamHandler()])

            logger = logging.getLogger(__name__)
            file_name = " ".join(message.text.split()[1:])
            file_path = os.path.join(FILE_DIR, file_name)
            os.remove(file_path)
            bot.send_message(message.chat.id, f"File {file_name} deleted successfully.")
            logger.info(f"File {file_name} deleted by {message.from_user.username} ({message.chat.id})")

    