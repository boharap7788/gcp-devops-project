from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,This is Simple Flask Application !!'

@app.route('/app')
def hello_world():
    return 'Hello,This is Simple Flask Application !!'