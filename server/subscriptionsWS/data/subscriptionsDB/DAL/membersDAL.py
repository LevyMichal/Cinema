from pymongo import MongoClient
from bson import ObjectId


class MembersDAL:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["subscriptionsDB"]
        self.__collection = self.__db["members"]

    # get all members
    def get_all_members(self):
        members = list(self.__collection.find({}))
        return members

    # # get member by id
    # def get_member_by_id(self, id):
    #     member = self.__collection.find_one({"_id": ObjectId(id)})
    #     return member

    # # add member
    # def add_member(self, member):
    #     self.__collection.insert_one(member)
    #     return member

    # # update member
    # def update_member(self, id, member):
    #     self.__collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": member})
    #     return member

    # # delete member
    # def delete_movie(self, id):
    #     self.__collection.find_one_and_delete({"_id": ObjectId(id)})
    #     return f"The member with ID {id} DELETED"
