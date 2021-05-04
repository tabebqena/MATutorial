from flask import request, jsonify, abort

from flask import current_app as app

from .utils import get_data, update_students_data, get_random_id
import http


@app.route("/students")
def students():
    # show list of all students
    return get_data()["students"], http.HTTPStatus.OK


@app.route("/students/new", methods=["PUT"])
def add_student():
    students_data = get_data()["students"]
    info = request.form

    # TODO FIX: more accurate validator
    if len(info) == 0:
        return jsonify({"state": "Error"}), http.HTTPStatus.NO_CONTENT

    # TODO add checker function to ensure no duplicate id.
    id = None
    while True:
        id = get_random_id()  # len(students_data) + 1
        if not students_data.get(id):
            break

    students_data[id] = info

    update_students_data(students_data)

    return jsonify({"state": "Created", "id": id}), http.HTTPStatus.OK


@app.route("/students/<string:id>", methods=["GET"])
def get_student_info(id):
    # show info of single student
    students_data = get_data()["students"]
    if students_data.get(id, None):
        return jsonify(students_data[id]), http.HTTPStatus.OK
    return jsonify({"state": "Error"}), http.HTTPStatus.NOT_FOUND


@app.route("/students/<string:id>", methods=["POST"])
def update_student(id):
    info = request.form
    students_data = get_data()["students"]
    if students_data.get(id, None):
        students_data[id] = info
        update_students_data(students_data)
        return jsonify({"state": "updated"}), http.HTTPStatus.OK
    else:
        # don't delete , it is an example
        # abort(http.HTTPStatus.BAD_REQUEST, f"No student with this {id}")
        return jsonify({"state": "Error"}), http.HTTPStatus.BAD_REQUEST


@app.route("/students/<string: id>", methods=["DELETE"])
def delete_student(id):
    students_data = get_data()["students"]
    if students_data.get(id, None):
        del students_data[id]
        update_students_data(students_data)
        return jsonify({"state": "Deleted"}), http.HTTPStatus.OK
    else:
        return jsonify({"state": "Error"}), http.HTTPStatus.BAD_REQUEST
