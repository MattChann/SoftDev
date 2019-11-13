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
    rickURL = urlopen("https://rickandmortyapi.com/api/character/1")
    rickData = json.loads(rickURL.read())
    mortyURL = urlopen("https://rickandmortyapi.com/api/character/2")
    mortyData = json.loads(mortyURL.read())
    mrpbURL = urlopen("https://rickandmortyapi.com/api/character/244")
    mrpbData = json.loads(mrpbURL.read())
    return render_template("index.html",
                            rick = rickData,
                            morty = mortyData,
                            mrpb = mrpbData)

if __name__ == "__main__":
    app.debug = True
    app.run()