"""
Ce module crée et configure une instance de l'application Flask,
y compris l'initialisation des extensions et des routes.
"""

from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from config import Config
from .api.notes_api import notes_api
from .api.users_api import users_api
from .routes import init_notes_routes, init_user_routes

mongo = PyMongo()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    """
    Crée une instance de l'application Flask
    et configure ses extensions et routes.

    Returns:
        Flask: L'instance configurée de l'application Flask.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(notes_api)
    app.register_blueprint(users_api)

    init_notes_routes(app)
    init_user_routes(app)

    return app
