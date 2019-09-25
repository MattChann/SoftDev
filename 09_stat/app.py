# Team "Space Tigers"
# Matthew Chan & Jacob Olin
# SoftDev1 pd2
# K#09: ’Tis Not a Race -- But You Will Go Faster
# 2019-09-19

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")

def hello_world():
    print(__name__)
    return "Boo!"

collection = [0,1,1,2,3,5,8]
@app.route("/my_foist_template")
def template():
    return render_template("/foist_template.html",
                            coll = collection,
                            foo = "Good title")

if __name__ == "__main__":
	app.debug = True
	app.run()
