from datetime import datetime, timedelta

import numpy as np
from dotenv import load_dotenv
from tqdm import tqdm

from src.classes import GamePlay, Player
from src.database import get_cursor, drop_and_create_tables
from src.settings import END_DATE, START_DATE, games, players


load_dotenv()


start_date = datetime.strptime(START_DATE, "%Y-%m-%d").date()
end_date = datetime.strptime(END_DATE, "%Y-%m-%d").date()
delta = (end_date - start_date).days


def generate_records_per_player(player: Player) -> list[GamePlay]:
    num_of_games_plays = np.random.binomial(n=delta, p=player.frequency)
    days = np.random.choice(range(delta), size=num_of_games_plays, replace=False)
    play_times = np.random.gamma(
        shape=player.average_play_time, scale=1, size=len(days)
    )
    scores = np.random.gamma(shape=player.average_score, scale=1, size=len(days))
    games_names = list(player.preferences.keys())
    played_games = np.random.choice(
        games_names, size=len(days), p=list(player.preferences.values())
    )
    game_plays = [
        GamePlay(
            id=0,
            player_id=player.id,
            game_id=next(game.id for game in games if game.name == played_games[i]),
            score=int(scores[i]),
            play_time=int(play_times[i]),
            date=start_date + timedelta(days=int(days[i])),
        )
        for i in range(len(days))
    ]
    return game_plays


def main() -> None:
    drop_and_create_tables()
    for game in games:
        with get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO games (id, name) VALUES (%s, %s)", (game.id, game.name)
            )
    for player in tqdm(players):
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
                        record.score,
                        record.play_time,
                        record.date,
                    ),
                )


if __name__ == "__main__":
    main()
