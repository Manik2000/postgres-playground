from src.classes import Game, Player


START_DATE = "2022-01-01"
END_DATE = "2024-12-31"


GAMES_NAMES = [
    "Battefront 2",
    "Minecraft",
    "FIFA 24",
    "Elden Ring",
    "Cyberpunk 2077",
    "For Honor",
    "My little pony",
    "The Witcher 3",
    "Battefield 2042",
    "Sekiro",
]

games = [Game(id=i, name=name) for i, name in enumerate(GAMES_NAMES)]

players = [
    Player(
        id=1,
        name="Alice",
        preferences={"Minecraft": 0.8, "The Witcher 3": 0.2},
        average_play_time=60,
        average_score=100,
        frequency=0.4,
    ),
    Player(
        id=2,
        name="Bob",
        preferences={"FIFA 24": 0.3, "Cyberpunk 2077": 0.7},
        average_play_time=30,
        average_score=90,
        frequency=0.7,
    ),
    Player(
        id=3,
        name="Marcin",
        preferences={"Battefront 2": 1},
        average_play_time=45,
        average_score=95,
        frequency=0.3,
    ),
    Player(
        id=4,
        name="Piotr",
        preferences={"Elden Ring": 0.4, "Sekiro": 0.4, "For Honor": 0.2},
        average_play_time=120,
        average_score=110,
        frequency=0.9,
    ),
    Player(
        id=5,
        name="Zofia",
        preferences={"My little pony": 1},
        average_play_time=15,
        average_score=85,
        frequency=0.1,
    ),
    Player(
        id=6,
        name="Alejandro",
        preferences={"Battefield 2042": 0.7, "My little pony": 0.2, "FIFA 24": 0.1},
        average_play_time=200,
        average_score=105,
        frequency=0.6,
    ),
    Player(
        id=7,
        name="Rene Descartes",
        preferences={"The Witcher 3": 0.5, "Cyberpunk 2077": 0.5},
        average_play_time=45,
        average_score=95,
        frequency=0.2,
    ),
]
