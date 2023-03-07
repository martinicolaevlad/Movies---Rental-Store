class Movie:

    def __init__(self, movie_id, title, description, genre):
        """
        Create a new movie.
        :param movie_id:
        :param title:
        :param description:
        :param genre:
        """
        self.__movie_id = movie_id
        self.__title = title
        self.__description = description
        self.__genre = genre

    @property
    def movie_id(self):
        return self.__movie_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self,title):
        self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self,description):
        self.__description = description

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self,genre):
        self.__genre = genre