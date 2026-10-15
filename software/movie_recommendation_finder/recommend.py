from __future__ import annotations

from .catalog import MOVIES


def _score(movie: dict, liked: dict | None, genres: set[str], mood: str) -> int:
    score = 0
    score += 3 * len(genres.intersection(movie["genres"]))
    if mood and movie["mood"] == mood:
        score += 2
    if liked:
        score += 4 * len(set(liked["genres"]).intersection(movie["genres"]))
        if liked["mood"] == movie["mood"]:
            score += 2
    return score


def find_movie(title: str) -> dict | None:
    needle = title.strip().lower()
    if not needle:
        return None
    for movie in MOVIES:
        if movie["title"].lower() == needle:
            return movie
    for movie in MOVIES:
        if needle in movie["title"].lower():
            return movie
    return None


def recommend(liked_title: str = "", genres: list[str] | None = None, mood: str = "", limit: int = 6) -> list[dict]:
    liked = find_movie(liked_title) if liked_title else None
    wanted = {g.strip().lower() for g in (genres or []) if g.strip()}
    mood = mood.strip().lower()
    ranked: list[tuple[int, dict]] = []
    for movie in MOVIES:
        if liked and movie["title"] == liked["title"]:
            continue
        score = _score(movie, liked, wanted, mood)
        if score <= 0:
            continue
        ranked.append((score, movie))
    ranked.sort(key=lambda item: (-item[0], item[1]["title"]))
    results = []
    for score, movie in ranked[:limit]:
        row = dict(movie)
        row["score"] = score
        results.append(row)
    return results
