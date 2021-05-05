import json
import os
import pytest
from project import create_app
from flask import Flask


@pytest.fixture
def app() -> Flask:
    db = "test_db.json"
    yield create_app(custom_config={"db": db})

    if os.path.exists(db):
        os.remove(db)
        pass


def test_add_student(app):
    with app.test_client() as client:
        student_data = {"name": "aly", "class": "2"}
        response = client.put("/students", data=student_data)
        # print(dir(response))
        id = response.json.get("id")

        print("student id : ", id)

        assert response.status_code == 200
        assert response.json.get("state") == "Created"
        assert id is not None

        with open(app.config.get("db"), "r") as f:
            data = f.read()
            data = json.loads(data)
            assert data["students"][id] == student_data


#
