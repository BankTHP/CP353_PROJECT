from flask import Flask,render_template,request
from werkzeug import datastructures
from flask_cors import CORS
from flask_jwt_extended.jwt_manager import JWTManager
from flask_restful import Api
from PIL import Image
import base64
from ml import TFModel
import os,json,requests
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = TFModel(model_dir='./ml-model/')
model.load()


api = Api(app)


@app.route("/")
def home():
    data = readJson() 
    return render_template("index.html",data = data)


@app.route('/catscan', methods=['GET', 'POST'])
def upload_file():
    data = readJson()
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'there is no file in form!'
        file = request.files['file']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)

        imagecat = Image.open(path)
        outputs = model.predict(imagecat)
        imagename = imagecat.filename
        cats = []
        name = outputs['predictions'][0]['label']
        for i in data:
            if  name == i['Name']:
                cats.append(i)   
        cats.append({
                "Name": "ไม่มีข้อมูล",
                "LifeSpanMin": "ไม่มีข้อมูล",
                "LifeSpanMax": "ไม่มีข้อมูล",
                "Color": "ไม่มีข้อมูล",
                "Coat": "ไม่มีข้อมูล",
                "Energy": "ไม่มีข้อมูล",
                "Shedding": "ไม่มีข้อมูล",
                "Size": "ไม่มีข้อมูล"
        },)
                
        return render_template('prediction.html', pred_result=outputs,pic = imagename,cats = cats)

    return render_template('upload.html')

def readJson():
    open_json_file = open('cat.json', 'r') 
    read_json_file = open_json_file.read()
    cat_data = json.loads(read_json_file)
    return cat_data

