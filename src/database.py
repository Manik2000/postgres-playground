import os
from contextlib import contextmanager
from typing import Generator

import psycopg2
from dotenv import load_dotenv


load_dotenv()


db_params = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}


@contextmanager
def get_cursor() -> Generator[psycopg2.extensions.cursor, None, None]:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()


def drop_and_create_tables() -> None:
    with get_cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS player_games")
        cursor.execute("DROP TABLE IF EXISTS players")
        cursor.execute("DROP TABLE IF EXISTS games")
        cursor.execute(
            "CREATE TABLE games (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL)"
        )
        cursor.execute(
            "CREATE TABLE players (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL)"
        )
        cursor.execute(
            "CREATE TABLE player_games (id SERIAL PRIMARY KEY, player_id INT REFERENCES players(id), game_id INT REFERENCES games(id), duration INT, score INT, date DATE)"
        )
