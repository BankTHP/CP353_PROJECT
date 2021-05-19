from flask import Flask,render_template,request
from werkzeug import datastructures
from flask_cors import CORS
from flask_jwt_extended.jwt_manager import JWTManager
from flask_restful import Api
from PIL import Image
import base64
from api.ml import TFModel
import os,json,requests
from flask_sqlalchemy import SQLAlchemy
from api.routes import create_route
from flask_swagger_ui import get_swaggerui_blueprint
import base64
import argparse
from werkzeug.middleware.proxy_fix import ProxyFix
config = {
    'JSON_SORT_KEYS': False,
    'JWT_SECRET_KEY': 'BaNPFol%Dgfgge',
    'JWT_ACCESS_TOKEN_EXPIRES': 300,
    'JWT_REFRESH_TOKEN_EXPIRES': 604800
}

#init app
app = Flask(__name__)


config = {
    'JSON_SORT_KEYS': False,
    'JWT_SECRET_KEY': 'BaNPFol%Dgfgge',
    'JWT_ACCESS_TOKEN_EXPIRES': 300,
    'JWT_REFRESH_TOKEN_EXPIRES': 604800
}

#init app
app = Flask(__name__)

CORS(app, origins="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"
], supports_credentials=True)


app.config.update(config)

api = Api(app)
create_route(api=api)
UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = TFModel(model_dir='./ml-model/')
model.load()
# swagger specific
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
SWAGGER_UI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Python Flask RESTful API"
    }
)
app.register_blueprint(SWAGGER_UI_BLUEPRINT, url_prefix=SWAGGER_URL)

# init JWT
jwt = JWTManager(app=app)

CORS(app, origins="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"
], supports_credentials=True)


@app.route("/")
def home():
    myurl = 'http://127.0.0.1:5000/cat'
    data = requests.get(myurl).json()
    return render_template('index.html',data = data)


app.wsgi_app = ProxyFix(app.wsgi_app)

model = TFModel(model_dir='./ml-model/')
model.load()

parser = argparse.ArgumentParser(description="Predict a label for an image.")
parser.add_argument("image", help="Path to your image file.")
args = parser.parse_args()

@app.route('/catscan', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return render_template("upload.html")
        file1 = request.files['file1']
        base64_encoded_data = base64.b64encode(file1.read())
        base64_message = base64_encoded_data.decode('utf-8')
        url = 'http://127.0.0.1:5000/machine'
        body = {'base64': base64_message}
        prediction = requests.post(url, json = body).json()
        myurl = 'http://127.0.0.1:5000/cat'
        data = requests.get(myurl).json()
        cats = []
        for i in data:
            if prediction['predictions'][0]['label'].lower() in i['Name'].lower()  :
                cats.append(i)
        return render_template("prediction.html",pred_result = prediction,cats = cats)

    return render_template("upload.html")

def readJson():
    open_json_file = open('cat.json', 'r') 
    read_json_file = open_json_file.read()
    cat_data = json.loads(read_json_file)
    return cat_data