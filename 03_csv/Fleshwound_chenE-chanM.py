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

def select():
	occupationList = list(occupationData)
	percentageList = list()
	for job in occupationList:
		percentageList.append(occupationData[job])

	choice = random.choices(occupationList,percentageList)
	print(choice)