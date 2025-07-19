import json
import os

DATA_FILE = "data.json"

def _load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def _save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get(key, default=None):
    data = _load_data()
    return data.get(key, default)

def set(key, value):
    data = _load_data()
    data[key] = value
    _save_data(data)

def delete(key):
    data = _load_data()
    if key in data:
        del data[key]
        _save_data(data)
