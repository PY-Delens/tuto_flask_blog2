from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World! from local tuto_flask_blog2 - TWO dimanche'
