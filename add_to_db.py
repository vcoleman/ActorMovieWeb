#install pymongo on your computer
#run 'mongod' from the terminal to create a locally hosted database
#insert your dictionary into this list in place of movie_dict and run this script

import pymongo
from pymongo import MongoClient
client = MongoClient()

db = client.test_database

movies = db.movies

# movie_dict = {'Star Wars': ['Luke Skywalker', 'Darth Vader'], 'Star Trek': ['Spock', 'captain kirk']}


for movie_name,actors in movie_dict.iteritems():
    movie = {"movie": movie_name,
        "actors": actors}
    movie_id = movies.insert(movie)
    

# print(movies.find_one({'movie':'Star Trek'}))
