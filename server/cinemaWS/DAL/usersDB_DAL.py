from pymongo import MongoClient
from bson import ObjectId


class UsersDB:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["UsersDB"]
        self.__collection = self.__db["users"]

    # CRUD functions:

    def get_all_users(self):
        users = list(self.__collection.find({}))
        print(users)
        return users

    def get_user_by_id(self, id):
        user = self.__collection.find_one({"_id": ObjectId(id)})
        # print(user)
        return user

    def add_user(self, user):
        self.__collection.insert_one(user)
        # print(user)
        return user

    def update_user(self, id, field_name, updated_value):
        full_update = {field_name: updated_value}
        self.__collection.update_one({"_id": ObjectId(id)}, {"$set": full_update})
        # print(updated_value)
        return updated_value

    def delete_user(self, id):
        self.__collection.delete_one({"_id": ObjectId(id)})
        return "DELETED"


# new_user = UsersDB()
# new_user.add_user({"userName": "admin@gmail.com", "password": "admin@gmail.com"})
# new_user.get_all_users()
