import json


def json_load(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data
