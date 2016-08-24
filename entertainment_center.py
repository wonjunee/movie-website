# -*- coding: utf8 -*-
import fresh_tomatoes
import media
import urllib
import json
import pprint
import os
import time

# This function will bring api key from the local file
def reading_api_key():
	lis = []
	with open("C:/rovi_api_key") as F:
		for i in F:
			lis.append(i.strip())
	return lis[0], lis[1]

# Creating urls to request
def create_request_url(entitytype, query, api_key, sig):
	return "http://api.rovicorp.com/search/v2.1/video/search?entitytype={}&query={}&rep=1&size=20&offset=0&language=en&country=US&format=json&apikey={}&sig={}".format(entitytype, query, api_key, sig)

# This function is used only for movies
# The movie data have to be requested with this separate url because
# This contains more detailed data such as director, actors, and so on.
def create_request_url_details(cosmoid, api_key, sig):
	return "http://api.rovicorp.com/data/v1.1/movie/info?cosmoid={}&country=US&language=en&format=json&apikey={}&sig={}".format(cosmoid, api_key, sig)
	
# This is function is used to request url and extract data from it
def request_data(entitytype, sig, query):
	# Setting API key
	api_key, secret_key = reading_api_key()

	# Setting request url
	request_url = create_request_url(entitytype, query, api_key, sig)
	print "request url:", request_url

	# Searching Batman related movies
	connection = urllib.urlopen(request_url)
	output = connection.read()
	connection.close()

	# Save the output into json format
	output = json.loads(output)

	return output

# This is only used for movies to take more detailed information
# It uses different request format
def request_movie(sig, cosmoid):
	# Setting API key
	api_key, secret_key = reading_api_key()

	# Setting request url
	request_url = create_request_url_details(cosmoid, api_key, sig)
	print "request url:", request_url

	# Searching Batman related movies
	connection = urllib.urlopen(request_url)
	output = connection.read()
	connection.close()
	print output
	# Save the output into json format
	output = json.loads(output)

	return output

# Rovi is the API for video data. It uses sig variable that is only usuable for 5 minutes
# once it is created. So instead of calling API everytime I run this script, I will save the result
# into the local directory and use the saved file when I rerun the script.
if "movies.json" in os.listdir(r"./"):
	print("\nmovies.json is in the current directory.\n")
	with open("movies.json") as F:
		for i in F:
			output = json.loads(i)
			break
else:
	# entitytype is movie or tvseries
	entitytype = "movie"

	# sig has to be updated manually everytime I run the script
	sig = "2e01942f7e7f8f0046a0db2dc098852e"

	# Query will be always batman for this project
	query = "batman"

	# Create Json file from Rovi API
	output = request_data(entitytype, sig, query)

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