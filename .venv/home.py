import os
from flask import Flask, flash, request, redirect, url_for
from flask import render_template
from flask import send_from_directory
from werkzeug.utils import secure_filename
import urllib.request

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = 'secret-key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def hello_world():
    print("render template")
    return render_template('index.html')


@app.route("/upload", methods=["POST"])
def upload_file():
    print("upload function")
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Image uploaded successfully')
            return render_template('index.html', filename=filename)
        else:
            flash('Allowed image types are = jpg, jpeg')
            return redirect(request.url)
    return render_template('index.html', filename=filename)

# view uploaded(stored in server system) files
@app.route('/upload_files/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


if __name__ == "__main__":
    app.run(debug=True)