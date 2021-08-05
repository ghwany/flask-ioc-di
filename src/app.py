from flask import Flask, json
from werkzeug.exceptions import HTTPException
import os

from container import Container
from models import db
from controllers.api import user


def middleware_app(app) -> Flask:
    @app.errorhandler(HTTPException)
    def handle_exception(e):
        response = e.get_response()
        response.data = json.dumps(
            {
                "code": e.code,
                "name": e.name,
                "description": e.description,
            }
        )
        response.content_type = "application/json"
        return response


def create_app():
    container = Container()
    container.wire(modules=[user])

    app = Flask(__name__)
    app.container = container

    if "FLASK_CONFIG" not in os.environ:
        os.environ["FLASK_CONFIG"] = "../config/{}.env".format(os.environ.get("ENV", "development"))
    app.config.from_envvar("FLASK_CONFIG")
    app.config["SQLALCHEMY_DATABASE_URI"] = "{}://{}:{}@{}:{}/{}?charset=utf8".format(
        app.config["DBMS"],
        app.config["DB_USER"],
        app.config["DB_PASSWORD"],
        app.config["DB_HOST"],
        app.config["DB_PORT"],
        app.config["DB_NAME"],
    )

    app.register_blueprint(user.blueprint)

    db.init_app(app)

    middleware_app(app)

    return app
