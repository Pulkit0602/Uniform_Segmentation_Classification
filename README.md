# Uniform_Segmentation_Classification

## Project Description

## Dataset and Additional Resources

- [Google Drive Link](https://drive.google.com/drive/folders/1HfK11VXf9JGjIigUYfZip74h1ZszWgmL?usp=sharing): Contains the processed dataset images, background-removed images, saved models, and other project resources.

This project involves the development of an image classification system for uniforms of armed personnel. 
- **`Objective`:**
  - Classify uniforms of armed personnel into distinct categories.
 
- **`Methodology`:**
  - Utilizes Pixellib for instance segmentation to remove background from images.
  -Implements a Convolutional Neural Network (CNN) based on MobileNetV2 for classification.
  -Categories include CRPF, BSF, J&K Police, and a "Random" category.

- **`Steps`:**
  -Load dataset and preprocess images by removing background and resizing..
  -Train the CNN model with data augmentation, including brightness adjustments.
  -Save the best-performing model based on validation accuracy.

- **`Conclusion`:**
  - Achieves a test accuracy of 88%, indicating successful classification of armed personnel uniforms.

The key components of the project are as follows:

## Project Files

- **`app.py`:**
  - Flask web application serving as an API for image classification.
  - API endpoint: `/predict`

- **`best_model.h5`:**
  - Trained TensorFlow Keras model for image classification.

- **`Classification_testing.ipynb`:**
  - Jupyter Notebook for testing the trained model.
  - Includes code for model evaluation.

- **`DockerFile`:**
  - Docker configuration file for building a containerized environment.
  - Build Docker image: `docker build -t your_project_image .`

- **`Documentation.docx`:**
  - Microsoft Word document with detailed project documentation.

- **`Image_helper.ipynb`:**
  - Jupyter Notebook with helper functions for image visualization.
  - Includes code to interact with the Flask API.

- **`requirement.txt`:**
  - List of Python dependencies.
  - Install dependencies: `pip install -r requirement.txt`

- **`training_logs.docx` and `training_logs.txt`:**
  - Logs and details about the model training process.

- **`train_model.py`:**
  - Script for training the image classification model.


## Getting Started

1. Build Docker image: `docker build -t your_project_image .`
2. Launch the endpoint

**For Docker and Kubernetes, refer to the [GitHub Repository](https://github.com/Pulkit0602/Classification_Model_Deployment).**

## Usage

- Use the `/predict` endpoint of the API for image classification.
- Refer to `Classification_testing.ipynb` for testing and evaluating the model.
- Explore `Image_helper.ipynb` for helper functions and interacting with the API.

## Additional Information

- For more detailed information, refer to `Documentation.docx`.
