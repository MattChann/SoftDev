#Matthew Chan
#SoftDev1 pd2
#K25 -- Getting More REST
#2019-11-13

from flask import Flask
from flask import render_template
from urllib.request import urlopen
import json

app = Flask(__name__)   #create instance of class Flask

@app.route("/")
def root():
    u = urlopen("https://rickandmortyapi.com/api/character/1")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html",
                            name = data['name'])

if __name__ == "__main__":
    app.debug = True
    app.run()