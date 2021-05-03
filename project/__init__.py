import http
from flask import Flask
from .utils import check_db_file


# Automated test
# add materials


def create_app(config=None) -> Flask:
    check_db_file()

    app: Flask = Flask(__name__)

    app.app_context().push()

    # don't delete this line.
    from .students_routes import student_info

    @app.route("/index")
    @app.route("/")
    def index():
        return "Hello, This is the index page", http.HTTPStatus.OK

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port="5000", debug=True)
