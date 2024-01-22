"""
Ce module configure les routes de l'API pour les utilisateurs dans l'app.
"""

from app.api.users_api import users_api


def init_user_routes(app):
    """
    Enregistre le blueprint des utilisateurs sur l'application Flask.

    Args:
        app (Flask): L'instance de l'application Flask.
    """
    app.register_blueprint(users_api, url_prefix="/api")
