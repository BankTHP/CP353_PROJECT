from flask import Flask, request, jsonify,render_template,Blueprint
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
import json
from flask_basicauth import BasicAuth
import os
import io
import base64
import argparse
from PIL import Image
from api.ml import TFModel
import requests

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

model = TFModel(model_dir='./ml-model/')
model.load()

api = Api(app,)

class MLware(Resource):
    def post(self):
        print("test")
        img_string = api.payload['base64']
        imgdata = base64.b64decode(img_string)
        image_temp = Image.open(io.BytesIO(imgdata))
        outputs = model.predict(image_temp)
        return jsonify(outputs)

