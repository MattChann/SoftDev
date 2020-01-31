#Matthew Chan
#SoftDev1 pd2
#K25 -- Getting More REST
#2019-11-13

from flask import Flask
from flask import render_template
from urllib.request import urlopen
import json

app = Flask(__name__)   #create instance of class Flask

# NOTE: need to make a file named "key.txt" that contains the key needed for the MapQuest Open Geocoding API
keyFile = open("key.txt", "r")
key = keyFile.read()
keyFile.close()

@app.route("/")
def root():
    # Rick and Morty API
    rickURL = urlopen("https://rickandmortyapi.com/api/character/1")
    rickData = json.loads(rickURL.read())
    mortyURL = urlopen("https://rickandmortyapi.com/api/character/2")
    mortyData = json.loads(mortyURL.read())
    mrpbURL = urlopen("https://rickandmortyapi.com/api/character/244")
    mrpbData = json.loads(mrpbURL.read())

    # MapQuest Open Geocoding API
    address = "1600 Pennsylvania Ave NW, Washington, DC 20500"
    address = address.replace(" ", "+")
    coordinates = {
        "latitude": 48.8584,
        "longitude": 2.2945,
    }
    geoForwardURL = urlopen(f"http://open.mapquestapi.com/geocoding/v1/address?key={key}&location={address}")
    geoForwardData = json.loads(geoForwardURL.read())
    geoReverseURL = urlopen(f"http://open.mapquestapi.com/geocoding/v1/reverse?key={key}&location={coordinates['latitude']},{coordinates['longitude']}")
    geoReverseData = json.loads(geoReverseURL.read())

    # Loripsum API
    numParagraphs = 10
    loripsumURL = urlopen(f"https://loripsum.net/api/{numParagraphs}/long/dl/bq/headers/decorate")
    loripsumData = loripsumURL.read()
    loripsumData = loripsumData.decode()
    loripsumData.replace("\n", "<br>")

    return render_template("index.html",
                            rick = rickData,
                            morty = mortyData,
                            mrpb = mrpbData,
                            geoForward = geoForwardData,
                            geoReverse = geoReverseData,
                            loripsum = loripsumData)

if __name__ == "__main__":
    app.debug = True
    app.run()