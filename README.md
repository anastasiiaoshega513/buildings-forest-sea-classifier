# Buildings, Forest and Sea Classifier

A Flask web application for image classification using a trained CNN model.

The application allows users to upload an image and get a prediction result.
The model classifies images into three scene categories:

* buildings
* forest
* sea

## Project Description

This project is an image classification service. The model was trained in Google Colab using TensorFlow and Keras, then downloaded locally and connected to a Flask web application.

The web app contains a simple upload page where users can select an image. After uploading, the application preprocesses the image, sends it to the trained model and displays the predicted class with a confidence score.

The classification logic is separated from the frontend part:

* `app.py` handles Flask routes and file uploads
* `classifier.py` contains image preprocessing and model prediction logic
* `templates/` contains HTML pages
* `static/` contains styles and uploaded images

## Dataset

Dataset used for this project:

[Intel Image Classification Dataset](https://www.kaggle.com/datasets/puneet6060/intel-image-classification)

The original dataset contains 6 classes:

* buildings
* forest
* glacier
* mountain
* sea
* street

For this project, 3 visually different classes were selected:

* buildings
* forest
* sea

This makes the classification task clearer because the selected classes are easier to distinguish visually.

## Model Training

The model was trained in Google Colab.

Google Colab notebook:

[Open Colab Notebook](https://colab.research.google.com/drive/1IHZtiTek3RbUzEwtbVS3gawACs_Mrm6U?usp=sharing)

The CNN model was trained on preprocessed images resized to 150x150 pixels.

The final model reached a best validation accuracy of about 97.6%.

## Technologies Used

* Python
* Flask
* TensorFlow / Keras
* NumPy
* Pillow
* HTML
* CSS

## Project Structure

```text
buildings-forest-sea-classifier/
│
├── app.py
├── classifier.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── model/
│   └── scene_classifier.keras
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    ├── css/
    │   └── style.css
    └── uploads/
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/anastasiiaoshega513/buildings-forest-sea-classifier.git
cd buildings-forest-sea-classifier
```

### 2. Create a virtual environment

For macOS / Linux:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

For Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python app.py
```

### 5. Open the app in browser

```text
http://127.0.0.1:5000
```

## How the Application Works

1. The user opens the main page.
2. The user uploads an image.
3. Flask saves the uploaded image into the `static/uploads/` folder.
4. The image is loaded and resized to 150x150 pixels.
5. The trained CNN model predicts the image class.
6. The result page displays the uploaded image, predicted class and confidence score.

## Example Predictions

### Upload Page

![Upload Page](screenshots/upload-page.png)

### Prediction Result

![Prediction Result](screenshots/result-page.png)

## Classes

The model can predict one of three scene classes:

- **buildings** — city or architecture scene
- **forest** — forest or green natural scene
- **sea** — sea, ocean or coast scene

## Model File

The trained model file is stored in the `model/` folder:

```text
model/scene_classifier.keras
```