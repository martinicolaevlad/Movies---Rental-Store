from src.domain.rental import Rental

import datetime


class RentalRepo:

    def __init__(self, client_repo, movie_repo):

        self.__rental_list = []
        self.__day_counter_list = []
        self.__active_clients = []
        self.__late_rentals = []
        self.__r_movie_list = movie_repo
        self.__r_client_list = client_repo
        tdelta = datetime.timedelta(days=14)

        i = 0

        day = datetime.date(2021, 7, 24)
        due_date = day + tdelta
        returned_date = datetime.date(2021, 9, 24)  # 62 days
        self.add_rental(Rental(3456, self.__r_movie_list.movie_table[i].movie_id, self.__r_client_list.client_table[i].client_id, day, due_date, returned_date))

        i += 1
        day = datetime.date(2021, 6, 23)
        due_date = day + tdelta
        returned_date = datetime.date(2021, 6, 30)  # 7 days
        self.add_rental(Rental(3457, self.__r_movie_list.movie_table[i].movie_id, self.__r_client_list.client_table[i].client_id, day, due_date, returned_date))

        i += 1
        day = datetime.date(2021, 11, 20)
        due_date = day + tdelta     # aprox. 10 days
        self.add_rental(Rental(3458, self.__r_movie_list.movie_table[i].movie_id, self.__r_client_list.client_table[i].client_id, day, due_date, 'Not returned yet.'))

        i += 1
        day = datetime.date(2021, 6, 23)
        due_date = day + tdelta
        returned_date = datetime.date(2021, 6, 29)  # 6 days
        self.add_rental(Rental(3459, self.__r_movie_list.movie_table[i].movie_id, self.__r_client_list.client_table[i-1].client_id, day, due_date, returned_date))

        i += 1
        day = datetime.date(2020, 7, 24)
        due_date = day + tdelta
        returned_date = datetime.date(2021, 7, 24)
        self.add_rental(Rental(3460, self.__r_movie_list.movie_table[i].movie_id, self.__r_client_list.client_table[i].client_id, day, due_date, returned_date))

        i += 1
        day = datetime.date(2021, 4, 23)
        due_date = day + tdelta
        self.add_rental(Rental(3461, self.__r_movie_list.movie_table[i].movie_id, self.__r_client_list.client_table[i].client_id, day, due_date, 'Not returned yet.'))

        i += 1
        day = datetime.date(2021, 10, 20)
        due_date = day + tdelta
        self.add_rental(Rental(3462, self.__r_movie_list.movie_table[i].movie_id, self.__r_client_list.client_table[i].client_id, day, due_date, 'Not returned yet.'))

        i += 1
        day = datetime.date(2021, 6, 23)
        due_date = day + tdelta
        returned_date = datetime.date(2021, 6, 29)
        self.add_rental(Rental(3463, self.__r_movie_list.movie_table[i].movie_id, self.__r_client_list.client_table[i].client_id, day, due_date, returned_date))

    @property
    def rental_table(self):
        return self.__rental_list

    @property
    def most_rented(self):
        return self.__day_counter_list

    @property
    def most_active(self):
        return self.__active_clients

    @property
    def late_rent(self):
        return self.__late_rentals

    def find_rental_by_id(self, rental_id):
        for rental in self.__rental_list:
            if rental.rental_id == int(rental_id):
                return rental



    def add_rental(self, rental):
        """
        Adds a rental.
        :param rental:
        :return:
        """
        self.__rental_list.append(rental)

    def return_movie(self, rental_id):
        """
        It changes the returned date into the current day.
        :param rental_id:
        :return:
        """
        tday = datetime.date.today()
        for x in self.rental_table:
            if int(x.rental_id) == int(rental_id):
                x.returned_date = tday

    def most_rented_movies(self):
        """
        Creates a table which contains the movie's id and the number of days it has been rented.
        :return:
        """
        self.__day_counter_list = []
        rental_list = self.__rental_list
        tday = datetime.date.today()
        for rental in rental_list:

            if rental.returned_date != 'Not returned yet.':
                difference = rental.returned_date - rental.rented_date
                list = [rental.movie_id, difference.days]
                self.__day_counter_list.append(list)
            else:
                difference = tday - rental.rented_date
                list = [rental.movie_id, difference.days]
                self.__day_counter_list.append(list)

        size = lambda day: day[1]
        self.__day_counter_list.sort(key=size, reverse=True)

    def change_id_title(self):
        """
        Replaces the movie's id with their title.
        :return:
        """
        self.most_rented_movies()
        rental_list = self.__day_counter_list
        movie_list = self.__r_movie_list.movie_table
        for rental in rental_list:
            for movie in movie_list:
                if str(rental[0]) == str(movie.movie_id):
                    rental[0] = movie.title

    def most_active_clients(self):
        """
        It creates a new table with two columns. On the first one are the names and on the second one are the number of days that a client has rented a movie.
        :return:
        """
        self.__active_clients = []
        rental_list = self.rental_table
        client_list = self.__r_client_list.client_table
        tday = datetime.date.today()
        for client in client_list:
            ct = 0
            for rental in rental_list:
                if str(client.client_id) == str(rental.client_id):
                    if rental.returned_date != 'Not returned yet.':
                        difference = rental.returned_date - rental.rented_date
                    else:
                        difference = tday - rental.rented_date
                    ct = ct + difference.days
            list = [client.name, ct]
            self.__active_clients.append(list)
        size = lambda day: day[1]
        self.__active_clients.sort(key=size, reverse=True)

    def late_rentals(self):
        """

        :return:
        """
        self.__late_rentals = []
        rental_list = self.rental_table
        movie_list = self.__r_movie_list.movie_table
        tday = datetime.date.today()
        for rental in rental_list:
            for movie in movie_list:
                if rental.movie_id == movie.movie_id:
                    if rental.returned_date == "Not returned yet." and tday > rental.due_date:
                        difference = tday - rental.due_date
                        data = [movie.title, difference.days]
                        self.__late_rentals.append(data)
        size = lambda day: day[1]
        self.__late_rentals.sort(key=size, reverse=True)

    def modify_returned_date(self, rental_id):
        for rental in self.__rental_list:
            if rental.rental_id == rental_id:
                rental.returned_date = 'Not returned yet'

    def remove_rental(self, rental_id):
        result_after_remove = []
        for rental in self.__rental_list:
            if rental.rental_id != rental_id:
                result_after_remove.append(rental)
        self.__rental_list = result_after_remove

    def append_rental(self, rental):
        self.__rental_list.append(rental)