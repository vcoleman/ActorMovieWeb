import timeit
import pynuodb

connection = pynuodb.connect("softsysActorweb", "localhost", "kgallagher", "softsys", options={'schema':'user'})
cursor = connection.cursor()


def find():
		cursor.execute("SELECT NAME FROM ACTOR WHERE MOVIE LIKE \'%%Kendra%\'")

t = timeit.Timer('find()', setup='from __main__ import find')
print t.timeit(number=100)
print t.timeit(number=1000)
print t.timeit(number=10000)