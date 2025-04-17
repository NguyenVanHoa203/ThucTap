from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import webbrowser

app = Flask(__name__)
# Thư mục lưu ảnh upload
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Mở trang web khi chạy
webbrowser.open("http://127.0.0.1:5000/")
@app.route("/", methods=["GET", "POST"])
def home():
    image_url = None

    if request.method == "POST":
        if "image" in request.files:
            file = request.files["image"]
            if file.filename != "":
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                image_url = f"/{filepath}"

    return render_template("index.html", image_url=image_url)

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
