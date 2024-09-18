from dataclasses import dataclass
from datetime import datetime


@dataclass
class PlayersGame:
    name: str
    preference: float
    average_play_time: float
    average_score: int


@dataclass
class Player:
    id: int
    name: str
    games: list[PlayersGame]
    frequency: float

    def __post_init__(self):
        total = sum(i.preference for i in self.games)
        if abs(total - 1) > 1e-5:
            raise ValueError(
                f"Sum of preferences for player {self.name} is not equal to 1 but {total}."
            )


@dataclass
class GamePlay:
    id: int
    player_id: int
    game_id: int
    score: int
    play_time: float
    date: datetime
