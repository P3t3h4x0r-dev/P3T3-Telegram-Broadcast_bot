# cogs/Subscribe.py
from cogs.utils import add_subscriber, remove_subscriber
from config import CHAT_ID


def register_handlers(bot):
    @bot.message_handler(commands=['subscribe'])
    def subscribe(message):
            if message.chat.id == CHAT_ID:
                add_subscriber(message.from_user.id)
                bot.reply_to(message, "You have signed up to receive files.")
            else:
                bot.reply_to(message, "This command can only be used in private chats.")

    @bot.message_handler(commands=['unsubscribe'])
    def unsubscribe(message):
            if message.chat.id == CHAT_ID:
                remove_subscriber(message.from_user.id)
                bot.reply_to(message, "You have unsubscribed from receiving files.")
            else:
                bot.reply_to(message, "This command can only be used in private chats.")