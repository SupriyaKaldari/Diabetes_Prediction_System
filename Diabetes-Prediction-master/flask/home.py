from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")


def preform():
    return render_template("performance.html")

app.run(debug=True)
