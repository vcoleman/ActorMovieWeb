import csv
import pymongo
from pymongo import MongoClient
client = MongoClient()

db = client.ActorList

movies = db.movies
db.movies.remove()

moviesDict = {}

with open('softsysdb-master/imdb-data-parser-master/outputdata/2014-03-05_120756_ImdbParserOutput/actresses.csv', 'rb') as actorslist:
    actorsreader = csv.DictReader(actorslist, ["actor_first", "actor_last", "movie"])
    for row in actorsreader:
        lastName = row['actor_last']
        firstName = row['actor_first']
        fullName = firstName + " " + lastName
        movie = row['movie']
        actorsList = []
        if movie in moviesDict:
            actorsList = moviesDict[movie]
            actorsList.append(fullName)
            moviesDict[movie] = actorsList
        else:
            moviesDict[movie] = [fullName]

        #movieInstance = movies.find_one({"movie": movie})
        #if movieInstance == None:
        #    actorsList = [fullName]
        #    movie = {"movie":movie, 
        #        "actors": actorsList}
        #    movie_id = movies.insert(movie)
        #else:
        #    actorsList = movieInstance["actors"].append(fullName)
        #    movies.update({"movie":movie}, 
        #        {"actors": actorsList}, upsert=True)
    
    print "now to store...."
    for key, value in moviesDict.iteritems():
        value
        print key
        movies.update({"movie":key}, {"actors": value}, upsert=True)

print movies.count()