import pymongo
from pymongo import MongoClient
client = MongoClient()

db = client.ActorList

actors = db.actors
movies = db.movies

# start_actor = 'Kevin BaconI'
start_actor = 'Chuck Norris'
end_actor = 'Meryl Streep'
flag = 0

FirstLayer = actors.find_one({'actor':start_actor})

while flag == 0:
    for first_layer_movie in FirstLayer['movies']:
        if flag == 1: break
        SecondLayer = movies.find_one({'movie': first_layer_movie})
        for second_layer_actor in SecondLayer['actors']:
            if second_layer_actor == end_actor:
                print (start_actor + " is connected to " + end_actor + \
                    " by " + first_layer_movie)
                flag = 1
                break
            else:
                ThirdLayer = actors.find_one({'actor':second_layer_actor})
                for third_layer_movie in ThirdLayer['movies']:
                    FourthLayer = movies.find_one({'movie': third_layer_movie})
                    if flag == 1: break
                    for fourth_layer_actor in FourthLayer['actors']:
                        if fourth_layer_actor == end_actor:
                            print (start_actor + " is connected to " + \
                                end_actor + " by " + first_layer_movie + \
                                " sand " + third_layer_movie)
                            flag = 1
                            break
                            
print "Life is great, and I just worked. Boooyeah"
            
                        