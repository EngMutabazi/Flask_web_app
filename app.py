from flask import Flask #Here we are importing Flask class from flask

app = Flask(__name__) # This is the name of the module

@app.route("/")
def hello():
    return "<h1>Hello, World!</h1>"
