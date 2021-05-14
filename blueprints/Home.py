from flask import Flask,render_template,request,Blueprint
import json
index = Blueprint('index', __name__)
@index.route("/")
def home():
    data = json.load(open('cat.json'))
    return render_template("index.html",data = data)


