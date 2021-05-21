from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World! 2021-03-12a'

@app.route('/hello')
def hello():
    return 'Hello, World - from flask_blog'

@app.route('/just')  
def just():
    return 'justawebsite'

from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath) 
   
