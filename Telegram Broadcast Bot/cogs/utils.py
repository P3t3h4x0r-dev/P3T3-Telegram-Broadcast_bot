# cogs/utils.py

import json

def get_subscribers():
    try:
        with open('data/subscribers.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_subscriber(user_id):
    subscribers = get_subscribers()
    if user_id not in subscribers:
        subscribers.append(user_id)
        with open('data/subscribers.json', 'w') as file:
            json.dump(subscribers, file)

def remove_subscriber(user_id):
    subscribers = get_subscribers()
    if user_id in subscribers:
        subscribers.remove(user_id)
        with open('data/subscribers.json', 'w') as file:
            json.dump(subscribers, file)