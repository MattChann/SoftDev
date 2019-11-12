#Matthew Chan
#SoftDev1 pd2
#K24 -- A RESTful Journey Skyward
#2019-11-12

from flask import Flask
from flask import render_template
from urllib3 import urlopen
import json

app = Flask(__name__)   #create instance of class Flask

@app.route("/")
def root():
    u = urllib3.urlopen("https://api.nasa.gov/planetary/apod?api_key=kPinVCLcM17ri49dnZA0pd0pGlnfZhh7g7OyR0Fo")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html",
                            pic = data['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
