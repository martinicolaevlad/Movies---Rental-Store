class Rental:

    def __init__(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date):
        """

        :param rental_id: integer
        :param movie_id: integer
        :param client_id: integer
        :param rented_date: date
        :param due_date: date
        :param returned_date: date
        """
        self.__rental_id = rental_id
        self.__movie_id = movie_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__due_date = due_date
        self.__returned_date = returned_date

    @property
    def movie_id(self):
        return self.__movie_id

    @movie_id.setter
    def movie_id(self, value):
        self.__movie_id = value


    @property
    def rental_id(self):
        return self.__rental_id

    @rental_id.setter
    def rental_id(self,rental_id):
        self.__rental_id = rental_id

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, client_id):
        self.__client_id = client_id

    @property
    def rented_date(self):
        return self.__rented_date

    @rented_date.setter
    def rented_date(self, value):
        self.__rented_date = value

    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, value):
        self.__due_date = value

    @property
    def returned_date(self):
        return self.__returned_date

    @returned_date.setter
    def returned_date(self, returned_date):
        self.__returned_date = returned_date