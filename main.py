import os
from flask import Flask, render_template, send_from_directory, url_for, request
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, FileField, SubmitField, validators
from wtforms.fields.html5 import EmailField
from mailjet_rest import Client
from google.cloud import bigquery


class ContactForm(FlaskForm):
    name = StringField('Name:', [validators.InputRequired('?'), validators.Length(max=255)])
    email = EmailField('Email:', [validators.InputRequired('??'), validators.Email()])
    message = TextAreaField('Message:', [validators.InputRequired('???')])
    recaptcha = RecaptchaField()

class RawEmailsForm(FlaskForm):
    raw = TextAreaField('Emails:', [validators.InputRequired('???')])
    recaptcha = RecaptchaField()

def send_to_db(params):
    text = params.get('raw').splitlines()
    emails = ''.join(map("('{0}'), ".format, lista)).strip(', ')
    query = f'INSERT INTO `ewerton-com-br.emails.raw` VALUES {emails}'
    
    client = bigquery.Client()
    query_job = client.query(query)

def send_email(params):
    """ Use Mailjet API to send email """
    MAILJET_KEY = '87d785b193f39adcf6aa35e8fad9af27'
    MAILJET_SECRET = 'a14f61549fa49e97a4a774cf0b00fa95'
    mailjet = Client(auth=(MAILJET_KEY, MAILJET_SECRET), version='v3.1')

    email = {
        "Messages": [
            {
                "From": {
                "Email": "ewerton@ewerton.com.br",
                "Name": "Ewerton E. de Souza"
                },
                "To": [
                {
                "Email": 'ewerton@ewerton.com.br'
                }
                ],
            "Subject": "ewerton.com.br - Contact Form",
            "HTMLPart": f"Name: {params.get('name')} <br/><br/> Email: {params.get('email')} <br/><br/> Message: {params.get('message')}",
        }
        ]
    }
    try:
        result = mailjet.send.create(data=email)
    except Exception as exception:
        print(exception)

app = Flask(__name__)
app.config['SECRET_KEY'] = '22bfddd8e6ca2a4739723034f02ced9c3014a8892d9bace1'
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LdQn1obAAAAAE1lwWFuBqFbbo7CbxX6K-jDp_Kg'
app.config['RECAPTCHA_PRIVATE_KEY'] ='6LdQn1obAAAAAJHisBMReP5ihnXguwWYAyaQg3dx'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/tutorials')
def tutorials():
    return render_template('tutorials.html')

@app.route('/vagas')
@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST' and form.validate_on_submit():
        send_email(request.form)
        return render_template("contact.html", form=form, success=True)

    return render_template('contact.html', form=form)

@app.route('/raw',  methods=['GET', 'POST'])
def raw():
    form = RawEmailsForm()

    if request.method == 'POST' and form.validate_on_submit():
        send_to_db(request.form)
        return render_template("raw.html", form=form, success=True)
    
    return render_template('raw.html',  form=form)

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(os.path.join(app.root_path, 'static'), request.path[1:])

@app.route('/cv/<lang>')
def get_pdf(lang='en'):
    return send_from_directory(os.path.join(app.root_path, 'static'), f'documents/cv_ewerton_{lang}.pdf', mimetype='application/pdf')

@app.route('/translations')
def get_flyer():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'documents/translation_flyer.pdf', mimetype='application/pdf')
    
@app.route('/img/translations')
def get_jpg_flyer():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'images/translation_flyer.jpg', mimetype='image/jpeg')

# Start server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))