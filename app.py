from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    forwarded_for = request.headers.get('X-Forwarded-For')
    
    # Return it or print it to see the value
    if forwarded_for:
        return f'X-Forwarded-For header: {forwarded_for}'
    else:
        return 'X-Forwarded-For header is not set'
