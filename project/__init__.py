import http
from flask import Flask

from gevent import config
from .utils import check_db_file


# Automated test
# add materials
# { defa }


def create_app(custom_config={}) -> Flask:
    app: Flask = Flask(__name__)
    app.app_context().push()
    # store the custom config in the app.config
    app.config.update(custom_config)
    if app.config.get("db", None) is None:
        app.config["db"] = "data.json"

    check_db_file()

    # don't delete this line.
    from .students_routes import get_student_info

    @app.route("/index")
    @app.route("/")
    def index():
        return "Hello, This is the index page", http.HTTPStatus.OK

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port="5000", debug=True)
