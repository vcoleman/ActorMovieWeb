import csv
import pymongo
from pymongo import MongoClient
client = MongoClient()

db = client.ActorList

actors = db.actors
# db.actor.remove()

previousName = ''
moviesList = []
with open('actresses.list.csv', 'rb') as actorslist:
    actorsreader = csv.DictReader(actorslist, ["actor_first", "actor_last", "movie"])
    for row in actorsreader:
        lastName = row['actor_last']
        firstName = row['actor_first']
        fullName = firstName + " " + lastName
        movie = row['movie']
        if fullName == previousName:
            moviesList.append(movie)
        else:
            actor = {"actor": previousName,
                "movies": moviesList}
            actor_id = actors.insert(actor)
            moviesList = [movie]
        previousName = fullName

print actors.count()