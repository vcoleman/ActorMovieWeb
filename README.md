ActorMovieWeb
=============

This is a new implementation of the classic oracle of bacon http://oracleofbacon.org/ using MongoDB.

To run this program there are several steps you must follow.

1. Go to ftp://ftp.fu-berlin.de/pub/misc/movies/database/ and download actors.list.gz and actresses.list.gz
2. Unzip these list files and place them into the inputdata folder of imdb-data-parser-master
3. Run imdbparser.py
4. Copy the files actors.list.tsv and actresses.list.tsv from the output data folder to the outside folder where the other scripts live.
5. Rename actors.list.tsv and actresses.list.tsv to actors.list.csv and actresses.list.csv
6. Run parselonglist.py with a MongoDB port open on your computer
7. Change parselonglist.py to take in the opposite script (either actors.list.csv or actresses.list.csv, whichever it has not already parsed)
8. Run parselonglist_movies.py
9. Change parselonglist_movies.py to take in the opposite script (either actors.list.csv or actresses.list.csv, whichever it has not already parsed)
