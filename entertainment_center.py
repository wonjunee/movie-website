import fresh_tomatoes
import media
# This library that collects movie data
from tmdb3 import set_key

# This function will bring api key from the local file
def reading_api_key():
	with open("C:/tmdb_api_key") as F:
		for i in F:
			return i.strip()

# Setting API key
api_key = reading_api_key()
print "api_key:",api_key

set_key(api_key)

"""
Chaching Engine: in order to limit excessive 
usage against the online API server
"""
from tmdb3 import set_cache
set_cache('null')
set_cache(filename='/full/path/to/cache') # the 'file' engine is assumed
set_cache(filename='tmdb3.cache') # relative paths are put in /tmp
set_cache(engine='file', filename='~/.tmdb3cache')
from tmdb3 import get_locale, set_locale
set_locale()

### Searching Movies
from tmdb3 import searchMovie
res = searchMovie('asdf')
print res

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