# Movie Website
### Udacity Full Stack Developer Nanodegree Project 1
I used Python, HTML, and Javascript to create the website.
The website shows information batman movies if you click them.

---
Details
---------
**media.py**: This python script contains the movie and TV shows classes I used for this website.
- Video: This is the main class. It is divided into Movie and TvShow (TV show won't be included in this project)
- Movie: It contains everything included in Video plus trailer url.

**entertainment_center.py**: This is the python scripts that creates instances for batman movies. It uses the movie API to gather the movie data and saves the data into an array.

**fresh_tomatoes.py**: This script contains Javascript, HTML, and CSS scripts that creates .html file showing list of batman movies created from **entertainment_center.py**.

---
Note 8/24/2016
---------
Used Rovi API to retrieve movie data easily. Unfortunately, this API doesn't provide image url or trailer url.

Will find these urls manually from google and save the data into separate file.

---
Completed!
---------
HTML for batman movie website is ready to go!

Run **entertainment_center.py** file, then the script will create a website.