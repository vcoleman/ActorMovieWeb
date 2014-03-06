import csv
import pymongo
from pymongo import MongoClient
client = MongoClient()

db = client.ActorList

movies = db.movies
db.movies.remove()

with open('actresses.list.csv', 'rb') as actorslist:
    actorsreader = csv.DictReader(actorslist, ["actor_first", "actor_last", "movie"])
    for row in actorsreader:
        lastName = row['actor_last']
        firstName = row['actor_first']
        fullName = firstName + " " + lastName
        movie = row['movie']
        movieInstance = movies.find_one({"movie": movie})
        if movieInstance == None:
            actorsList = [fullName]
            movie = {"movie":movie, 
                "actors": actorsList}
            movie_id = movies.insert(movie)
        else:
            actorsList = movieInstance["actors"].append(fullName)
            movies.update({"movie":movie}, 
                {"actors": actorsList}, upsert=True)

print movies.count()