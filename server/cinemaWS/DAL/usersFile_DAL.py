import json
import os
import sys


class UsersFile:
    def __init__(self):
        self.__path = os.path.join(sys.path[0], "data\\users.json")

    # CRUD functions:

    def get_all_users(self):
        with open(self.__path, "r") as f:
            data = json.load(f)
        # print(f"all users: {data["users"]}")
        return data["users"]

    def get_user_by_id(self, id):
        with open(self.__path, "r") as f:
            data = json.load(f)
            users = data["users"]
            user = list(filter(lambda u: u["id"] == id, users))
        # print(user)
        return user

    def add_user(self, user):
        users = self.get_all_users()
        users.append(user)
        with open(self.__path, "w") as f:
            json.dump({"users": users}, f)

        status = "User CREATED"
        # print(status)
        return status

    def update_user(self, id, field_name, updated_value):
        users = self.get_all_users()

        # Find the index of the user with the specified ID
        index = next((i for i, user in enumerate(users) if user["id"] == id))

        # Update the specified field with the new value
        users[index][field_name] = updated_value

        # Save the updated list back to the JSON file
        with open(self.__path, "w") as f:
            json.dump({"users": users}, f)

        status = f"Field '{field_name}' for user with ID {id} updated successfully."
        # print(status)
        return status

    def delete_user(self, id):
        users = self.get_all_users()

        # Find the index of the user with the specified ID
        index = next((i for i, user in enumerate(users) if user["id"] == id))

        # DELETE the specified user
        users.pop(index)

        # Save the updated list back to the JSON file
        with open(self.__path, "w") as f:
            json.dump({"users": users}, f)

        status = f"the user with ID {id} deleted successfully."
        # print(status)
        return status
