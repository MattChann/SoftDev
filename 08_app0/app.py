from flask import Flask
app = Flask(__name__)


@app.route("/")                 # 127.0.0.1:5000/test displays "Hello World!"
def hello_world():
    print(__name__)
    return "Hello World!"

@app.route("/test")             # 127.0.0.1:5000/test displays "test"
def test():                     # I don't think function names matter?
    print(__name__)
    return "test"

@app.route("/woah")             # 127.0.0.1:5000/woah displays "this is pretty cool"
def wowza():
    print(__name__)
    return "this is pretty cool"

if __name__ == "__main__":
    app.debug = True            # When True, gives error messages within the browser when attempting to load
    app.run()                   # If commented out, running "python3 app.py" does nothing