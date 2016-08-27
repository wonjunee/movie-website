"""
This python script is to clean movie json file that contains
batman related movie data from Rovi API.
It searched 40 movies using a query "batman" but it contains
some movies that are not related to batman such as baatan, boatman, and so on.
"""

import json
import pprint

def clean_json(movies):
	# Calling movies.json
	with open("movies.json") as F:
		for i in F:
			movies = json.loads(i)

	new_json = {}
	for key, value in movies.iteritems():
		try:
			title = value["movie"]["title"]
			if "batman" in title.lower():
				new_json[key] = value
		except:
			print "\nError (removed from the list):", value

	return new_json