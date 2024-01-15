
## Uniform_Segmentation_Classification

### `app.py`

Flask web application serving as an API for image classification.
API endpoint: `/predict`

### `best_model.h5`

Trained TensorFlow Keras model for image classification.

### `Classification_testing.ipynb`

Jupyter Notebook for testing the trained model.
Includes code for model evaluation.

### `DockerFile`

Docker configuration file for building a containerized environment.
Build Docker image: `docker build -t your_project_image .`

### `Documentation.docx`

Microsoft Word document with detailed project documentation.

### `Image_helper.ipynb`

Jupyter Notebook with helper functions for image visualization.
Includes code to interact with the Flask API.

### `requirement.txt`

List of Python dependencies.
Install dependencies: `pip install -r requirement.txt`

### `training_logs.docx` and `training_logs.txt`

Logs and details about the model training process.

### `train_model.py`

Script for training the image classification model.

## Getting Started

1. Build Docker image: `docker build -t your_project_image .`
2. Launch the endpoint

For Docker and Kubernets refer the Repo : https://github.com/Pulkit0602/Classification_Model_Deployment 

## Usage

- Use the `/predict` endpoint of the API for image classification.
- Refer to `Classification_testing.ipynb` for testing and evaluating the model.
- Explore `Image_helper.ipynb` for helper functions and interacting with the API.

## Additional Information

For more detailed information, refer to `Documentation.docx`.


