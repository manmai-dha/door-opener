from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import base64
from face_recog import *
from firebase-demo import *


#some CONST
UPLOAD_FOLDER = 'uploads'
DATA_PATH = "faceData.json"

#init and config
app = Flask(__name__)
app.secret_key = "12345"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", public_url=public_url)

@app.route('/face-recog', methods=['POST'])
def faceRecog():
    # check if the post request has the file part
    file = request.files['file']
    filename = secure_filename(file.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path)
    res = findFace(path, DATA_PATH)
    firebaseSend(path)
    os.remove(path)
    return jsonify(success=True, result=res)

@app.route('/register-face', methods=['POST'])
def registerFace():
    # check if the post request has the file part
    file = request.files['file']
    filename = secure_filename(file.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path)
    res = addFace(path, request.form["name"], DATA_PATH)
    os.remove(path)
    return jsonify(result=res)

@app.route('/delete-face', methods=['DELETE'])
def removeFace():
    # check if the post request has the file part
    res = deleteFace(request.form["name"], DATA_PATH)
    return jsonify(result=res)


app.run(host='0.0.0.0', port=80)