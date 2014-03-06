import pymongo
from pymongo import MongoClient
client = MongoClient()

db = client.ActorList

actors = db.actors

# start_actor = 'Kevin BaconI'
start_actor = 'Chuck Norris'
end_actor = 'Meryl Streep'

FirstLayer = actors.find_one({'actor':start_actor})

for first_layer_movie in FirstLayer['movies']:
    SecondLayer = movies.find_one({'movie': movie})
        for second_layer_actor in SecondLayer['actors']:
            if second_layer_actor == end_actor:
                print (start_actor + " is connected to " + end_actor + \
                    " by " + first_layer_movie)
            else:
                ThirdLayer = actors.find_one({'actor':second_layer_actor})
                for third_layer_movie in ThirdLayer['movies']:
                    FourthLayer = movies.find_one({'movie': third_layer_movie})
                    for fourth_layer_actor in FourthLayer['actors']:
                        if fourth_layer_actor == end_actor:
                            print (start_actor + " is connected to " + \
                                end_actor + " by " + first_layer_movie + \
                                " and " + third_layer_movie)
                        else:
                            print("I give up!")