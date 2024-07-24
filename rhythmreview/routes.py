# referenced https://github.com/andrewcannan/elite-pt-pro to help write log in / register functions (sent to me by mentor to help understand what is required for project)

from flask import render_template, request, redirect, url_for, session, flash
from rhythmreview import app, db
from rhythmreview.models import User, Reviews
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/")
def home():
    return render_template("base.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """ 
    Register a new user account if username does not already exist in database
    """
    if request.method == "POST":
        # check if username is in database
        user_exists = User.query.filter(
            User.username == request.form.get("username"))

        if user_exists:
            flash ("Username already exists, please choose another")
            return redirect(url_for("register"))
        
        #  create a new user account
        new_user = User(
            fname = request.form.get("fname"),
            lname = request.form.get("lname"),
            email = request.form.get("email"),
            username = request.form.get("username"),
            password = generate_password_hash(request.form.get("password)"))
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registration was successful")
        return redirect(url_for("home"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username is in database
        user_exists = User.query.filter(
            User.username == request.form.get("username"))

        # check if password is valid
        if user_exists:
            if check_password_hash(
                    user_exists.password, request.form.get("password")):
                session["user"] = request.form.get("username")
                return redirect(url_for(
                    "my_account", username=account["user"]))
            # if password is not valid
            else:
                flash("Username and/or Password incorrect")
                return redirect(url_for("login"))
        # if username is not in database
        else:
            flash("Username does not exist")
            return redirect(url_for("register"))
            
    return render_template("login.html")


    
