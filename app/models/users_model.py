"""Ce module contient le modèle de données pour les utilisateurs."""

from .. import mongo, bcrypt


class User:
    """
    Représente un utilisateur dans l'application.

    Attributs:
        username (str): Le nom d'utilisateur unique.
        password (str): Le mot de passe hashé de l'utilisateur.
    """

    def __init__(self, username, password):
        """
        Initialise une nouvelle instance de la classe User.

        Args:
            username (str): Le nom d'utilisateur.
            password (str): Le mot de passe en clair.
        """
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def save(self):
        """
        Enregistre l'utilisateur dans la base de données.

        Returns:
            ObjectId: L'identifiant unique de l'utilisateur enregistré.
        """
        user_data = {"username": self.username, "password": self.password}
        return mongo.db.users.insert_one(user_data).inserted_id

    @staticmethod
    def find_by_username(username):
        """
        Recherche un utilisateur par son nom d'utilisateur.

        Args:
            username (str): Le nom d'utilisateur à rechercher.

        Returns:
            Un dictionnaire représentant l'utilisateur ou None si non trouvé.
        """
        # ...

    @staticmethod
    def validate_login(username, password):
        """
        Valide les identifiants de connexion de l'utilisateur.

        Args:
            username (str): Le nom d'utilisateur.
            password (str): Le mot de passe.

        Returns:
            Un dictionnaire représentant l'utilisateur valide, sinon None.
        """
        user = User.find_by_username(username)
        if user and bcrypt.check_password_hash(user["password"], password):
            return user
        return None
