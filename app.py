from flask import Flask, render_template, request, jsonify, flash

app = Flask(__name__)
app.secret_key = "GREET_APP_TEST"


@app.route("/")
def index():
    flash("What's your name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']))
    return render_template("index.html")
