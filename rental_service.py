from src.domain.exceptions import IdAlreadyExists, LateReturn, NoRentalWithThisId, IsLetter
from src.domain.rental import Rental

import datetime


class RentalService:

    def __init__(self, rental_repository):
        self.__rental_repo = rental_repository

    @property
    def rental_list(self):
        return self.__rental_repo.rental_table

    @property
    def most_rent(self):
        return self.__rental_repo.most_rented

    @property
    def most_act(self):
        return self.__rental_repo.most_active

    @property
    def late_rental(self):
        return self.__rental_repo.late_rent

    def add_rental(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date):
        """

        :param rental_id:
        :param movie_id:
        :param client_id:
        :param rented_date:
        :param due_date:
        :param returned_date:
        :return:
        """
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__rental_repo.add_rental(rental)

    def verify_rental_id(self, rental_id):

        for rental in self.__rental_repo.rental_table:
            if str(rental.rental_id) == rental_id:
                raise IdAlreadyExists

    def verify_if_rental_exist(self, rental_id):
        x = 0
        for rental in self.__rental_repo.rental_table:
            if int(rental_id) == int(rental.rental_id):
                x = 1
        if x == 0:
            raise NoRentalWithThisId

    def verify_past_rented_movies(self, client_id):

        for rental in self.__rental_repo.rental_table:
            if rental.client_id == int(client_id):
                RentalService.verify_past_dates(rental)

    @staticmethod
    def verify_past_dates(rental):

        tday = datetime.date.today()
        if rental.returned_date == "Not returned yet.":
            if rental.due_date < tday:
                raise LateReturn

    def return_movie(self, rental_id):
        """

        :param rental_id:
        :return:
        """
        self.__rental_repo.return_movie(rental_id)

    @staticmethod
    def verify_isdigit_input(string):

        if not string.isdigit():
            raise IsLetter

    def search_key_word(self, word):
        """

        :param word:
        :return:
        """
        if any(word in s for s in self.__rental_repo.rental_table):
            return self.__rental_repo.rental_table.index(word)

    def most_rented_movies(self):
        """
        Calls the function from the repo.
        :return:
        """
        self.__rental_repo.change_id_title()

    def most_active_clients(self):
        """
        Calls the function from the repo.
        :return:
        """
        self.__rental_repo.most_active_clients()

    def late_rentals(self):
        """
        Calls the function from the repo.
        :return:
        """
        self.__rental_repo.late_rentals()

    def modify_returned_date_(self, rental_id):
        """

        :param rental_id:
        :return:
        """
        self.__rental_repo.modify_returned_date(rental_id)

    def remove_rental(self, rental_id):
        """

        :param rental_id:
        :return:
        """
        self.__rental_repo.remove_rental(rental_id)

    def append_rental_(self, rental):
        self.__rental_repo.append_rental(rental)
