import requests

class MembersWS:
    def __init__(self):
        self.__url = "http://jsonplaceholder.typicode.com/users"
    def get_members(self):
        response = requests.get(self.__url)
        return response.json()