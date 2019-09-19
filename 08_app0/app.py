from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    print(__name__)
    return "Hello World!"

@app.route("/test")
def test():
    print(__name__)
    return "test"

@app.route("/woah")
def wowza():
    print(__name__)
    return "this is pretty cool"

if __name__ == "__main__":
	app.debug = True
	app.run()