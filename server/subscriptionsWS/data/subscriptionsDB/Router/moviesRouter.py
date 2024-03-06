from flask import Blueprint, jsonify, request
from DAL.movies import Movies

movies = Blueprint("movies", __name__)

BLL=Movies()

@movies.route("/", methods=["GET"])
def get_movies():
    all_movies = BLL.get_movies()
    return jsonify(all_movies)
