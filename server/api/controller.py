from flask import Blueprint
from .views import *

api = Blueprint('api', __name__)

@api.route('/api/test')
def test_location():
    return test()

@api.route('/api/account')
def account_location():
    return accountList()
