#Peihua Huang and Matthew Chan (Apples Bananas)
#SoftDev1 pd2
#K15 -- Login
#2019-10-02

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
import os
# imported Flask, render_template, and request
app = Flask(__name__)
#create instance of class Flask

usr = "apples"
pwd = "bananas"
# hardcode username and password
app.secret_key = os.urandom(32)
# set secret key to randomly generated string

@app.route("/")
def root():
    #print(url_for("login"))
    if ("loggedIn" in session):
        # if user is logged in
        return redirect(url_for("welcome"))
        # redirect to welcome page
    else:
        # else
        return redirect(url_for("login"))
        # redirect to login page

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
            # if password is incorrect
            return render_template("error.html", rsn = "incorrect password")
            # render error page and error message
    else:
        # if username is incorrect
        return render_template("error.html", rsn = "incorrect username")
        # render error page and error message
    return render_template("error.html", rsn = "bad juju")
    #if it fails for any othe reason, return error page and error message

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
    return render_template("template.html")
    # render template

@app.route("/logout")
def logout():
    if ("loggedIn" in session):
    # if user is logged in
        session.pop("loggedIn")
        # pop session to log user out
    return redirect("/")
    #redirect user back to root route

if __name__ == "__main__":
    app.debug = True
    app.run()
