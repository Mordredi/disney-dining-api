import os
from flask import Flask

from flask_migrate import Migrate

from disney_dining.controllers.restaurants import restaurants
from disney_dining.controllers.users import users
from disney_dining.db import db
from disney_dining.scripts.load_restaurants import load_restaurants


migrate = Migrate()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(restaurants, url_prefix="/restaurants")
    app.register_blueprint(users, url_prefix="/users")
    app.cli.add_command(load_restaurants)
    return app
