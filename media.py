import webbrowser

class Video():
	def __init__(self, title, storyline, poster_image_url):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url

class Movie(Video):
	""" This class provides a way to store movie related information"""
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	def __init__(self, title, storyline, poster_image_url, trailer, releaseYear, rating, director):
		Video.__init__(self, title, storyline, poster_image_url)
		self.trailer_youtube_url = trailer
		self.releaseYear = releaseYear
		self.rating = rating
		self.director = director

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

# This is a class for TV shows. But it won't be included in the website this time.
class TvShow(Video):
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	def __init__(self, title, storyline, poster_image_url, trailer):
		Video.__init__(self, title, storyline, poster_image_url)
		self.num_seasons = num_seasons
