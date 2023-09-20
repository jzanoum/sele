# Utilisez une image Python officielle en tant qu'image parent
FROM python:3.9-slim

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installez les dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le reste du code dans le conteneur
COPY . .

# Exposez le port 5000 pour accéder à l'application Flask
EXPOSE 5000

# Définissez la variable d'environnement FLASK_APP sur le nom du fichier principal de votre application Flask
ENV FLASK_APP=main.py

# Exécutez l'application Flask lorsque le conteneur démarre
CMD ["flask", "run", "--host=0.0.0.0"]
