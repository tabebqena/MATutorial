import os
import json
from flask import Flask, request, jsonify


app = Flask(__name__)


# refactoring ,
# test , Automated test
# git

website_data = {}


if not os.path.exists("data.json"):
    f = open("data.json", "w")
    default_data = {"students": {}, "material": {}}
    f.write(json.dumps(default_data, indent=4))
    f.close()
    website_data = default_data
else:
    with open("data.json", "r") as f:
        data = f.read()
        print(data)
        data = json.loads(data)
        print(data)
        website_data = data


def update_students_data(new_data):
    website_data["students"] = new_data
    with open("data.json", "w") as f:
        f.write(json.dumps(website_data, indent=4))


@app.route("/index")
@app.route("/")
def index():
    return "Hello, This is the index page"


@app.route("/students")
def students():
    # show list of all students
    return website_data["students"]


@app.route("/students/new", methods=["PUT"])
def new_student():
    students_data = website_data["students"]
    info = request.form

    if len(info) == 0:
        return jsonify({"state": "Error"}), 204
    id = len(students_data) + 1
    students_data[id] = info

    update_students_data(students_data)

    return jsonify({"state": "Created", "id": id}), 200


@app.route("/students/<int:id>", methods=["GET", "POST", "DELETE"])
def student_info(id):
    # show info of single student
    info = request.form
    students_data = website_data["students"]

    if request.method == "GET":
        return jsonify(students_data[id])
        # sync , request, website_data, data.json

    elif request.method == "POST":
        if students_data.get(id, None):
            students_data[id] = info

            update_students_data(students_data)

            return jsonify({"state": "updated"}), 200
        else:
            return jsonify({"state": "Error"}), 400
    elif request.method == "DELETE":
        if students_data.get(id, None):
            del students_data[id]
            update_students_data(students_data)
            return jsonify({"state": "Deleted"}), 200
        else:
            return jsonify({"state": "Error"}), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)


# http get http://127.0.0.1:5000/students/1  id=1  it works , the port was missed