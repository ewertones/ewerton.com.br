import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """Site em construção, volte outro dia!\n
              Site under maintenance, come back later!\n\n
              
              (I decided to build it from scratch using Flask, so I can better present my work and improve my front-end skills, haha'.\n\n
              
              You can reach me at ewerton@ewerton.com.br"""


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080))