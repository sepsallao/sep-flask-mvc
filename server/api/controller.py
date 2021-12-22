from flask import Flask
from .views import *

app = Flask(__name__)

@app.route('/api/test')
def test_location():
    return test()

@app.route('/api/account')
def account_location():
    return accountList()
