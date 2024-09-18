from datetime import datetime, timedelta

import numpy as np
from dotenv import load_dotenv
from tqdm import tqdm

from src.classes import GamePlay, Player
from src.database import drop_and_create_tables, get_cursor
from src.settings import END_DATE, GAMES, PLAYERS, START_DATE


load_dotenv()


start_date = datetime.strptime(START_DATE, "%Y-%m-%d").date()
end_date = datetime.strptime(END_DATE, "%Y-%m-%d").date()
delta = (end_date - start_date).days


def generate_records_per_player(player: Player) -> list[GamePlay]:
    num_of_games_plays = np.random.binomial(n=delta, p=player.frequency)
    days = np.random.choice(range(delta), size=num_of_games_plays, replace=False)
    games = [game.name for game in player.games]
    games_preferences = [game.preference for game in player.games]
    games_play_times = [game.average_play_time for game in player.games]
    games_scores = [game.average_score for game in player.games]

    played_games = np.random.choice(games, size=num_of_games_plays, p=games_preferences)
    play_times = [
        np.random.gamma(shape=games_play_times[games.index(i)], scale=1, size=1)[0]
        for i in played_games
    ]
    scores = [
        np.random.gamma(shape=games_scores[games.index(i)], scale=1, size=1)[0]
        for i in played_games
    ]
    game_plays = [
        GamePlay(
            id=0,
            player_id=player.id,
            game_id=GAMES[played_games[i]],
            score=int(scores[i]),
            play_time=round(float(play_times[i]), 2),
            date=start_date + timedelta(days=int(days[i])),
        )
        for i in range(len(days))
    ]
    return game_plays


def main() -> None:
    drop_and_create_tables()
    for game_name, game_id in GAMES.items():
        with get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO games (id, name) VALUES (%s, %s)", (game_id, game_name)
            )
    for player in tqdm(PLAYERS):
        player_records = generate_records_per_player(player)
        with get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO players (id, name) VALUES (%s, %s)",
                (player.id, player.name),
            )
            for record in player_records:
                cursor.execute(
                    "INSERT INTO player_games (player_id, game_id, duration, score, date) VALUES (%s, %s, %s, %s, %s)",
                    (
                        record.player_id,
                        record.game_id,
                        record.play_time,
                        record.score,
                        record.date,
                    ),
                )


if __name__ == "__main__":
    main()
