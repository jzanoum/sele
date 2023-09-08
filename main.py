
import json from selenium import webdriver from selenium.webdriver.chrome.options import Options import requests from flask import Flask, request

app = Flask(name)

@app.route(‘/video’, methods=[‘POST’]) def video(): # Obtenir le contenu du fichier json en utilisant request.get_json() data = request.get_json() # Appeler la fonction qui traite le fichier json et renvoie le nom du fichier de sortie output_file = process_json(data) # Retourner le nom du fichier de sortie comme réponse return output_file

Définir une fonction qui prend en entrée le contenu du fichier json et renvoie le nom du fichier de sortie
def process_json(data): # Extraire les informations du fichier json url = data[‘url’] format = data[‘format’] folder = data[‘folder’]

# Créer les options pour le navigateur chrome en mode headless
options = Options()
options.add_argument('--headless')

# Utiliser selenium pour accéder à l'url de la vidéo avec un navigateur chrome en mode headless
driver = webdriver.Chrome(options=options)
driver.get(url)

# Utiliser selenium pour obtenir le titre de la vidéo
video_title = driver.title

# Utiliser requests pour obtenir le contenu binaire de la vidéo en utilisant l'url du tag video
video_data = requests.get(driver.find_element_by_tag_name('video').get_attribute('src')).content

# Fermer le navigateur
driver.quit()

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
