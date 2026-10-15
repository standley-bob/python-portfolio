MOVIES = [
    {"title": "Spirited Away", "year": 2001, "genres": ["animation", "fantasy"], "mood": "wonder"},
    {"title": "The Grand Budapest Hotel", "year": 2014, "genres": ["comedy", "drama"], "mood": "stylish"},
    {"title": "Mad Max: Fury Road", "year": 2015, "genres": ["action", "adventure"], "mood": "loud"},
    {"title": "Before Sunrise", "year": 1995, "genres": ["romance", "drama"], "mood": "quiet"},
    {"title": "Get Out", "year": 2017, "genres": ["horror", "thriller"], "mood": "tense"},
    {"title": "Paddington 2", "year": 2017, "genres": ["comedy", "family"], "mood": "cozy"},
    {"title": "Arrival", "year": 2016, "genres": ["sci-fi", "drama"], "mood": "thoughtful"},
    {"title": "John Wick", "year": 2014, "genres": ["action", "thriller"], "mood": "loud"},
    {"title": "Amélie", "year": 2001, "genres": ["romance", "comedy"], "mood": "whimsical"},
    {"title": "The Dark Knight", "year": 2008, "genres": ["action", "crime"], "mood": "tense"},
    {"title": "Whiplash", "year": 2014, "genres": ["drama", "music"], "mood": "intense"},
    {"title": "Coco", "year": 2017, "genres": ["animation", "family"], "mood": "warm"},
    {"title": "Parasite", "year": 2019, "genres": ["thriller", "drama"], "mood": "tense"},
    {"title": "The Matrix", "year": 1999, "genres": ["sci-fi", "action"], "mood": "cool"},
    {"title": "Lady Bird", "year": 2017, "genres": ["comedy", "drama"], "mood": "honest"},
    {"title": "Spider-Man: Into the Spider-Verse", "year": 2018, "genres": ["animation", "action"], "mood": "fun"},
    {"title": "Moonlight", "year": 2016, "genres": ["drama"], "mood": "quiet"},
    {"title": "Everything Everywhere All at Once", "year": 2022, "genres": ["sci-fi", "comedy", "action"], "mood": "wild"},
    {"title": "The Social Network", "year": 2010, "genres": ["drama"], "mood": "sharp"},
    {"title": "Knives Out", "year": 2019, "genres": ["mystery", "comedy"], "mood": "clever"},
    {"title": "Dune", "year": 2021, "genres": ["sci-fi", "adventure"], "mood": "epic"},
    {"title": "Little Miss Sunshine", "year": 2006, "genres": ["comedy", "drama"], "mood": "warm"},
    {"title": "Shaun of the Dead", "year": 2004, "genres": ["comedy", "horror"], "mood": "fun"},
    {"title": "Her", "year": 2013, "genres": ["romance", "sci-fi", "drama"], "mood": "tender"},
    {"title": "Ratatouille", "year": 2007, "genres": ["animation", "family", "comedy"], "mood": "warm"},
    {"title": "No Country for Old Men", "year": 2007, "genres": ["thriller", "crime"], "mood": "bleak"},
    {"title": "The Princess Bride", "year": 1987, "genres": ["adventure", "comedy", "romance"], "mood": "playful"},
    {"title": "Interstellar", "year": 2014, "genres": ["sci-fi", "drama"], "mood": "epic"},
    {"title": "The Farewell", "year": 2019, "genres": ["drama", "comedy"], "mood": "tender"},
    {"title": "Baby Driver", "year": 2017, "genres": ["action", "crime", "music"], "mood": "cool"},
]


MOOD_LABELS = {
    "bleak": "stormy",
    "clever": "clever",
    "cool": "cool kid",
    "cozy": "cozy night in",
    "epic": "go big",
    "fun": "just for fun",
    "honest": "no filter",
    "intense": "on edge",
    "loud": "turn it up",
    "playful": "playful",
    "quiet": "quiet hours",
    "sharp": "sharp",
    "stylish": "dressed up",
    "tender": "soft heart",
    "tense": "hold breath",
    "thoughtful": "thinky",
    "warm": "warm hug",
    "whimsical": "a bit silly",
    "wild": "chaos gremlin",
    "wonder": "wide-eyed",
}


def all_genres() -> list[str]:
    found = {genre for movie in MOVIES for genre in movie["genres"]}
    return sorted(found)


def all_moods() -> list[str]:
    return sorted({movie["mood"] for movie in MOVIES})


def mood_choices() -> list[dict[str, str]]:
    keys = sorted({movie["mood"] for movie in MOVIES})
    return [{"value": key, "label": MOOD_LABELS.get(key, key)} for key in keys]
