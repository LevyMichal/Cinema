from flask import Flask

from flask_cors import CORS
import json
from bson import ObjectId

from router.subscriptionsRouter import subscriptions
from router.usersRouter import users


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


app = Flask(__name__)
app.json_encoder = JSONEncoder
app.register_blueprint(subscriptions, url_prefix="/subscriptions")
app.register_blueprint(users, url_prefix="/users")


CORS(app)

app.run()


# from DAL.usersFile_DAL import UsersFile


# users = UsersFile()
# users.get_all_users()
# users.get_user_by_id("123")
# users.update_user("65b6133e6b59cd2a0820bd79", "firstName", "Avi")
# users.add_user(
#     {
#         "id": "456",
#         "firstName": "admin",
#         "lastName": "Admin",
#         "createdDate": "24/01/2024",
#     }
# )
# users.delete_user("456")

# from DAL.usersDB_DAL import UsersDB

# usersDB = UsersDB()
# usersDB.get_all_users()
# usersDB.delete_user("65bebb6e8e897e79de7a94d4")

# from BLL.usersBLL import UsersBLL

# users = UsersBLL()

# users.get_user_by_id("65b6133e6b59cd2a0820bd79")
# users.add_user(
#     {
#         "userName": "avi@gmail.com",
#         "firstName": "Avi",
#         "lastName": "Choen",
#         "createdDate": "28/01/24",
#         "user_permissions": [
#             "View Subscriptions",
#             "Create Subscriptions",
#             "Delete Subscriptions",
#         ],
#     }
# )
# users.get_all_users()

# users.delete_user("65b60c2b15c85610bece37da")
# users.delete_user("65b58dc851018808a4dddfb2")
# users.delete_user("65b58dd9cc0f5416eefdfef7")
# users.delete_user("65b608d3277b8432b9dfe667")
# users.delete_user("65b60979dbb97becc5602292")
# users.delete_user("65b58d68dc4df75d4b3f3849")

# users.update_user(
#     "65b6133e6b59cd2a0820bd79", ["password", "firstName"], ["avi@gmail.com", "Avi"]
# )

# from DAL.usersDB_DAL import UsersDB

# usersDB = UsersDB()
# usersDB.update_user("65b6133e6b59cd2a0820bd79", "password", "avi@gmail.com")
