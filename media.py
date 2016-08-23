import webbrowser

class Movie:
	def __init__(self, movie_name, storyline, thumbnail, trailer):
		self.movie_name = movie_name
		self.storyline = storyline
		self.thumbnail = thumbnail
		self.trailer = trailer

	def show_trailer(self):
		webbrowser.open(self.trailer)