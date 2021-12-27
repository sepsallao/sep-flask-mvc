from flask import Blueprint, request
from .controller import *
from .views import *

api = Blueprint('api', __name__)

@api.route('/api/test')
def test_location():
    input_value = 420
    return test(input_value)

@api.route('/api/managed-list', methods=['GET', 'POST'])
def managed_list():
    if request.method == 'GET':
        company_name = request.args.get('content')
        return content_to_query(company_name)

# @api.route('/api/company-details', methods=['GET'])
# def company_details():
#     pass
