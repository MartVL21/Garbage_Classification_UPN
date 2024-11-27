from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications import xception
import numpy as np
import os

# Inicializa la aplicación Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Cargar el modelo
model = load_model('model.h5', custom_objects={'xception': xception})

# Configura el tamaño de imagen y categorías
IMAGE_SIZE = (320, 320)
gen_label_map = {0: 'battery', 1: 'biological', 2: 'brown-glass', 3: 'cardboard', 
                 4: 'clothes', 5: 'green-glass', 6: 'metal', 7: 'paper', 
                 8: 'plastic', 9: 'shoes', 10: 'trash', 11: 'white-glass'}

def classify_image(img_path):
    img = load_img(img_path, target_size=IMAGE_SIZE)
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    pred_class = np.argmax(pred, axis=1)
    return gen_label_map[pred_class[0]]

@app.route("/", methods=["GET", "POST"])
def upload_and_classify():
    if request.method == "POST":
        # Guarda la imagen cargada
        img = request.files["image"]
        img_path = os.path.join(app.config["UPLOAD_FOLDER"], img.filename)
        img.save(img_path)

        # Clasifica la imagen
        result = classify_image(img_path)

        return render_template("index.html", result=result, img_path=img_path)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
