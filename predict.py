import os
from flask import Flask, request, render_template, jsonify,Blueprint,current_app
from PIL import Image
import base64
from ml import TFModel

UPLOAD_FOLDER = './static/uploads'

predictml = Flask(__name__)
predictml.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = TFModel(model_dir='./ml-model/')
model.load()

@predictml.route('/catscan', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'there is no file in form!'
        file = request.files['file']
        path = os.path.join(predictml.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)

        imagecat = Image.open(path)
        outputs = model.predict(imagecat)
        imagename = imagecat.filename
        return render_template('prediction.html', pred_result=outputs,pic = imagename)

    return render_template('upload.html')

