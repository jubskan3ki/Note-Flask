"""
Ce module configure les routes de l'API pour les notes dans l'app.
"""

from app.api.notes_api import notes_api


def init_notes_routes(app):
    """
    Enregistre le blueprint des notes sur l'application Flask.

    Args:
        app (Flask): L'instance de l'application Flask.
    """
    app.register_blueprint(notes_api, url_prefix="/api")
