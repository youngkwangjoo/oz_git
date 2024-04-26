from flask import Flask, request
import test

app = Flask(__name__)

@app.route('/')
def home():
    return "hello, This is Main Page!"

@app.route('/about')
def about():
    return "This is the about page!"

#동적으로 url파라미터 값을 받아서 처리해준다

import requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5001/submit'
    data = 'test data'
    response = requests.post(url = url, data = data)

    return response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print("GET method")
        
    if request.method == 'POST':
        print("POST method ***", request.data)

#postman을 쓰거나 request를 쓰면 post를 날릴수 있다. 

host = '127.0.0.1'
port = '5001'

if __name__ == "__main__":
    app.run(host=host, port = port)




##http://localhost:5000/