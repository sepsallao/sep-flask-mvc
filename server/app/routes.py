from flask import Blueprint
from .controller import *
from .views import *

api = Blueprint('api', __name__)

@api.route('/api/test')
def test_location():
    return test()

@api.route('/api/account')
def account_location():
    return accountList()

@api.route('/home')
def home():
    return Home()

@api.route('/about')
def about():
    return About()
