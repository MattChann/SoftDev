# Team "Space Tigers"
# Matthew Chan & Jacob Olin
# SoftDev1 pd2
# K#10: Jinja Tuning
# 2019-09-23

from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return "Hello World!"



# Reading the file's data
file = open("static/occupations.csv", 'r') # opens the file in read mode to parse through the data

headerData = dict() # dictionary to hold the first line header
trailingData = dict() # dictionary to hold the last line total
occupationData = dict() # dictionary to hold the data and percentages in the csv file
for line in file: # for each line, splits occupation and number
    splitList = line.rsplit(',',1) # splits the line by the last found ','
    splitList[0] = splitList[0].strip('"') # takes away the '"' characters around the occupation
    
    if splitList[0] == 'Job Class': # stores the first line with occupation 'Job Class' as a header
        headerData[splitList[0]] = splitList[1]
    else:
        splitList[1] = float(splitList[1]) # makes the percentage a float, recognizable by python

        if splitList[0] == 'Total': # stores the last line with occupation 'Total' as a trailing data
            trailingData[splitList[0]] = splitList[1]
        else:
            occupationData[splitList[0]] = splitList[1] # stores the line as a key-value pair in the dictionary
file.close() # closes the file when done

def select():
    occupationList = list(occupationData.keys()) # gives a list of the occupations from the dictionary
    percentageList = list(occupationData.values()) # gives a list of the corresponding percentages/weights

    '''
    Uses random.choices to return a random weighted selection of occupations.
    The functions takes in choices and their corresponding weights to output
    any number of choices based on those weights.
    '''
    choice = random.choices(occupationList,percentageList)[0] # returns the choice in a list so we just take the only element of it out as a string
    return choice

@app.route("/occupyflaskst")
def occupation():
    chosen = select() # makes the selection after the route is loaded to make it change on reload
    return render_template("/occupations.html",
                            selection = chosen,
                            header = headerData,
                            dict = occupationData,
                            tail = trailingData)

if __name__ == "__main__":
    app.debug = True
    app.run()
