"""
Ce module contient les services liés à la gestion des utilisateurs,
y compris la création de nouveaux utilisateurs et l'authentification.
"""
from flask_bcrypt import generate_password_hash, check_password_hash
from app.models.users_model import User


def create_user(username, password):
    """
    Crée un nouvel utilisateur avec un mot de passe haché.

    Args:
        username (str): Le nom d'utilisateur.
        password (str): Le mot de passe en clair.

    Returns:
        User: L'instance de l'utilisateur créé.
    """
    hashed_password = generate_password_hash(password).decode("utf-8")
    new_user = User(username, hashed_password)
    new_user.save()
    return new_user


def authenticate_user(username, password):
    """
    Vérifie les identifiants de connexion d'un utilisateur.

    Args:
        username (str): Le nom d'utilisateur.
        password (str): Le mot de passe.

    Returns:
        User | None: L'objet User si l'authentification réussit, sinon None.
    """
    user = User.find_by_username(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None
