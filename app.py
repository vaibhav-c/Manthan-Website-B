from flask import Flask, render_template
app = Flask(__name__)
port = 5000

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run(port=port)