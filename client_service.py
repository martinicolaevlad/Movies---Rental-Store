from src.domain.exceptions import NoClientWithThisId, TheIdMustHave4Digits, IsPositive, IsDigit, IsLetter, \
     IdAlreadyExists

from src.domain.client import Client
from src.repository.client_repo import Client_repo


class Client_service:

    def __init__(self, client_repository):
        self.__client_repo = client_repository

    @property
    def client_list(self):
        return self.__client_repo.client_table

    def verify_client_id(self, client_id):

        for client in self.__client_repo.client_table:
            if client.client_id == int(client_id):
                raise IdAlreadyExists

    @staticmethod
    def verify_isdigit_input(string):

        if not string.isdigit():
            raise IsLetter

    @staticmethod
    def verify_isletter_input(string):

        if string.isdigit():
            raise IsDigit

    @staticmethod
    def verify_ispositive(nr):
        if int(nr) < 0:
            raise IsPositive

    @staticmethod
    def verify_4digits(nr):
        if int(nr) < 1000 or int(nr) >= 10000:
            raise TheIdMustHave4Digits

    def add_client(self, client_id, client_name):
        """
        Adds a client to the repository.
        :param client_id:
        :param client_name:
        :return:
        """
        client = Client(client_id, client_name)
        self.__client_repo.add_client(client)

    def remove_client(self, client_id):
        """
        Removes a client from the repository with an inputed id.
        :param client_id:
        :return:
        """
        x = 0
        for client in self.__client_repo.client_table:
            if int(client_id) == client.client_id:
                self.__client_repo.remove_client(client)
                x = 1
        if x == 0:
            raise NoClientWithThisId

    def update_client(self, client_id, client_name):
        """
        The function updates a client's name, by his ID.
        :param client_id:
        :param client_name:
        :return:
        """

        self.__client_repo.update_client(client_id, client_name)

    def verify_if_client_exist(self, client_id):
        """

        :param client_id:
        :return:
        """
        x = 0
        for client in self.__client_repo.client_table:
            if client_id == str(client.client_id):
                x = 1
        if x == 0:
            raise NoClientWithThisId

