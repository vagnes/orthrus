import json


def config():
    with open("config.json", "r") as file:
        content = json.load(file)

    return content
