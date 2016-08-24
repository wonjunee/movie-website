# -*- coding: utf8 -*-
import fresh_tomatoes
import media
import urllib
import json
import pprint
import os
import sys
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
	return "http://api.rovicorp.com/search/v2.1/video/search?entitytype={}&query={}&rep=1&size=40&offset=0&language=en&country=US&format=json&apikey={}&sig={}".format(entitytype, query, api_key, sig)

# This function is used only for movies
# The movie data have to be requested with this separate url because
# This contains more detailed data such as director, actors, and so on.
def create_request_url_details(cosmoid, api_key, sig):
	return "http://api.rovicorp.com/data/v1.1/movie/info?cosmoid={}&country=US&language=en&format=json&apikey={}&sig={}".format(cosmoid, api_key, sig)

def make_connection(request_url):
	# connect to API to retrieve the data
	connection = urllib.urlopen(request_url)
	output = connection.read()
	connection.close()
	print output

	# Save the output into json format
	output = json.loads(output)
	return output

# This is function is used to request url and extract data from it
def request_data(entitytype, sig, query):
	# Setting API key
	api_key, secret_key = reading_api_key()

	# Setting request url
	request_url = create_request_url(entitytype, query, api_key, sig)
	print "request url:", request_url

	# Searching Batman related movies
	return make_connection(request_url)

# This is only used for movies to take more detailed information
# It uses different request format
def request_movie(sig, cosmoid):
	# Setting API key
	api_key, secret_key = reading_api_key()

	# Setting request url
	request_url = create_request_url_details(cosmoid, api_key, sig)
	print "request url:", request_url

	# Searching Batman related movies
	return make_connection(request_url)

def request_synopsis(sig, cosmoid):
	# Setting API key
	api_key, secret_key = reading_api_key()

	# Setting request url
	request_url = create_request_url_synopsis(cosmoid, api_key, sig)
	print "request url:", request_url

	# Searching Batman related movies
	return make_connection(request_url)

def parsing_movies(line):
	parsed = {}
	parsed["title"] = line["movie"]["title"]
	if line["movie"]["directors"]:
		parsed["director"] = line["movie"]["directors"][0]['name']
	parsed["producedBy"] = line["movie"]["producedBy"]
	parsed["releaseYear"] = line["movie"]["releaseYear"]
	parsed["releasedBy"] = line["movie"]["releasedBy"]
	parsed["rating"] = line["movie"]["rating"]
	return parsed
