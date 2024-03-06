from DAL.moviesDAL import MoviesDAL


class MoviesBLL:
    def __init__(self):
        self.__movies = MoviesDAL()

    # get all movies
    def get_all_movies(self):
        movies = list(self.__movies.get_all_movies())
        return movies

    # # get movie by id
    # def get_movie_by_id(self, id):
    #     movies = self.get_all_movies()
    #     movie_exists = list(filter(lambda m: str(m["_id"]) == id, movies))
    #     if not movie_exists:
    #         return "movie is not exists"
    #     movie = self.__movies.get_movie_by_id(id)
    #     return movie

    # # add movie
    # def add_movie(self, movie):
    #     movies = self.get_all_movies()
    #     movie_exists = list(filter(lambda m: str(m["_id"]) == id, movies))
    #     if movie_exists:
    #         return "movie is already exists"
    #     self.__movies.add_movie(movie)
    #     return movie

    # # update movie
    # def update_movie(self, id, movie):
    #     movies = self.get_all_movies()
    #     movie_exists = list(filter(lambda m: str(m["_id"]) == id, movies))
    #     if not movie_exists:
    #         return "movie is not exists"
    #     updated_movie = self.__movies.update_movie(id, movie)
    #     return updated_movie

    # # delete movie
    # def delete_movie(self, id):
    #     movies = self.get_all_movies()
    #     movie_exists = list(filter(lambda m: str(m["_id"]) == id, movies))
    #     if not movie_exists:
    #         return "movie is not exists"
    #     self.__movies.delete_movie(id)
    #     return f"The movie with ID {id} DELETED"
