"""
Ce module fournit des services autour de la gestion des notes,
comme la création, la récupération, la mise à jour et la suppression des notes.
"""
from app.models.notes_model import Note


def create_note(title, content, user_id):
    """
    Crée une nouvelle note et l'enregistre dans la base de données.

    Args:
        title (str): Le titre de la note.
        content (str): Le contenu de la note.
        user_id (str): L'identifiant de l'utilisateur qui crée la note.

    Returns:
        Note: L'instance de la note créée.
    """
    new_note = Note(title, content, user_id)
    new_note.save()
    return new_note


def get_all_notes():
    """
    Récupère toutes les notes enregistrées dans la base de données.

    Returns:
        list[Note]: Une liste des instances de notes.
    """
    return Note.get_all_notes()


def get_note_by_id(note_id):
    """
    Récupère une note spécifique par son identifiant.

    Args:
        note_id (str): L'identifiant de la note.

    Returns:
        Note | None: L'instance de la note si trouvée, sinon None.
    """
    return Note.find_by_id(note_id)


def update_note(note_id, title, content):
    """
    Met à jour le titre et le contenu d'une note spécifiée par son identifiant.

    Args:
        note_id (str): L'identifiant de la note à mettre à jour.
        title (str): Le nouveau titre de la note.
        content (str): Le nouveau contenu de la note.

    Returns:
        Note | None: L'instance de la note mise à jour, sinon None .
    """
    note = Note.find_by_id(note_id)
    if note:
        note["title"] = title
        note["content"] = content
        Note.update(note_id, note)
    return note


def delete_note(note_id):
    """
    Supprime une note spécifiée par son identifiant.

    Args:
        note_id (str): L'identifiant de la note à supprimer.

    Returns:
        bool: True si la suppression a réussi, False sinon.
    """
    return Note.delete(note_id)
