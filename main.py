from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    url = request.json['url']
    format = request.json['format']
    folder = request.json['folder']
    response = requests.get(url)
    with open(f'{folder}/video.{format}', 'wb') as file:
        file.write(response.content)
    return jsonify({'message': 'Video downloaded successfully!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv("PORT", default=5000))
