from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Cria a instancia da classe Flask
app = Flask(__name__)

# Clase base para modelos do SQLAlchemy
class Base(DeclarativeBase):
    pass

# Inicia o SQLAlchemy com a classe base
db = SQLAlchemy(model_class=Base)

# Configura a URI do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto.db'
db.init_app(app)

# Isso evita problemas de importação circular
from app.controllers import routes