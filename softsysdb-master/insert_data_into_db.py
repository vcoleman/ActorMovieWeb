import pynuodb
import csv
 
connection = pynuodb.connect("softsysActorweb", "localhost", "kgallagher", "softsys", options={'schema':'USER'})
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS ACTOR")
sql = """CREATE TABLE ACTOR (
         ID int NOT NULL primary key,
         NAME 		VARCHAR(60),
         MOVIE   	VARCHAR(150))"""
cursor.execute(sql)

idcount = 0
with open('shortactors.csv', 'rb') as csvfile:
	actorReader = csv.reader(csvfile, delimiter=',')
	for row in actorReader:
		actor_val=(idcount,row[0]+" "+row[1], row[2][:148])
		cursor.execute("INSERT INTO ACTOR VALUES (?,?,?)", actor_val)
		idcount+=1
with open('shortactresses.csv', 'rb') as csvfile2:
	actressReader = csv.reader(csvfile2, delimiter=',')
	for row in actressReader:
		actress_val=(idcount,row[0]+" "+row[1], row[2][:148])
		cursor.execute("INSERT INTO ACTOR VALUES (?,?,?)", actress_val)
		idcount+=1

connection.commit()

# cursor.execute("SELECT * FROM ACTOR")
# print cursor.fetchone()

connection.close()