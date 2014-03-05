from imdb import IMDb
ia = IMDb()

moviesDict={}

for number in range(100):
	idNumber = str(number+1)
	idNumber = "0"*(7-len(idNumber)) + idNumber

	movie = ia.get_movie(idNumber)
	try: 
		title = movie['title']
		if title != '':
			persons = movie['actors']
			actors = []
			i = 0
			for person in persons:
				try: 
					actors.append(person['name'])
					i += 1
				except: 
					continue
			moviesDict[title] = actors
	except: 
		continue

print moviesDict

