from flask import Flask, render_template

app = Flask(__name__)
projects = ["Airplane", "Car", "Boat"]

@app.route("/test")
def test():
    return render_template('test.html')

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')