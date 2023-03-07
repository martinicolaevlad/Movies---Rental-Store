class Client:

    def __init__(self, client_id, name):
        """

        :param client_id: integer
        :param name: string
        """
        self.__client_id = client_id
        self.__name = name

    @property
    def client_id(self):
        return self.__client_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name