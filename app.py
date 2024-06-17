from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from filters import apply_filters
from PIL import Image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/filtered_images'

# Certifique-se de que o diretório existe
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        img = Image.open(file)
        filter_type = request.form.get('filter')
        img_filtered = apply_filters(img, filter_type)
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'filtered_image.jpg')
        img_filtered.save(output_path)
        
        return render_template('result.html', image_file='filtered_image.jpg', filter_type=filter_type)

@app.route('/download/<filename>')
def download_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
