# Importer les bibliothèques
import os # Importer os pour accéder aux variables d'environnement
import json
import requests # Importer requests pour faire des requêtes HTTP
from selenium import webdriver # Importer webdriver pour contrôler le navigateur
from flask import Flask, request
# Créer une instance de l'application flask
app = Flask(__name__)

# Définir une route pour le point de terminaison
@app.route('/video', methods=['POST'])
def video():
    # Obtenir le contenu du fichier json en utilisant request.get_json()
    data = request.get_json()
    # Appeler la fonction qui traite le fichier json et renvoie le nom du fichier de sortie
    output_file = process_json(data)
    # Retourner le nom du fichier de sortie comme réponse
    return output_file

# Définir une fonction qui prend en entrée le contenu du fichier json et renvoie le nom du fichier de sortie
def process_json(data):
    # Extraire les informations du fichier json
    url = data['url']
    format = data['format']
    folder = data['folder']

    # Utiliser selenium pour accéder à l'url de la vidéo
    options = webdriver.ChromeOptions() # Créer un objet options pour configurer le navigateur
    options.add_argument('headless') # Ajouter l'argument headless pour ne pas afficher le navigateur
   driver = webdriver.Chrome(options=options)
 # Créer un objet driver avec le chemin du chromedriver et les options
    driver.get(url) # Accéder à l'url avec le driver

    # Utiliser requests pour obtenir le contenu binaire de la vidéo
    video_url = driver.find_element_by_tag_name('video').get_attribute('src') # Trouver l'élément vidéo dans la page et obtenir son attribut src qui contient l'url de la vidéo
    video_data = requests.get(video_url).content # Faire une requête GET à l'url de la vidéo et obtenir son contenu binaire

    # Utiliser selenium pour obtenir le titre de la vidéo
    video_title = driver.title

    # Créer le nom du fichier de sortie
    output_file = folder + '/' + video_title + '.' + format

    # Ouvrir le fichier de sortie en mode binaire
    with open(output_file, 'wb') as f:
        # Écrire les données de la vidéo dans le fichier
        f.write(video_data)

    # Retourner le nom du fichier de sortie
    return output_file

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv("PORT", default=5000))
