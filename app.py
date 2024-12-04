from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Your IP is {request.remote_addr}'
