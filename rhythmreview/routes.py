from flask import render_template
from rhythmreview import app, db
from rhythmreview.models import User, Reviews

@app.route("/")
def home():
    return render_template("base.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

    
@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("base.html")