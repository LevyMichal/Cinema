import json
import os
import sys


class Movies:
    def __init__(self):
        self.__path = os.path.join(sys.path[0], "data\\movies.json")
        print(self.__path)

    def get_movies(self):
        with open(self.__path, "r") as f:
            movies = json.load(f)
            final_movies = []
            for movie in movies:
                name = movie["name"]
                genres = movie["genres"]
                image = movie["image"]["medium"]
                premiered = movie["premiered"]

                final_movie = {
                    "name": name,
                    "genres": genres,
                    "image": image,
                    "premiered": premiered,
                }
                final_movies.append(final_movie)
            print(final_movies)
            return final_movies
