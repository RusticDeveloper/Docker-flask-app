from flask import Flask,jsonify,render_template,request,Blueprint, Request
import os
import requests
from decouple import config

main = Blueprint('main', __name__)

@main.route('/')
def index():
    image_folder = os.path.join('app', 'static', 'images')
    images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    return render_template('index.html', images=images)

@main.route('/analyze', methods=['POST'])
def analyze_image():
    image_name = request.form.get('image_name')
    image_path = os.path.join('app', 'static', 'images', image_name)
    categories = call_imagga_api(image_path)
    return jsonify({'categories': categories})

def call_imagga_api(image_path):
    api_key = config('API_KEY')
    api_secret = config('API_SECRET')
    api_url = 'https://api.imagga.com/v2/tags'

    with open(image_path, 'rb') as image_file:
        response = requests.post(
            api_url,
            auth=(api_key, api_secret),
            params={'language':'es'},
            files={'image': image_file}
        )

    if response.status_code == 200:
        result = response.json()
        tags = result.get('result', {}).get('tags', [])
        # categories = [tag['tag']['es'] for tag in tags]
        categories=[tags[0],tags[1]]
        return categories
    else:
        return ['Error al analizar la imagen']



