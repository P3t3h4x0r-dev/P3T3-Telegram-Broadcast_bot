#cogs/Text.py
import logging
import os
from config import ADMIN_USER_ID

def register_handlers(bot):
    @bot.message_handler(content_types=['document'])
    def handle_file(message):
        FILE_DIR = 'files'

        logging.basicConfig(level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler('bot.log', encoding='utf-8'),
        logging.StreamHandler()])
        logger = logging.getLogger(__name__)

        if message.chat.type == 'private' and message.from_user.id == ADMIN_USER_ID:
            try:
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
            
                file_path = os.path.join(FILE_DIR, message.document.file_name)
                with open(file_path, 'wb') as new_file:
                    new_file.write(downloaded_file)
            
                bot.reply_to(message, f"File {message.document.file_name} stored successfully!")
                logger.info(f"File {message.document.file_name} stored by {message.from_user.username} ({message.chat.id})")
            except Exception as e:
                bot.reply_to(message, "There was an error storing the file.")
                logger.error(f"Error storing file {message.from_user.username} ({message.chat.id}): {e}")
        else:
            bot.reply_to(message, "You are not authorized to upload files to this bot.")
            logger.info(f"Attempt to send unauthorized file by {message.from_user.username} ({message.chat.id})")


    
