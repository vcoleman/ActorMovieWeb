import pynuodb

connection = pynuodb.connect("softsysActorweb", "localhost", "kgallagher", "softsys", options={'schema':'user'})
cursor = connection.cursor()

# cursor.execute("SELECT * FROM ACTOR")
# print cursor.fetchall()

while 1:
	search_movie = raw_input('Would you like to search by movie (m) or actor (a)?: ')
	if (search_movie == "q"): break

	if (search_movie == "m" or search_movie == "M"):
		data_input = raw_input('What movie would you like to search the actor/actress database by?: ')
		if (search_movie == "q"): break
		cursor.execute("SELECT NAME FROM ACTOR WHERE MOVIE LIKE \'%"+data_input+"%\'")
		for i in cursor.fetchall():
			print i[0]

	elif (search_movie == "a" or search_movie == "A"):
		data_input = raw_input('Which actor would you like to search the movie database by?: ')
		if (search_movie == "q"): break

		cursor.execute("SELECT MOVIE FROM ACTOR WHERE NAME LIKE \'%"+data_input+"%\'")
		for i in cursor.fetchall():
			print i[0]
	else:
		print("Unrecognizable character, type 'q' to exit if that's what you want to do")