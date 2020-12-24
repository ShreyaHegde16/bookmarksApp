import json


def load_data():
    with open('./model/data.json', mode='r') as f:
        return json.load(f)


def load_bookmarks(bookmarks):
    with open('./model/data.json', mode='w') as f:
        json.dump(bookmarks, f)
