import os
from flask import Flask, json, jsonify
import psycopg2
from flask_cors import CORS
from .routes import api
from .models import model_blueprint

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.register_blueprint(api)
app.register_blueprint(model_blueprint)
