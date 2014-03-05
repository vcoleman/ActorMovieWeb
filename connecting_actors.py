import pymongo
from pymongo import MongoClient
client = MongoClient()

db = client.ActorList

actors = db.actors

start_actor = 'Kevin Bacon [I]'
end_actor = 'Chuck Norris'

FirstEntry = actors.find_one({'actor':start_actor})

print(FirstEntry)