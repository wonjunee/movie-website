# -*- coding: utf8 -*-
import fresh_tomatoes
import media
import urllib
import json
import pprint
import os

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

def create_request_url_details(query, api_key, sig):
	return "http://api.rovicorp.com/data/v1.1/movie/info?cosmoid={}&country=US&language=en&format=json&apikey={}&sig={}".format(query, api_key, sig)
	
# This is function is used to request url and extract data from it
def request_API(sig, query, id):
	# Setting API key
	api_key, secret_key = reading_api_key()
	print "api_key:",api_key
	print "secret key:",secret_key

	# Setting query
	query = "batman"

	# Setting request url
	request_url = "http://api.rovicorp.com/search/v2.1/video/search?entitytype=movie&query={}&rep=1&size=20&offset=0&language=en&country=US&format=json&apikey={}&sig={}".format(query, api_key, sig)
	print request_url

	# Searching Batman related movies
	connection = urllib.urlopen(request_url)
	output = connection.read()
	connection.close()

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
	# Setting API key
	api_key, secret_key = reading_api_key()
	print "api_key:",api_key
	print "secret key:",secret_key
	sig = "4ff6e610fefc9aa453a493854ce9e80b"
	# Setting query
	query = "batman"



	# Searching Batman related movies
	connection = urllib.urlopen(request_url)
	output = connection.read()
	connection.close()

	# Save the output into json format
	output = json.loads(output)

	# We are only interested in title and id from this output
	results = output['searchResponse']['results']
	for i in results:
		print i['video']['masterTitle']
		print i['id']

	# Save Json file to local drive
	with open("movies.json", "w") as F:
		json.dump(output, F)

output = json.loads(output)
# pprint.pprint(output)


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