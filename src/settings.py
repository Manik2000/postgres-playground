from src.classes import Player, PlayersGame


START_DATE = "2022-01-01"
END_DATE = "2024-12-31"


GAMES = {
    "Battefront 2": 1,
    "Minecraft": 2,
    "FIFA 24": 3,
    "Elden Ring": 4,
    "Cyberpunk 2077": 5,
    "For Honor": 6,
    "My little pony": 7,
    "The Witcher 3": 8,
    "Battefield 2042": 9,
    "Sekiro": 10,
}


PLAYERS = [
    Player(
        id=1,
        name="Alice",
        games=[
            PlayersGame(
                name="Minecraft",
                preference=0.8,
                average_play_time=45,
                average_score=101,
            ),
            PlayersGame(
                name="The Witcher 3",
                preference=0.2,
                average_play_time=60,
                average_score=60,
            ),
        ],
        frequency=0.4,
    ),
    Player(
        id=2,
        name="Bob",
        games=[
            PlayersGame(
                name="FIFA 24", preference=0.3, average_play_time=33, average_score=90
            ),
            PlayersGame(
                name="Cyberpunk 2077",
                preference=0.7,
                average_play_time=42,
                average_score=90,
            ),
        ],
        frequency=0.7,
    ),
    Player(
        id=3,
        name="Marcin",
        games=[
            PlayersGame(
                name="Battefront 2",
                preference=1,
                average_play_time=125,
                average_score=95,
            )
        ],
        frequency=0.3,
    ),
    Player(
        id=4,
        name="Piotr",
        games=[
            PlayersGame(
                name="Elden Ring",
                preference=0.4,
                average_play_time=122,
                average_score=11,
            ),
            PlayersGame(
                name="Sekiro", preference=0.4, average_play_time=107, average_score=90
            ),
            PlayersGame(
                name="For Honor", preference=0.2, average_play_time=91, average_score=50
            ),
        ],
        frequency=0.9,
    ),
    Player(
        id=5,
        name="Zofia",
        games=[
            PlayersGame(
                name="My little pony",
                preference=1,
                average_play_time=15,
                average_score=85,
            )
        ],
        frequency=0.1,
    ),
    Player(
        id=6,
        name="Alejandro",
        games=[
            PlayersGame(
                name="Battefield 2042",
                preference=0.7,
                average_play_time=192,
                average_score=105,
            ),
            PlayersGame(
                name="My little pony",
                preference=0.2,
                average_play_time=310,
                average_score=105,
            ),
            PlayersGame(
                name="FIFA 24", preference=0.1, average_play_time=11, average_score=105
            ),
        ],
        frequency=0.6,
    ),
    Player(
        id=7,
        name="Rene Descartes",
        games=[
            PlayersGame(
                name="The Witcher 3",
                preference=0.5,
                average_play_time=566,
                average_score=95,
            ),
            PlayersGame(
                name="Cyberpunk 2077",
                preference=0.5,
                average_play_time=642,
                average_score=95,
            ),
        ],
        frequency=0.2,
    ),
]
