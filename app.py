from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Request Headers:", request.headers)
    print("Request Method:", request.method)
    print("Request URL:", request.url)
    print("Request Path:", request.path)
    print("Request Args:", request.args)
    print("Request Form:", request.form)
    print("Request JSON:", request.get_json())
    print("Request Remote Addr:", request.remote_addr)
    print("Request Access Route:", request.access_route)
    
    forwarded_for = request.headers.get('X-Forwarded-For')
    
    # Return it or print it to see the value
    if forwarded_for:
        return f'X-Forwarded-For header: {forwarded_for}'
    else:
        return 'X-Forwarded-For header is not set'
