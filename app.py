from scrapefeatured import featured_movies
from urllib.parse import urlparse
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    movies = featured_movies()
    names = []    
    urls = []
    for i in list(movies):
        urls.append(i)
        names.append(str(urlparse(str(i)).path).split(sep="/")[-1].replace('-', ' ').title())
    print(names)
    return ''

hello()