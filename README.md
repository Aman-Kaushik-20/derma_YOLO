# YOLO Derma: Skin Disease Detection using YOLOv8 Segmentation

## 🚀 Overview

YOLO Derma is a Flask-based web application that uses YOLOv8 segmentation to detect and segment 25 different skin diseases from images. Leveraging the power of the Ultralytics YOLOv8 model, this project provides:

- Accurate segmentation of affected skin regions.
- Confidence scores for detected diseases.
- Visualizations with annotated images.

## 🏗️ Project Structure

```
├── app.py                 # Flask application script
├── 200_epochs_last.pt     # YOLOv8 trained model (25 skin diseases)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## ⚡ Features

- 🔍 **Detection & Segmentation**: Identifies and segments skin diseases using YOLOv8.
- 📷 **Image Upload Endpoint**: Accepts image uploads via a RESTful API.
- 🖼️ **Annotated Output**: Returns annotated images with segmented disease regions.
- 📊 **Confidence Scores**: Provides prediction confidence for each detected disease.

## 🔧 Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/yourusername/yolo-derma.git
cd yolo-derma
```

2. **Create a Virtual Environment (Optional but Recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

4. **Download YOLOv8 Model:**

Ensure `200_epochs_last.pt` is in the root directory. This file is the trained YOLOv8 segmentation model for detecting 25 skin diseases.

## 🚀 Running the Application

```bash
python app.py
```

The application will run on:

```
http://0.0.0.0:5000/
```

## 🌐 API Endpoints

### 1. **GET /**
- **Description:** Welcome route.
- **Response:**
  ```json
  "Welcome to YOLO DERMA"
  ```

### 2. **POST /detect**
- **Description:** Detects skin diseases from the uploaded image.
- **Request:**
  - Content-Type: `multipart/form-data`
  - Parameter: `image` (JPEG/PNG file)

- **Response:**
  ```json
  {
    "bounding_boxes": [[x1, y1, x2, y2]],
    "class_names": ["disease_name"],
    "confidence_scores": [0.95],
    "annotated_image": "data:image/jpeg;base64,..."
  }
  ```

## 🛠️ Key Components

- **Flask**: Web framework for creating RESTful API endpoints.
- **YOLOv8 (Ultralytics)**: Segmentation model for skin disease detection.
- **OpenCV (cv2)**: Image preprocessing and encoding.
- **NumPy**: Efficient image array manipulation.
- **Base64**: Encodes annotated images for easy transmission in JSON.

## 📜 How It Works

1. The user uploads an image to the `/detect` endpoint.
2. YOLOv8 model performs segmentation, detecting the disease regions.
3. The annotated image, along with bounding box coordinates, class names, and confidence scores, is returned as a JSON response.

## 🎯 Model Details

- **Model**: YOLOv8 Segmentation
- **Training**: 200 epochs on a custom dataset containing 25 skin diseases.
- **Output**: Segmented images with labeled skin conditions and prediction confidence.

## ⚡ Sample cURL Request

```bash
curl -X POST http://0.0.0.0:5000/detect \
  -F image=@/path/to/your/image.jpg
```

## 💡 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 🙌 Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)

---

🌟 *Happy Detecting with YOLO Derma!* 🌟

