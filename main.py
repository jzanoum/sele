from flask import Flask, request, jsonify
import validators

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    url = request.json['url']
    format = request.json['format']
    folder = request.json['folder']
    
    if not is_valid_video_url(url):
        return jsonify({'message': 'L\'URL fournie n\'est pas un lien vidéo valide.'})
    
    response = requests.get(url)
    with open(f'{folder}/video.{format}', 'wb') as file:
        file.write(response.content)
    
    return jsonify({'message': 'Vidéo téléchargée avec succès !'})

def is_valid_video_url(url):
    return validators.url(url) and any(ext in url for ext in ['.mp4', '.avi', '.mov', '.wmv'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv("PORT", default=5000))
