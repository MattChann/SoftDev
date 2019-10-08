# Team "TBD"
# Matthew Chan & Ethan Chen
# SoftDev1 pd2
# K#17: No Trouble
# 2019-10-07

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================



with open('courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

with open('students.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


