from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return "Hello World!"



# Reading the file's data
file = open("static/occupations.csv", 'r')
file.readline() # remove first header line

occupationData = dict()
for line in file: # for each line, splits occupation and number
    splitList = line.rsplit(',',1) # splits the line by the last found ','
    splitList[0] = splitList[0].strip('"') # takes away the '"' characters around the occupation
    splitList[1] = float(splitList[1]) # makes the percentage a float, recognizable by python

    if splitList[0] != 'Total': # removes the last line with occupation 'Total'
        occupationData[splitList[0]] = splitList[1]
file.close() # closes the file when done

def select():
    occupationList = list(occupationData.keys())
    percentageList = list(occupationData.values())

    choice = random.choices(occupationList,percentageList)[0]
    return choice

@app.route("/occupyflaskst")
def occupation():
    occupation = select()
    return render_template("/foist_template.html",
                            dict = occupationData)

if __name__ == "__main__":
    app.debug = True
    app.run()
