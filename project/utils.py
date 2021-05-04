import json
import os

import secrets


def get_random_id(length=1):
    # TODO easy, short
    return secrets.token_hex(length)


# 10 + 28 = 38 * 38 = 1444 ... 1445


def check_db_file():
    if not os.path.exists("data.json"):
        f = open("data.json", "w")
        default_data = {"students": {}, "material": {}}
        f.write(json.dumps(default_data, indent=4))
        f.close()


def get_data():
    with open("data.json", "r") as f:
        data = f.read()
        return json.loads(data)


def update_students_data(new_data):
    website_data = get_data()
    website_data["students"] = new_data
    with open("data.json", "w") as f:
        f.write(json.dumps(website_data, indent=4))


def sum(x, y):
    return x + y