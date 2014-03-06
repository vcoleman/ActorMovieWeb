import pymongo
from pymongo import MongoClient
client = MongoClient()

db = client.ActorList

actors = db.actors
movies = db.movies

# start_actor = 'Kevin BaconI'

start_actor = 'Johnny Depp'
end_actor = 'Meryl Streep'
flag = 0

FirstLayer = actors.find_one({'actor':start_actor})


def get_user_input():
    valid = False
    while valid == False:
        startActor = raw_input("starting actor name (First Last): ")
        valid = check_actor_validity(startActor)
        if valid == False:
            print "Not a valid input, try again!"
            
    valid = False
    while valid == False:
        endActor = raw_input("target actor name (First Last): ")
        valid = check_actor_validity(startActor)
        if valid == False:
            print "Not a valid input, try again!"
            
    return [startActor,endActor]

#searches movie title for all related actors. Kicks out if finds it,
#continues if doesn't
#
# movie           string of movie title
# desiredActor    string of desired actor name
# actorPath       array of actors + movies to trace path between actors

def search_movie_for_actor(startingActor, desiredActor, actorPath):
    try:
        actorInstance = actors.find_one({'actor': startingActor})
        for movie in actorInstance['movies']:
            movieInstance = movies.find_one({'movie': movie})
            for actor in movieInstance['actors']:
                if actor == desiredActor:
                   actorPath.append(" --> " + movie + " --> " + actor)
                   return actorPath
        for movie in actorInstance['movies']:
            movieInstance = movies.find_one({'movie': movie})
            for actor in movieInstance['actors']:
                actorPath.append(" --> " + actor + " --> " + movie)
                return search_movie_for_actor(actor, desiredActor, actorPath)
        return "No connection :("
    except: 
        return "name not valid :("
        
def check_actor_validity(actor):
    if actors.find_one({'actor': actor}) == None:
        return False
    else:
        return True
   
# Main Function        
def find_actor_path():
    startingActor, desiredActor = get_user_input()
    actorPath = [startingActor]
    pathList = search_movie_for_actor(startingActor, desiredActor, actorPath)
    finalPath = ""
    for part in pathList:
        finalPath = finalPath + part
    return finalPath
    
print find_actor_path()
    
    
    

    