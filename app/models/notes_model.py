"""Ce module contient le modèle de données pour les notes."""

from bson import ObjectId
from .. import mongo


class Note:
    """
    Représente une note dans l'application.

    Attributs:
        title (str): Le titre de la note.
        content (str): Le contenu de la note.
        user_id (ObjectId): L'identifiant de l'utilisateur qui a créé la note.
    """

    def __init__(self, title, content, user_id):
        """
        Initialise une nouvelle instance de la classe Note.

        Args:
            title (str): Le titre de la note.
            content (str): Le contenu de la note.
            user_id (str): L'identifiant de l'utilisateur.
        """
        self.title = title
        self.content = content
        self.user_id = ObjectId(user_id)

    def save(self):
        """
        Enregistre la note dans la base de données.

        Returns:
            ObjectId: L'identifiant unique de la note enregistrée.
        """
        note_data = {
            "title": self.title,
            "content": self.content,
            "user_id": self.user_id,
        }
        return mongo.db.notes.insert_one(note_data).inserted_id

    @staticmethod
    def find_by_user(user_id):
        """
        Recherche les notes créées par un utilisateur spécifique.

        Args:
            user_id (str): L'identifiant de l'utilisateur.

        Returns:
            list: Liste des notes trouvées.
        """
        return list(mongo.db.notes.find({"user_id": ObjectId(user_id)}))

    @staticmethod
    def get_all_notes():
        """
        Récupère toutes les notes de la base de données.

        Returns:
            list[Note]: Liste de toutes les notes.
        """
        return list(mongo.db.notes.find({}))

    @staticmethod
    def find_by_id(note_id):
        """
        Trouve une note par son identifiant.

        Args:
            note_id (str): L'identifiant de la note.

        Returns:
            Note | None: La note trouvée ou None si non trouvée.
        """
        return mongo.db.notes.find_one({"_id": ObjectId(note_id)})

    @staticmethod
    def update(note_id, note_data):
        """
        Met à jour une note existante.

        Args:
            note_id (str): L'identifiant de la note à mettre à jour.
            note_data (dict): Les données mises à jour de la note.

        Returns:
            bool: True si la mise à jour a réussi, False sinon.
        """
        result = mongo.db.notes.update_one(
            {"_id": ObjectId(note_id)}, {"$set": note_data}
        )
        return result.matched_count > 0

    @staticmethod
    def delete(note_id):
        """
        Supprime une note de la base de données.

        Args:
            note_id (str): L'identifiant de la note à supprimer.

        Returns:
            bool: True si la suppression a réussi, False sinon.
        """
        result = mongo.db.notes.delete_one({"_id": ObjectId(note_id)})
        return result.deleted_count > 0
