from flask import Flask

app = Flask(__name__)

# ASCII art for Flask logo with project name and infinity sign
flask_logo = '''
      _ _       
     | (_)      
  ___| |_  __ _ 
 / __| | |/ _` |
 \__ \ | | (_| |
 |___/_|_|\__,_|
    GCP-DEVOPS-PROJECT
            ∞
'''

@app.route('/')
def hello_world():
    return flask_logo + '\n\nHello, This is a Simple Flask Application!!'

@app.route('/app')
def hello_app():
    return flask_logo + '\n\nWelcome to the Application!!'

if __name__ == '__main__':
    app.run(debug=True)
