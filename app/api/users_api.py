"""
Ce module gère les routes d'API pour les fonctionnalités liées aux utilisateur,
telles que l'enregistrement et la connexion.
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.services.user_service import create_user, authenticate_user
from app.middleware import validate_required_fields

users_api = Blueprint("users_api", __name__)


@users_api.route("/users/register", methods=["POST"])
@validate_required_fields(["username", "password"])
def register():
    """
    Enregistre un nouvel utilisateur.

    Args:
        username (str): Le nom d'utilisateur.
        password (str): Le mot de passe.

    Returns:
        JSON: Message de confirmation avec un code de statut HTTP 201.
    """
    data = request.json
    create_user(data["username"], data["password"])
    return jsonify({"message": "Utilisateur créé avec succès"}), 201


@users_api.route("/users/login", methods=["POST"])
@validate_required_fields(["username", "password"])
def login():
    """
    Authentifie un utilisateur et fournit un JWT.

    Args:
        username (str): Le nom d'utilisateur.
        password (str): Le mot de passe.

    Returns:
        JSON: JWT en cas de succès ou message d'erreur avec le code de
        statut HTTP approprié.
    """
    data = request.json
    user = authenticate_user(data["username"], data["password"])
    if user:
        access_token = create_access_token(identity=data["username"])
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Échec de la connexion"}), 401
