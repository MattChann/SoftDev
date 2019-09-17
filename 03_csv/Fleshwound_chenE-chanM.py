import random

# Reading the file's data
file = open("occupations.csv", 'r')
file.readline() # remove first header line

occupationData = dict()
for line in file:
    splitList = line.rsplit(',',1)
    splitList[0] = splitList[0].strip('"')
    splitList[1] = float(splitList[1])

    if splitList[0] != 'Total':
        occupationData[splitList[0]] = splitList[1]
file.close()

# Selects a random occupation using weights
def select():
    occupationList = list(occupationData.keys())
    percentageList = list(occupationData.values())

    choice = random.choices(occupationList,percentageList)[0]
    return choice

# Testing for select() and generated percentages
def test(amountOfTests):
    testData = dict()
    occupationList = list(occupationData.keys())
    for job in occupationList:
        testData[job] = 0

    for i in range(amountOfTests):
        testData[select()] += 1
    
    for job in occupationList:
        testData[job] = (testData[job] / amountOfTests) * 100

    print("Occupations                                       Percentage   Tested Percentage ")
    print("=================================================|============|==================")
    for occupation,percentage in occupationData.items():
        print(f'{occupation:49}:{percentage:5}' + '       : ' + str(testData[occupation]))

# test(998000)