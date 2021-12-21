from controller import main

hello = "hello"

@app.route('/api/test')
def test():
    return{'message':'test'}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
