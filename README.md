# Telegram Bot Documentation


## Introduction


	 This bot for Telegram is focused on file sharing on private servers and for Broadcast.

## Requirement


    Python 3.12 or higher
    Telebot

## Library installation


    pip install telebot
    or run the requirements.bat file

## Configuration

**Settings in the Config.py file**

    TOKEN = 'Bot token' #Replace with the bot token
    
    ADMIN_USER_ID = <Administrator user ID> #Replace with your Telegram user ID
    
    CHAT_ID = -<Chat ID where the bot will be> #Replace with your Telegram chat ID**

## Starting the bot
    python main.py or run run.bat

## Administration

**handling files in the bot:**

### to send and delete files it is necessary to do it in the bot's private chat (only the administrator can handle files, store, delete and send broadcast). To store files, just send them to the bot in the private chat
    
**Admin commands:**

    /broadcast <filename> #sends the file to all users who subscribed to the broadcast
    

    /delete <filename> #deletes the stored file

**User Commands**

    /list #Lists all stored files
    
    /subscribe #the user can receive files via broadcast
    
    /unsubscribe #the user no longer receives files via broadcast
    
    /file <filename> #the bot sends the stored file in the chat
    
    /help #lists the bot commands

## config.py
    Admin configuration file

## Subscribers.json file
    Subscriber IDs are stored in a JSON file (subscribers.json). The load_subscribers, save_subscribers, add_subscriber, and remove_subscriber functions are used to manage these IDs.
