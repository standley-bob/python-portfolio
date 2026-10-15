from flask import Blueprint, render_template, request

from data.projects import get_project
from data.site import NAME, ROLE
from software.movie_recommendation_finder.catalog import MOVIES, all_genres, mood_choices
from software.movie_recommendation_finder.recommend import recommend

bp = Blueprint(
    "movies",
    __name__,
    url_prefix="/apps/movies",
    template_folder="templates",
    static_folder="static",
)


@bp.route("/", methods=["GET", "POST"])
def home():
    query = (request.values.get("q") or "").strip()
    liked = (request.values.get("like") or query).strip()
    mood = (request.values.get("mood") or "").strip()
    genres = request.values.getlist("genre")
    results = []
    searched = request.method == "POST" or bool(liked or mood or genres or query)
    if searched:
        results = recommend(liked, genres, mood)
    project = get_project("movie-recommendation-finder")
    return render_template(
        "movies_app.html",
        name=NAME,
        role=ROLE,
        project=project,
        movies=MOVIES,
        genres=all_genres(),
        moods=mood_choices(),
        liked=liked,
        query=query,
        mood=mood,
        selected_genres=genres,
        results=results,
        searched=searched,
    )
