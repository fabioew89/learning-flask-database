from flask import render_template, request
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new-user', methods=['GET', 'POST'])
def user_create():
    if request.method == 'POST':
        if not request.form['f_username'] or not request.form['f_email']:
            username = request.form['f_username']
            email = request.form['f_email']
            return render_template('user/create.html', username=username, email=email)
    return render_template('user/create.html')