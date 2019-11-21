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
    model = keras.models.load_model("./keras.h5")
    img = base64.b64decode(b64_img)
    im = Image.open(io.BytesIO(img))
    print(im.size)
    im = im.resize((28, 28))
    im = im.convert("L")
    im = ImageOps.invert(im)
    data = np.asarray(im)
    X = []
    X.append(data)
    X = np.array(X)
    X = X.reshape((28, 28, 1))
    result = model.predict([np.expand_dims(X, axis=0)])[0]
    ind = (-result).argsort()[:20]
    f = open("./class_names.txt")
    answers = f.read().split("\n")
    latex = [answers[x] for x in ind]
    answer = answers[resultIndex]
    response = {}
    response["answer"] = answer
    return json.dumps(response)

if __name__ == "__main__":
    load_model()
    app.run()