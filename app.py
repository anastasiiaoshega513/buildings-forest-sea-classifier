from pathlib import Path
from uuid import uuid4

import tensorflow as tf
from flask import Flask, render_template, request, redirect, url_for

from classifier import classify


app = Flask(__name__)

UPLOAD_FOLDER = Path("static/uploads")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

MODEL_PATH = "static/model/scene_classifier.keras"
model = tf.keras.models.load_model(MODEL_PATH)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
