from flask import render_template
from rhythmreview import app, db


@app.route("/")
def home():
    return render_template("base.html")
