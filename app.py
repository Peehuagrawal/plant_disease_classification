from flask import Flask, render_template, request
from utils import predict_disease
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            label, confidence = predict_disease(file_path)
            return render_template("index.html", prediction=label, confidence=confidence, image_path=file_path)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
