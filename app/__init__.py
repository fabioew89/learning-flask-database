from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app.config['SECRET_KEY'] = 'f6b42562bc1f3ee92dbad7c9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto.db'
db.init_app(app)

from app.controllers import routes