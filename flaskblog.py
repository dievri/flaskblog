from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello, Sasha</h1><br><a href='/about'>Click here</a>"

@app.route("/about")
def about():
    return "<h2>We are smart!</h2>"