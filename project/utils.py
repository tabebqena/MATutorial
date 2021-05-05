import json
import os

import secrets


def get_random_id(length=1):
    # TODO easy, short
    return secrets.token_hex(length)


def check_db_file():
    from flask import current_app as app

    db = app.config.get("db") or ""
    if not os.path.exists(db):
        f = open(db, "w")
        default_data = {"students": {}, "material": {}}
        f.write(json.dumps(default_data, indent=4))
        f.close()


def get_data():
    from flask import current_app as app

    db = app.config.get("db") or ""
    with open(db, "r") as f:
        data = f.read()
        return json.loads(data)


def update_students_data(new_data):
    from flask import current_app as app

    db = app.config.get("db") or ""

    website_data = get_data()
    website_data["students"] = new_data
    with open(db, "w") as f:
        f.write(json.dumps(website_data, indent=4))


def sum(x, y):
    return x + y