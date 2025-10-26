from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.FaceClassification.pipeline.predict import PredictionPipeline 

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods = ['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods = ['GET', 'POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"

@app.route("/predict", methods = ['POST'])
@cross_origin()
def predictRoute():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400
    file.save(clApp.filename)
    try:
        result = clApp.classifier.predict()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


clApp = ClientApp()
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=8080)