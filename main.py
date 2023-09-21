import os
from flask import Flask, request, jsonify
import requests
import validators

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    url = request.json['url']
    format = request.json['format']
    folder = request.json['folder']
    
    if not validators.url(url):
        return jsonify({'message': 'L\'URL fournie n\'est pas un lien vidéo valide.'})
    
    response = requests.get(url)
    
    # Obtenez le répertoire de stockage externe sur Android
    external_storage_dir = '/storage/emulated/0/VotreApplication'
    
    # Créez un répertoire spécifique pour votre application
    os.makedirs(external_storage_dir, exist_ok=True)
    
    # Enregistrez la vidéo téléchargée dans le répertoire spécifique
    with open(os.path.join(external_storage_dir, f'video.{format}'), 'wb') as file:
        file.write(response.content)
    
    return jsonify({'message': 'Vidéo téléchargée avec succès !'})

# Le reste du code...

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv("PORT", default=5000))
