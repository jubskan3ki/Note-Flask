"""
Ce module fournit des décorateurs pour la gestion de l'authentification JWT.
"""
from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request


def jwt_required(fn):
    """
    Décorateur pour exiger un JWT valide dans la requête.

    Args:
        fn (function): La fonction à décorer.

    Returns:
        Function: La fonction décorée.
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except Exception:
            return jsonify(msg="Accès refusé, token invalide ou absent."), 401
        return fn(*args, **kwargs)

    return wrapper
