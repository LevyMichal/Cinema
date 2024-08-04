from DAL.usersDB_DAL import UsersDB
from DAL.usersFile_DAL import UsersFile
from DAL.permissionsFile_DAL import PermissionsFile


from bson import ObjectId


class UsersBLL:
    def __init__(self):
        self.__users_db = UsersDB()
        self.__users_file = UsersFile()
        self.__permissions_file = PermissionsFile()

    # CRUD functions:

    def get_all_users(self):
        users_db = list(self.__users_db.get_all_users())
        users_file = list(self.__users_file.get_all_users())
        permissions_file = list(self.__permissions_file.get_all_permissions())

        users = []

        for user in users_db:
            # data from users DB:
            id = user["_id"]
            user_name = user["userName"]
            password = user["password"]

            # data from users file:
            user_file = list(filter(lambda u: u["id"] == str(id), users_file))
            user_file = user_file[0]
            first_name = user_file["firstName"]
            last_name = user_file["lastName"]
            created_date = user_file["createdDate"]

            # data from permissions file:
            print(permissions_file)
            permission_file = list(
                filter(lambda p: p["id"] == str(id), permissions_file)
            )
            permission_file=permission_file[0]
            print(permission_file)
            permissions = permission_file["permissions"]
            print(permissions)

            # final users from all the data sources:
            users.append(
                {
                    "_id": id,
                    "userName": user_name,
                    "password": password,
                    "firstName": first_name,
                    "lastName": last_name,
                    "createdDate": created_date,
                    "permissions": permissions,
                }
            )

        print(users)
        return users


    def get_user_by_id(self, id):
        user_db = self.__users_db.get_user_by_id(id)
        user_file = self.__users_file.get_user_by_id(id)
        permissions_file = self.__permissions_file.get_permissions_by_id(id)

        # data from users DB:
        user_name = user_db["userName"]
        password = user_db["password"]

        # data from users file:
        user_file = user_file[0]
        first_name = user_file["firstName"]
        last_name = user_file["lastName"]
        created_date = user_file["createdDate"]

        # data from permissions file:
        permissions = permissions_file[0]["permissions"]

        # final user from all the data sources:
        user = {
            "_id": id,
            "userName": user_name,
            "password": password,
            "firstName": first_name,
            "lastName": last_name,
            "createdDate": created_date,
            "permissions": permissions,
        }
        # print(user)
        return user
    

    
    def get_user_by_username(self, username):
        user = self.__users_db.get_user_by_username(username)
        print(user)
        return user



    def add_user(self, new_user):

        # data from users DB:
        users_db = list(self.__users_db.get_all_users())

        #checked if this user already exists
        name_exists = list(
            filter(lambda u: u["userName"] == new_user["userName"], users_db)
        )

        if name_exists:
            print (f"user name {new_user["userName"]} already exists")
            return f"user name {new_user["userName"]} already exists"

        new_user_db = {"userName": new_user["userName"], "password": ""}
        user = self.__users_db.add_user(new_user_db)

        new_user_file = {
            "id": str(user["_id"]),
            "firstName": new_user["firstName"],
            "lastName": new_user["lastName"],
            "createdDate": new_user["createdDate"],
        }
        new_permissions_file = {
            "id": str(user["_id"]),
            "permissions": new_user["permissions"],
        }

        self.__users_file.add_user(new_user_file)
        self.__permissions_file.add_permissions(new_permissions_file)

        print(new_user_file)
        return "NEW USER CREATED"
    


    def update_user(self,id,fields_names, updated_values):
        
        for i,field_name in enumerate (fields_names):
        
            # determine which DAL to use based on the field_name:

            if field_name in ["userName", "password"]:

                # Use UsersDB DAL for database fields
                self.__users_db.update_user(id, field_name, updated_values[i])

            if field_name in ["firstName","lastName","createdDate"]:

                # Use UsersFile DAL for json file fields
                self.__users_file.update_user(id, field_name, updated_values[i])

            if field_name == "permissions":

                # Use Permissions File DAL for json file fields
                self.__permissions_file.update_permissions(id, updated_values[i])

        updated_user=self.get_user_by_id(id)
            
        # print({"updated_user":updated_user})
        return updated_user

        

    def delete_user(self, id):
        self.__users_db.delete_user(id)
        self.__users_file.delete_user(id)
        self.__permissions_file.delete_permissions(id)

        status = f"User with ID {id} deleted."
        print(status)
        return status
