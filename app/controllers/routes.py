from flask import Flask, render_template
from app import app, db
from app.models import User

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/outro', methods=['GET', 'POST'])
def outro():
    return render_template('outro.html')

@app.route('/dados', methods=['GET', 'POST'])
def dados():
    return render_template('dados.html')

@app.route('/users')
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template('user/list.html', users=users)