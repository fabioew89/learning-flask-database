from flask import Flask

app = Flask(__name__)

from app.controllers import routes
from app.models import database
