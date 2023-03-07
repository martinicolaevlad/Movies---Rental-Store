from src.domain.movie import Movie

import random


class Movie_repo:

    def __init__(self):
        self.__movie_list = []

        fin_data = open("repository\\movie_database.txt", "r", encoding="utf8")
        list_data = random.sample(fin_data.read().splitlines(), k=20)

        possible_id = list(range(1000, 10000))
        get_id = random.sample(possible_id, k=20)

        for i in range(20):
            movie_data = list_data[i].split("@")

            movie = Movie(get_id[i], movie_data[0].strip(), movie_data[1].strip(), movie_data[2].strip())
            self.add_movie(movie)

        movie = Movie(1111, "test", "test", "test")
        self.add_movie(movie)

    @property
    def movie_table(self):
        return self.__movie_list

    def find_by_id(self, movie_id):
        for movie in self.__movie_list:
            if movie.movie_id == int(movie_id):
                return movie
            else:
                return None

    def add_movie(self, movie):
        """

        :param movie:
        :return:
        """
        self.__movie_list.append(movie)

    def remove_movie(self, movie):
        """

        :param movie:
        :return:
        """
        del self.__movie_list[self.__movie_list.index(movie)]

    def update_movie(self, movie_id, title, description, genre):
        """

        :param movie_id:
        :param title:
        :param description:
        :param genre:
        :return:
        """
        for movie in self.__movie_list:
            if int(movie_id) == movie.movie_id:
                movie.title = title
                movie.description = description
                movie.genre = genre
