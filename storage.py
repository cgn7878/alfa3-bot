# storage.py

import json
import os

DATA_FILE = "followed_coins.json"

def load_followed_coins():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_followed_coins(coins):
    with open(DATA_FILE, "w") as f:
        json.dump(coins, f, indent=2)

def get_followed_coins():
    return load_followed_coins()

def add_coin_to_follow(coin_id):
    coins = load_followed_coins()
    if coin_id not in coins:
        coins.append(coin_id)
        save_followed_coins(coins)
        return True
    return False

def remove_coin_from_follow(coin_id):
    coins = load_followed_coins()
    if coin_id in coins:
        coins.remove(coin_id)
        save_followed_coins(coins)
        return True
    return False
