import flask
import numpy as np
import json
from PIL import Image, ImageOps
from tensorflow import keras
import base64
import io
from flask import request

app = flask.Flask(__name__)
model = None

def load_model():
    global model

@app.route("/", methods=["POST"])
def redirect():
    b64_img = request.form["img"]
    model = keras.models.load_model("./quickdraw_100.h5")
    img = base64.b64decode(b64_img)
    im = Image.open(io.BytesIO(img))
    im = im.resize((28, 28))
    im = im.convert("L")
    im = ImageOps.invert(im)
    data = np.asarray(im)
    X = []
    X.append(data)
    X = np.array(X)
    X = X.reshape((1, 28, 28, 1))
    result = np.array(model.predict([X])[0])
    resultIndex = np.where(result == 1)[0][0]
    f = open("./class_names_100.txt")
    answers = f.read().split("\n")
    answer = answers[resultIndex]
    response = {}
    response["answer"] = answer
    return json.dumps(response)

if __name__ == "__main__":
    load_model()
    app.run()