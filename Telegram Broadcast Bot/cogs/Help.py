#cogs/Help.py

from config import CHAT_ID

def register_handlers(bot):
    @bot.message_handler(commands=['help'])
    def send_help(message):
        if message.chat.id == CHAT_ID:
            help_text = (
                "/help - Show this help message\n"
                "/subscribe - Subscribe to receive private messages\n"
                "/unsubscribe - Unsubscribe to stop receiving private messages\n"
                "/broadcast <filename> - Sends specific files to subscribed users\n"
                "/list - Lists stored files\n"
                "/delete <filename> - deletes a specific file\n"
                "/file <filename> - bot sends the specified file in the chat\n"
            )
            bot.reply_to(message, help_text)