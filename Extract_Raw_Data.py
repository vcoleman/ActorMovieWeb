from imdb import IMDb
ia = IMDb()

moviesDict={}

for number in range(10):
	idNumber = str(number)
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
			moviesDict[title] = actors
		except: 
			continue

print moviesDict

