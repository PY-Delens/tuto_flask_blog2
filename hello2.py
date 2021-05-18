from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello2():
    return 'Hello, World! from flask-tutorial hello2.py'
    
