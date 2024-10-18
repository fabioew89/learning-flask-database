from flask import render_template, request
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new-user', methods=['GET', 'POST'])
def user_create():
    if request.method == 'POST':
        if not request.form['f-username'] or not request.form['f-email']:
            username = request.form['f-username']
            email = request.form['f-email']
            return render_template('user/create.html', username=username, email=email)
    return render_template('user/create.html')