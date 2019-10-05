#Peihua Huang and Matthew Chan (Apples Bananas)
#SoftDev1 pd2
#K16 -- Flashing and Template Inheritance
#2019-10-03

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
import os

app = Flask(__name__)   #create instance of class Flask

# hardcoded username and password
usr = "apples"
pwd = "bananas"

# set secret key to randomly generated string
app.secret_key = os.urandom(32)

@app.route("/")
def root():
    #print(url_for("login"))
    if ("loggedIn" in session):
        # if user is logged in redirect to welcome page
        return redirect(url_for("welcome"))
    else:
        # else redirect to login page
        return redirect(url_for("login"))

@app.route("/auth")
def authenticate():
    if (usr == request.args['username']):
        if (pwd == request.args['password']):
            # if both the username and password are correct
            session["loggedIn"] = usr
            # start a session and store username
            return redirect(url_for("welcome"))
            # redirect to welcome page
        else:
            # if password is incorrect render error page and flash error message
            flash("Error: incorrect password")
            return render_template("login.html")
    else:
        # if username is incorrect render error page and flash error message
        flash("Error: incorrect username")
        return render_template("login.html")
    #if it fails for any other reason, return error page and error message
    flash("Error: bad juju")
    return render_template("login.html")

@app.route("/welcome")
def welcome():
    if ("loggedIn" in session):
        # is user is logged in
        return render_template("welcome.html")
        # redirect to welcome page
    return redirect(url_for("login"))
    # else redirect to login page

@app.route("/login")
def login():
    return render_template("login.html")
    # render template

@app.route("/logout")
def logout():
    if ("loggedIn" in session):
        # if user is logged in pop session to log user out
        session.pop("loggedIn")
    return redirect("/")
    #redirect user back to root route

if __name__ == "__main__":
    app.debug = True
    app.run()
