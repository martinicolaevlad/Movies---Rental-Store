from src.domain.client import Client

import random


class Client_repo:

    def __init__(self):
        self.__client_list = []

        names = ['Andrei', 'David', 'Alexandru', 'Gabriel', 'Mihai', 'Cristian', 'Ștefan', 'Maria', 'Elena', 'Ioana', 'Andreea', 'Sofia', 'Alexandra', 'Antonia', 'Daria', 'Ana', 'Gabriela', 'Oliver', 'George', 'Arthur', 'Noah', 'Muhammad', 'Leo', 'Oscar']
        picked_names = random.choices(names, k=20)

        possible_id = list(range(1000, 10000))
        get_id = random.sample(possible_id, k=20)

        for i in range(20):
            client = Client(get_id[i], picked_names[i])
            self.add_client(client)

        client = Client(1111, 'test')
        self.add_client(client)

    @property
    def client_table(self):
        return self.__client_list

    def find_by_id(self, client_id):
        client_table = self.__client_list
        for c in client_table:
            if c.client_id == int(client_id):
                return c

    def add_client(self, client):
        """
        Adds a client to the list.
        :param client:
        :return:
        """
        self.__client_list.append(client)

    def remove_client(self, client):
        """
        Removes a client from the list.
        :param client:
        :return:
        """
        del self.__client_list[self.__client_list.index(client)]

    def update_client(self, client_id, client_name):
        """
        Updates a client's name by his id.
        :param client_id:
        :param client_name:
        :return:
        """
        for client in self.__client_list:
            if int(client_id) == client.client_id:
                client.name = client_name
