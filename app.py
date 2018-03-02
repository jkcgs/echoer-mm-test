from flask import Flask, Response
from flask import request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        app.logger.info(request.data)
        print(request.data)
    
    return "Hello World!"

@app.route("/ping")
def ping():
    resp = Response('{"response_type": "in_channel", "text": "pong!"}')
    resp.headers['Content-Type'] = 'application/json'
    return resp
