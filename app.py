from flask import Flask, render_template
from flask_cors import CORS, cross_origin
app = Flask(__name__)
port = 5000
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run(port=port)