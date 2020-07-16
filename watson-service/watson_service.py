import json
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import sys
import os
from PIL import Image
from visual_recognition import classify_image

app = Flask(__name__)
CORS(app)

@app.route('/visual/recognizer', methods=['POST'])
def process_image():
    url = request.json['image_url']
    response = Response(json.dumps(classify_image(url)), status=200, mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = True
    return response

if __name__ == "__main__":
  port = int(os.getenv("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
