import os
from flask import Flask
from .db.core import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
        pass
    else:
        app.config.from_mapping(test_config)
        pass
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    @app.route("/hello")
    def hello():
        return 'hello world mike'

    return app
