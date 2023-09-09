# Utiliser une image de base Python 3.9
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY . .

# Installer les bibliothèques Python à partir du fichier requirements.txt
RUN pip install -r requirements.txt

# Exposer le port 5000 du conteneur
EXPOSE 5000

# Définir la variable d'environnement FLASK_APP
ENV FLASK_APP=main.py

# Lancer l'application Flask avec la commande 
CMD ["flask", "run", "--host=0.0.0.0"]
