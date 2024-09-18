\c games_db;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE player_games (
    id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(id),
    game_id INT REFERENCES games(id),
    duration INT,
    score INT,
    date DATE
);