# -*- coding: utf8 -*-
import fresh_tomatoes
import media
import urllib
import json
import pprint
import os
import sys
import time
from rovi import request_data, request_movie, parsing_movies

# Rovi is the API for video data. It uses sig variable that is only usuable for 5 minutes
# once it is created. So instead of calling API everytime I run this script, I will save the result
# into the local directory and use the saved file when I rerun the script.
if "movies.json" in os.listdir(r"./"):
	print("\nmovies.json is in the current directory.\n")
	with open("movies.json") as F:
		for i in F:
			movies = json.loads(i)
			break
else:
	try:
		# entitytype is movie or tvseries
		entitytype = "movie"

		# sig has to be updated manually everytime I run the script
		sig = "9f33d82363a8d0b7aa40d6d5799d6623"

		# Query will be always batman for this project
		query = "batman"

		# Create Json file from Rovi API
		output = request_data(entitytype, sig, query)

	except ValueError:
		sys.exit("\n\tERROR!! Please update the sig!!")

	# We are going to request the data for each movie from output file
	# This result will contain better data with more details
	results = output['searchResponse']['results']
	movies = []
	for i in results:
		cosmoid = i['id']
		time.sleep(1)
		movies.append(request_movie(sig, cosmoid))
	
	# Save Json file to local drive
	with open("movies.json", "w") as F:
		json.dump(movies, F)

movies_parsed = []
for i in movies:
	if i['status'] != 'error':
		movies_parsed.append(parsing_movies(i))

for i in movies_parsed:
	pprint.pprint(i)

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", "A marine on an alien planet",
	"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
	"http://www.youtube.com/watch?v=-9ceBgWV8io")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
	"http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
	"https://www.youtube.com/watch?v=3PsUJFEBC74")



# movies = [toy_story, avatar, ratatouille]
# fresh_tomatoes.open_movies_page(movies)