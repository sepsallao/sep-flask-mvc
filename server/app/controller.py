from flask import jsonify

def test(input_value):
    return{'message':input_value}

def content_to_query(content):
    # return{'message':content}
    return jsonify({'message': content})