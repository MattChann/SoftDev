# Team "Disney Channel"
# Matthew Chan & David Lupea
# SoftDev1 pd2
# K#12: Echo Echo Echo
# 2019-09-26

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("/form.html")

@app.route("/auth")
def authenticate():
    '''
    print(app)                  # the <Flask 'app'> object
    print(request)              # the request being made
    print(request.args)         # the dictionary made from info entered
    print(request.headers)      # stuff about the computer making the request
    print(request.form)         # always gives empty immutable dict?
    print(request.method)       # what kind of request being made
    '''
    return render_template("/echo.html", name = request.args["answer"], method = request.method)


if __name__ == "__main__":
    app.debug = True
    app.run()
