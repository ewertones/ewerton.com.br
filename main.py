import os
from flask import Flask, render_template, send_from_directory, url_for

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/cv/<lang>')
def get_pdf(lang='en'):
    return send_from_directory(os.path.join(app.root_path, 'static'), f'documents/cv_ewerton_{lang}.pdf', mimetype='application/pdf')

@app.route('/translations')
def get_flyer():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'documents/translation_flyer.pdf', mimetype='application/pdf')
    
@app.route('/img/translations')
def get_flyer():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'images/translation_flyer.jpg', mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))