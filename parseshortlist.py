import csv
import pymongo
from pymongo import MongoClient
client = MongoClient()

db = client.shortActressList

actors = db.actors
movies = db.movies
db.actors.remove()

actor_to_movies = {}
movie_to_actors = {}
previousName = ''
moviesList = []
actorsList = []
with open('shortactresslist.csv', 'rb') as actresslist:
    actorreader = csv.DictReader(actresslist, ["actor_first", "actor_last", "movie"])
    for row in actorreader:
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
            actorInstance = actors.find_one({"actor": "Elizabe Aaron"})
            actor = {"actor": previousName,
                "movies": moviesList}
            actor_id = actors.insert(actor)
            actor_to_movies[previousName] = moviesList
            moviesList = [movie]

            ###### insert info into movies collection
            for movie in moviesList:
                #will create entry if none exists

                movieInstance = movies.find_one({"movie": movie})

                if movieInstance == None:
                    actorsList = [fullName]
                else:
                    actorsList = movieInstance["actors"].append(fullName)
                
                movies.update({"movie":movie}, {"actors": actorsList}, upsert=True)

        previousName = fullName
        
print len(actor_to_movies)

print actors.count()