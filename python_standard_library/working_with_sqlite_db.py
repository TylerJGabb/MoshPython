import sqlite3
import json
import sys
from pathlib import Path


def get_connection():
    return sqlite3.connect("db.sqlite3")


def init_db():
    movies_sql = Path("movies.sql")
    text = movies_sql.read_text('utf8')
    with get_connection() as conn: conn.executescript(text)
    print('DB Initialized')


def load_movies_into_db():
    movies = json.loads(Path("movies.json").read_text())
    with get_connection() as conn:
        command = "insert into movies values (?,?,?)"
        for movie in movies:
            conn.execute(command, tuple(movie.values()))
        conn.commit()
    print("Loaded movies into DB")


def select_all_from_movies():
    with get_connection() as conn:
        cursor = conn.execute("select * from movies")
        for row in cursor:
            print(row)


if __name__ == '__main__':
    init_db()
    load_movies_into_db()
    select_all_from_movies()
