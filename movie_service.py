from src.domain.exceptions import IdAlreadyExists, IsLetter, TheIdMustHave4Digits, NoMovieWithThisId
from src.domain.movie import Movie


class Movie_service:

    def __init__(self, movie_repository):
        self.__movie_repo = movie_repository

    @property
    def movie_list(self):
        return self.__movie_repo.movie_table

    def verify_movie_id(self, movie_id):

        for movie in self.__movie_repo.movie_table:
            if movie.movie_id == int(movie_id):
                raise IdAlreadyExists

    @staticmethod
    def verify_isdigit_input(string):

        if not string.isdigit():
            raise IsLetter

    @staticmethod
    def verify_4digits(nr):
        if int(nr) < 1000 or int(nr) >= 10000:
            raise TheIdMustHave4Digits

    def add_movie(self, movie_id, title, description, genre):
        """

        :param movie_id:
        :param title:
        :param description:
        :param genre:
        :return:
        """
        movie = Movie(movie_id, title, description, genre)
        self.__movie_repo.add_movie(movie)

    def remove_movie(self, movie_id):
        """

        :param movie_id:
        :return:
        """
        x = 0
        for movie in self.__movie_repo.movie_table:
            if int(movie_id) == movie.movie_id:
                self.__movie_repo.remove_movie(movie)
                x = 1
        if x == 0:
            raise Exception("* There is no movie with this id in the list. *")

    def update_movie(self, movie_id, title, description, genre):
        """

        :param movie_id:
        :param title:
        :param description:
        :param genre:
        :return:
        """
        self.__movie_repo.update_movie(movie_id, title, description, genre)

    def verify_if_movie_exist(self, movie_id):
        """

        :param movie_id:
        :return:
        """
        x = 0
        for movie in self.__movie_repo.movie_table:
            if int(movie_id) == movie.movie_id:
                x = 1
        if x == 0:
            raise NoMovieWithThisId


