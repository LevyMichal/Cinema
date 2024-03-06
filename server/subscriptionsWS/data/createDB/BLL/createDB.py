from pymongo import MongoClient
from BLL.membersBLL import Members
from BLL.moviesBLL import Movies

members_bll = Members()
members = members_bll.get_all_members()

movies_bll = Movies()
movies = movies_bll.get_movies()


class MembersBLL:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["SubscriptionsDB"]
        self.__collection = self.__db["members"]

    def insert_members(self):
        members_from_DB = list(self.__collection.find({}))
        members_to_insert = members
        if len(members_from_DB) < 10:
            self.__collection.insert_many(members_to_insert)


class MoviesBLL:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["SubscriptionsDB"]
        self.__collection = self.__db["movies"]

    def insert_movies(self):
        movies_from_DB = list(self.__collection.find({}))
        movies_to_insert = movies
        if len(movies_from_DB) < 10:
            self.__collection.insert_many(movies_to_insert)
