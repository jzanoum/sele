# Utilisez l'image Python 3.7-slim comme image de base
FROM python:3.7-slim

# Définissez le répertoire de travail sur /app
WORKDIR /app

# Copiez le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installez les dépendances à partir du fichier requirements.txt
RUN pip install -r requirements.txt

# Copiez tout le contenu du répertoire actuel dans le répertoire de travail
COPY . .

# Exposez le port 5000 pour que l'application puisse être accessible depuis l'extérieur du conteneur
EXPOSE 5000

# Définissez la commande par défaut pour exécuter l'application Flask
CMD ["python", "main.py"]
