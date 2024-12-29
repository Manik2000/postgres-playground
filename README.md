# postgres-playground

A couple of exercises for setting up and querying Postgres database.

## Setup

### Version with standalone Postgres

1. Install Postgres (follow: https://www.postgresql.org/download/) and enter its CLI (`psql -U postgres`).

2. Create a database owner.

```sql
CREATE USER games_db_o WITH PASSWORD '';
```

3. Create a database.

```sql
CREATE DATABASE games_db OWNER games_db_o;
```

4. Create tables.

```sql
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
```
5. Create a user with read-only access.

```sql
CREATE USER games_db_r WITH PASSWORD '';
GRANT CONNECT ON DATABASE games_db TO games_db_r;
GRANT USAGE ON SCHEMA public TO games_db_r;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO games_db_r;
```

6. Insert the required credentials into `.env` file.


6. Uncomment the lines with `dotenv` inside `src/database.py` and comment the lines with the `get_db_password` which is used for Docker.

### Version with Docker

1. Install Docker
2. Preprare the `.env` file with the following content:

```bash
DB_USER=...
DN_NAME=games_db
```

3. Uncomment the lines with `get_db_password` inside `src/database.py` and comment the lines with the `dotenv`.

4. Create a file `db_password.txt` with the database password.

5. Run the following command:

```bash
docker-compose up --build
```

3. Connect to your database using either `psql` (` psql -h localhost -p 5433 -U games_db_o -d games_db`) or anything by your choice.


### Render

You can also host your database using Render for free. Create an account and simply choose the service from the available ones. Then you can connect to the database, set the credentials accordingly, and use `main.py` to fill up the database.

## Query exercises

You can find a list of exercises here: https://manik2000.github.io/postgres-playground/.

## Disclaimer

I created this small project for my brother. The synthetic data is quite dummy (I am planning to improve it), the database is of quite simple structure (only 3 tables), and there are not so many exercises.
