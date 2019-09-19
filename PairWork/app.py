from flask import Flask
app = Flask(__name__)

coll = [0,1,1,2,3,5,8]


@app.route("/")

def hello_world():
    print(__name__)
    return "Boo!"

#@app.route("/my_foist_template")

#def 

if __name__ == "__main__":
	app.debug = True
	app.run()