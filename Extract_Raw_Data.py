from imdb import IMDb
from pymongo import MongoClient
ia = IMDb()

# moviesDict={}

client = MongoClient()
db = client.test_database
movies = db.movies
db.movies.remove()

for number in range(5000000):
	idNumber = str(number+1)
	idNumber = "0"*(7-len(idNumber)) + idNumber

	movie = ia.get_movie(idNumber)
	title = movie['title']
	if title != '':
		try: 
			persons = movie['actors']
			actors = []
			i = 0
			for person in persons:
				try: 
					actors.append(person['name'])
					i += 1
				except: 
					continue
			# moviesDict[title] = actors
			movie = {"movie": title,
			    "actors": actors}
			movie_id = movies.insert(movie)
		except: 
			continue