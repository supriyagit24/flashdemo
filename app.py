from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Supriya , Welcome to Flask app on EC2!'

if __name__ == '__main__':
    app.run(debug=False)
