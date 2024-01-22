"""
Ce module verifie la validation des champs requis dans la requête JSON.
"""
from functools import wraps
from flask import request, jsonify


def validate_required_fields(required_fields):
    """
    Décorateur pour valider les champs requis dans la requête JSON.

    Args:
        required_fields (list): Liste des champs requis.

    Returns:
        Function: La fonction décorée.
    """

    def decorator_validate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            data = request.get_json()
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                return (
                    jsonify(
                        {
                            "msg": "Champs requis manquants : "
                            + ", ".join(missing_fields)
                        }
                    ),
                    400,
                )
            return fn(*args, **kwargs)

        return wrapper

    return decorator_validate
