import json
import os
import sys


class PermissionsFile:
    def __init__(self):
        self.__path = os.path.join(sys.path[0], "data\\permissions.json")

    # CRUD functions:

    def get_all_permissions(self):
        with open(self.__path) as f:
            data = json.load(f)
            # print(data["permissions"])
            return data["permissions"]

    def get_permissions_by_id(self, id):
        with open(self.__path) as f:
            data = json.load(f)
            permissions = data["permissions"]
            permission = list(filter(lambda p: p["id"] == id, permissions))
            # print(permission)
            return permission

    def add_permissions(self, new_permissions):
        permissions = self.get_all_permissions()
        permissions.append(new_permissions)
        with open(self.__path, "w") as f:
            json.dump({"permissions": permissions}, f)
        status = f"User created"
        # print(status)
        return status

    def update_permissions(self, id, updated_value):
        permissions = self.get_all_permissions()
        # Find the index of the user with the specified ID
        index = next((i for i, user in enumerate(permissions) if user["id"] == id))

        # Update the specified field with the new value
        permissions[0]["permissions"] = updated_value

        # Save the updated list back to the JSON file
        with open(self.__path, "w") as f:
            json.dump({"permissions": permissions}, f)

        status = f" user with ID {id} updated successfully."
        # print(status)
        return status

    def delete_permissions(self, id):
        permissions = self.get_all_permissions()
        # Find the index of the user with the specified ID
        index = next((i for i, user in enumerate(permissions) if user["id"] == id))

        # DELETE the specified user permissions
        permissions.pop(index)

        # Save the updated list back to the JSON file
        with open(self.__path, "w") as f:
            json.dump({"permissions": permissions}, f)

        status = f" user with ID {id} deleted successfully."
        # print(status)
        return status
