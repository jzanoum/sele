# Importer les bibliothèques
import json
from requestium import Session
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

    # Utiliser requestium pour accéder à l'url de la vidéo
    s = Session(webdriver_path='chromedriver',
                browser='chrome',
                default_timeout=15,
                webdriver_options={'arguments': ['headless']})
    s.get(url)

    # Utiliser requestium pour obtenir le contenu binaire de la vidéo
    video_data = s.driver.get_screenshot_as_png()

    # Utiliser requestium pour obtenir le titre de la vidéo
    video_title = s.driver.title

    # Créer le nom du fichier de sortie
    output_file = folder + '/' + video_title + '.' + format

    # Ouvrir le fichier de sortie en mode binaire
    with open(output_file, 'wb') as f:
        # Écrire les données de la vidéo dans le fichier
        f.write(video_data)

    # Retourner le nom du fichier de sortie
    return output_file


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
