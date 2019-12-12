import json
from pathlib import Path
from pprint import pprint

def store_movies():
    movies = [
        {
            "id": 1,
            "title": "Terminator",
            "year": 1989
        },
        {
            "id": 2,
            "title": "Mall Cop",
            "year": 2014
        },
    ]

    data = json.dumps(movies, indent=4)
    path = Path("movies.json")
    path.write_text(data)

def read_movies():
    data = Path("movies.json").read_text()
    movies = json.loads(data)
    pprint(movies, width=10)


read_movies()