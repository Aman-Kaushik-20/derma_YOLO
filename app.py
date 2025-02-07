import cv2
import base64
from flask import Flask, request, jsonify
from ultralytics import YOLO
import numpy as np

app = Flask(__name__)
model = YOLO("200_epochs_last.pt")

def encode_image_to_base64(image):
    _, buffer = cv2.imencode('.jpg', image)
    encoded_image = base64.b64encode(buffer).decode('utf-8')
    return f"data:image/jpeg;base64,{encoded_image}"

@app.route('/', methods=["GET"])
def home():
    return " Welcome to YOLO DERMA"

@app.route('/detect', methods=['POST'])
def detect_objects():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image_file = request.files['image']
    image_array = np.frombuffer(image_file.read(), np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # Run YOLO model
    results = model.predict(image, max_det=1)

    # Annotated image with bounding boxes
    annotated_image = results[0].plot()
    
    # Encode the annotated image to Base64
    base64_image = encode_image_to_base64(annotated_image)

    # Extract detection details
    detections = results[0].boxes.xyxy.cpu().numpy()
    class_ids = results[0].boxes.cls.cpu().numpy().astype(int)
    confidences = results[0].boxes.conf.cpu().numpy()
    class_names = [model.names[class_id] for class_id in class_ids]

    response_data = {
        'bounding_boxes': detections.tolist(),
        'class_names': class_names,
        'confidence_scores': confidences.tolist(),
        'annotated_image': base64_image
    }

    return jsonify(response_data)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)
