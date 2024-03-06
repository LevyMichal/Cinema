from DAL.subscriptionsWS_DAL import SubscriptionsDAL


class SubscriptionsBLL:
    def __init__(self):
        self.__dal = SubscriptionsDAL()

    # Movies
    def get_all_movies(self):
        return self.__dal.get_all("movies")

    def get_movie_by_id(self, movie_id):
        return self.__dal.get_by_id("movies", movie_id)

    def create_movie(self, data):
        return self.__dal.create("movies", data)

    def update_movie(self, movie_id, data):

        movie = self.__dal.update("movies", movie_id, data)
        print({"BLL": movie})
        return movie

    def delete_movie(self, movie_id):
        return self.__dal.delete("movies", movie_id)

    # Members
    def get_all_members(self):
        return self.__dal.get_all("members")

    def get_member_by_id(self, member_id):
        return self.__dal.get_by_id("members", member_id)

    def create_member(self, data):
        return self.__dal.create("members", data)

    def update_member(self, member_id, data):
        return self.__dal.update("members", member_id, data)

    def delete_member(self, member_id):
        return self.__dal.delete("members", member_id)

    # Subscriptions
    def get_all_subscriptions(self):
        return self.__dal.get_all("subscriptions")

    def get_subscription_by_id(self, subscription_id):
        return self.__dal.get_by_id("subscriptions", subscription_id)

    def create_subscription(self, data):
        return self.__dal.create("subscriptions", data)

    def update_subscription(self, subscription_id, data):
        return self.__dal.update("subscriptions", subscription_id, data)

    def delete_subscription(self, subscription_id):
        return self.__dal.delete("subscriptions", subscription_id)
