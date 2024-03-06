import requests


class SubscriptionsDAL:
    def __init__(self):
        # Base URL for all API endpoints
        self.__base_url = "http://127.0.0.1:8000"

    def _request(self, method, endpoint, data=None):
        # Helper function to make HTTP requests
        url = f"{self.__base_url}/{endpoint}"
        # print({"req": data})
        response = requests.request(method, url, json=data)
        # print({"DAL": response.json()})
        return response.json()

    # CRUD operations for all entities
    def get_all(self, entity):
        return self._request("GET", entity)

    def get_by_id(self, entity, item_id):
        return self._request("GET", f"{entity}/{item_id}")

    def create(self, entity, data):
        # print({"DAL": data})
        return self._request("POST", entity, data)

    def update(self, entity, item_id, data):
        return self._request("PUT", f"{entity}/{item_id}", data)

    def delete(self, entity, item_id):
        return self._request("DELETE", f"{entity}/{item_id}")
