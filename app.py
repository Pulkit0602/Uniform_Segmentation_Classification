from flask import Flask, request, jsonify
import cv2
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras import applications
from pixellib.torchbackend.instance import instanceSegmentation
import os

app = Flask(__name__)

# Set the paths within the Docker container
model_path = "/app/best_model.h5"  # Update with the correct path
segmentation_model_path = "/app/pointrend_resnet50.pkl"  # Update with the correct path

ins = instanceSegmentation()
ins.load_model(segmentation_model_path)

def get_person_reduced_mask(results, threshold=80):
    transposed_mask = np.transpose(results["masks"], (2, 0, 1))
    req_transposed_mask = [
        mask for mask, class_id, score in zip(transposed_mask, results["class_ids"], results["scores"])
        if class_id == 0 and score > threshold
    ]
    binary_mask = np.logical_or.reduce(req_transposed_mask, axis=0)
    return binary_mask

def remove_background(image_path, threshold=80):
    image = cv2.imread(image_path)
    results, _ = ins.segmentImage(image_path, show_bboxes=True)
    binary_mask = get_person_reduced_mask(results, threshold)
    binary_mask = np.uint8(binary_mask)
    expanded_mask = np.expand_dims(binary_mask, axis=-1)
    result = image * expanded_mask
    return result

def preprocess_image(image_path, model_input_size=(224, 224)):
    image_no_bg = remove_background(image_path)
    image_preprocessed = cv2.resize(image_no_bg, (224, 224))
    image_preprocessed = applications.mobilenet_v2.preprocess_input(image_preprocessed)
    return image_preprocessed

def predict_class(image_path):
    preprocessed_image = preprocess_image(image_path)
    model = load_model(model_path)
    prediction = model.predict(np.expand_dims(preprocessed_image, axis=0))
    class_labels = ['CRPF', 'BSF', 'J_K', 'Random']
    predicted_class = class_labels[np.argmax(prediction)]
    return predicted_class

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file:
        image_path = "/app/uploaded_image.jpg"  # Update with the correct path within the container
        file.save(image_path)
        predicted_class = predict_class(image_path)
        return jsonify({'predicted_class': predicted_class})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
