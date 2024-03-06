from pymongo import MongoClient
from bson import ObjectId


class MoviesBLL:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["subscribtionsDB"]
        self.__collection = self.__db["movies"]

    # get all movies
    def get_all_movies(self):
        movies = list(self.__collection.find({}))
        return movies

#     # get movie by id
#     def get_movie_by_id(self, id):
#         movie = self.__collection.find_one({"_id": ObjectId(id)})
#         return movie

#     # add movie
#     def add_movie(self, movie):
#         self.__collection.insert_one(movie)
#         return movie

#     # update movie
#     def update_movie(self, id, movie):
#         self.__collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": movie})
#         return movie

#     # delete movie
#     def delete_movie(self, id):
#         self.__collection.find_one_and_delete({"_id": ObjectId(id)})
#         return f"The movie with ID {id} DELETED"


# # m = MoviesBLL()
# # movies = m.get_all_movies()
# # print(movies)
