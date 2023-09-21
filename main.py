import os
from flask import Flask, request, jsonify, Response
import requests
import validators
import time

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    url = request.json['url']
    format = request.json['format']
    folder = request.json['folder']
    
    if not validators.url(url):
        return jsonify({'message': 'L\'URL fournie n\'est pas un lien vidéo valide.'})
    
    response = requests.get(url, stream=True)
    
    external_storage_dir = '/storage/emulated/0/VotreApplication'
    
    os.makedirs(external_storage_dir, exist_ok=True)
    
    file_path = os.path.join(external_storage_dir, f'video.{format}')
    with open(file_path, 'wb') as file:
        total_size_in_bytes = int(response.headers.get('content-length', 0))
        bytes_downloaded = 0
        start_time = time.time()
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)
            bytes_downloaded += len(chunk)
            percentage_complete = bytes_downloaded / total_size_in_bytes * 100
            remaining_time = (total_size_in_bytes - bytes_downloaded) / (bytes_downloaded / (time.time() - start_time)) if bytes_downloaded > 0 else 0
            response_json = {
                'bytes_downloaded': bytes_downloaded,
                'total_size': total_size_in_bytes,
                'percentage_complete': percentage_complete,
                'remaining_time': remaining_time,
                'file_name': file_path,
                'message': 'Téléchargement en cours...'
            }
            dynamic_json_data = get_dynamic_json()
            response_json.update(dynamic_json_data)
            return jsonify(response_json)

@app.route('/data')
def get_dynamic_json():
    # Votre logique pour générer les données JSON dynamiques ici
    data = {
        'key1': 'valeur1',
        'key2': 'valeur2',
        'key3': 'valeur3'
    }
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv("PORT", default=5000))
