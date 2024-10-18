from flask import Flask, render_template
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/outro', methods=['GET', 'POST'])
def outro():
    return render_template('outro.html')

@app.route('/dados', methods=['GET', 'POST'])
def dados():
    return render_template('dados.html')