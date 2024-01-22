"""
Ce module définit les routes de l'API pour la gestion des notes.
Il inclut les fonctionnalités pour :
créer, récupérer, mettre à jour et supprimer des notes.
"""
from flask import Blueprint, request, jsonify
from app.middleware import jwt_required, validate_required_fields
from app.services.note_service import (
    create_note,
    get_all_notes,
    get_note_by_id,
    update_note,
    delete_note,
)

notes_api = Blueprint("notes_api", __name__)


@notes_api.route("/notes", methods=["POST"])
@jwt_required
@validate_required_fields(["title", "content"])
def add_note():
    """
    Crée une nouvelle note. L'utilisateur doit être authentifié.

    Args:
        - title (str): Le titre de la note.
        - content (str): Le contenu de la note.
        - user_id (str): L'ID de l'utilisateur (obtenu du JWT).

    Returns:
        JSON: La note créée avec un code de statut HTTP 201.
    """
    data = request.json
    note = create_note(data["title"], data["content"], data["user_id"])
    return jsonify(note), 201


@notes_api.route("/notes", methods=["GET"])
@jwt_required
def get_notes():
    """
    Récupère toutes les notes.
    L'utilisateur doit être authentifié.

    Returns:
        JSON: Liste des notes avec un code de statut HTTP 200.
    """
    notes = get_all_notes()
    return jsonify(notes), 200


@notes_api.route("/notes/<note_id>", methods=["GET"])
@jwt_required
def get_note(note_id):
    """
    Récupère une note spécifique par son ID.
    L'utilisateur doit être authentifié.

    Args:
        note_id (str): L'ID de la note.

    Returns:
        JSON: La note demandée ou un message d'erreur,
        avec le code de statut HTTP approprié.
    """
    note = get_note_by_id(note_id)
    if note:
        return jsonify(note), 200
    return jsonify({"message": "Note not found"}), 404


@notes_api.route("/notes/<note_id>", methods=["PUT"])
@jwt_required
def update_note_route(note_id):
    """
    Met à jour une note spécifique. L'utilisateur doit être authentifié.

    Args:
        note_id (str): L'ID de la note.
        title (str): Le nouveau titre.
        content (str): Le nouveau contenu.

    Returns:
        JSON: La note mise à jour ou un message d'erreur,
        avec le code de statut HTTP approprié.
    """
    data = request.json
    updated_note = update_note(note_id, data["title"], data["content"])
    if updated_note:
        return jsonify(updated_note), 200
    return jsonify({"message": "Note not found"}), 404


@notes_api.route("/notes/<note_id>", methods=["DELETE"])
@jwt_required
def delete_note_route(note_id):
    """
    Supprime une note spécifique. L'utilisateur doit être authentifié.

    Args:
        note_id (str): L'ID de la note à supprimer.

    Returns:
        JSON: Message de confirmation ou d'erreur,
        avec le code de statut HTTP approprié.
    """
    if delete_note(note_id):
        return jsonify({"message": "Note deleted successfully"}), 200
    return jsonify({"message": "Note not found"}), 404
