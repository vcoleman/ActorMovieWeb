import csv
import pymongo
from pymongo import MongoClient
client = MongoClient()

db = client.shortActressList

actresses = db.actresses
db.actresses.remove()

actor_to_movies = {}
previousName = ''
moviesList = []
with open('shortactresslist.csv', 'rb') as actresslist:
    actressreader = csv.DictReader(actresslist, ["actor_first", "actor_last", "movie"])
    for row in actressreader:
        lastName = row['actor_last']
#         print "Last Name: "+lastName+"\n"
        firstName = row['actor_first']
#         print "First Name: " +firstName+"\n"
        fullName = firstName + " " + lastName
        print fullName
        movie = row['movie']
        print "Movie: " + movie+"\n"
        if fullName == previousName:
            moviesList.append(movie)
#             print moviesList
        else:
            actress = {"actress": previousName,
                "movies": moviesList}
            actress_id = actresses.insert(actress)
            actor_to_movies[previousName] = moviesList
            moviesList = [movie]
        previousName = fullName
        
print len(actor_to_movies)

print actresses.count()