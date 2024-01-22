# routes/__init__.py
from .notes_route import init_notes_routes
from .users_route import init_user_routes

def init_app_routes(app):
    init_notes_routes(app)
    init_user_routes(app)
