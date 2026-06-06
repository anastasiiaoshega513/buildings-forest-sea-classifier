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


@app.route("/predict", methods=["POST"])
def predict():
    image = request.files.get("image")

    if image is None or image.filename == "":
        return redirect(url_for("index"))

    file_extension = Path(image.filename).suffix.lower()
    filename = f"{uuid4()}.{file_extension}"
    image_path = UPLOAD_FOLDER / filename

    image.save(image_path)

    label, probability = classify(model, str(image_path))

    return render_template(
        "result.html",
        label=label,
        probability=round(probability * 100, 2),
        image_path=f"uploads/{filename}"
    )


if __name__ == "__main__":
    app.run(debug=True)
