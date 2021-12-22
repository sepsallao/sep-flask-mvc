from flask import Flask
from .controller import api

app = Flask(__name__)

app.register_blueprint(api)