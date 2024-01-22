# BlogNotes

Bienvenue sur BlogNotes, une application web Flask dynamique pour la gestion de notes personnelles. Avec une interface intuitive, les utilisateurs peuvent facilement créer, lire, mettre à jour et supprimer des notes, tout en bénéficiant d'une authentification sécurisée et d'une base de données robuste MongoDB.

## Caractéristiques

- **Création de notes :** Les utilisateurs peuvent ajouter de nouvelles notes avec des titres et du contenu personnalisés.
- **Affichage des notes :** Visualisez toutes vos notes en un coup d'œil.
- **Mise à jour et suppression :** Modifiez facilement le contenu de vos notes ou supprimez-les si nécessaire.
- **Authentification des utilisateurs :** Inscription et connexion sécurisées pour une expérience utilisateur personnalisée.
- **Stockage persistant :** Toutes les notes sont stockées dans MongoDB, garantissant la sécurité et la pérennité de vos données.

## Prérequis

- Python 3.8 ou version ultérieure
- Docker et Docker Compose (pour le déploiement avec conteneurs)

## Installation

Clonez le dépôt et installez les dépendances :

```bash
git clone [URL de votre dépôt]
cd BlogNotes
pip install -r requirements.txt
```

## Configuration

Configurez les variables d'environnement suivantes :

- `SECRET_KEY` : une clé secrète pour l'application Flask.
- `MONGO_URI` : URI de connexion à votre base de données MongoDB.
- `JWT_SECRET_KEY` : une clé secrète pour JWT.

Ces variables peuvent être placées dans un fichier `.env` à la racine du projet.

## Démarrage avec Docker

Exécutez l'application en utilisant Docker Compose :

```bash
docker-compose up --build
```

L'application sera accessible à `http://localhost:5000`.

## Exécution sans Docker

Si vous préférez exécuter l'application sans Docker :

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

Veillez à ce que MongoDB soit en fonctionnement sur votre machine.

## Contribution

Les contributions à BlogNotes sont toujours les bienvenues. N'hésitez pas à soumettre des pull requests ou à signaler des problèmes.