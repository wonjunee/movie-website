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
from clean_json import clean_json

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
		sig = "6e6e1efb9e56ee3dc086d8547a8385e6"

		# Query will be always batman for this project
		query = "batman"

		# Create Json file from Rovi API
		output = request_data(entitytype, sig, query)

	except ValueError:
		sys.exit("\n\tERROR!! Please update the sig!!")

	# We are going to request the data for each movie from output file
	# This result will contain better data with more details
	results = output['searchResponse']['results']
	movies = {}

	# retrieving movie data
	for i in results:
		cosmoid = i['id']
		time.sleep(.5)
		movies[cosmoid] = request_movie("info", sig, cosmoid)
		movies[cosmoid]["synopsis"] = request_movie("synopsis", sig, cosmoid)
	
	# Save Json file to local drive
	with open("movies.json", "w") as F:
		json.dump(movies, F)

# Clean json file using clean_json function
movies = clean_json(movies)

# Parsing movies array. Only contain movie with synopsis and director
movies_parsed = []
for _,i in movies.iteritems():
	if i['status'] != 'error':
		parsed_movie = parsing_movies(i)
		if "synopsis" in parsed_movie.keys() and "director" in parsed_movie.keys():
			movies_parsed.append(parsing_movies(i))

# Print movies
for i in movies_parsed:
	pprint.pprint(i)
	pprint.pprint(i["director"])


# Number of movies
print "Number of movies:", len(movies)

# I manually found the trailer and image for each movie
# rovi has the API for it but it needs more clearance before I can use such feature
# Since I don't have such clearance, I decided to do this manually instead.

# Updating poster_image_url and trailer
trailer_image = {}
with open("trailer_image_urls.txt") as F:
	a = 0
	for line in F:
		if a % 3 == 0:
			movie_title = line.strip()
		elif a % 3 == 1:
			movie_image = line.strip()
		elif a % 3 == 2:
			movie_trailer = line.strip()
			trailer_image[movie_title] = [movie_image, movie_trailer]
		a += 1
for i in trailer_image:
	print i, trailer_image[i]

movies_instances = []
for i in movies_parsed:
	globals()[i["id"]] = media.Movie(i["title"], i["synopsis"], trailer_image[i["title"]][0], trailer_image[i["title"]][1], i["releaseYear"], i["rating"], i["director"])
	movies_instances.append(globals()[i["id"]])

for i in movies_instances:
	print i.title
	print
fresh_tomatoes.open_movies_page(movies_instances)