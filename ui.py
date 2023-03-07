from src.domain.exceptions import NoClientWithThisId, TheIdMustHave4Digits, IsPositive, IsDigit, IsLetter, \
    IdAlreadyExists, NoMovieWithThisId, LateReturn, WrongAnswer, NoRentalWithThisId, NoItemMatching, NothingToUndo, \
    NothingToRedo
from src.services.client_service import Client_service
from src.services.movie_service import Movie_service
from src.services.rental_service import RentalService
import datetime


class UI:

    def __init__(self, c_list, m_list, r_list, undo_redo):

        self.__c_list = c_list
        self.__m_list = m_list
        self.__r_list = r_list
        self.__undo_redo = undo_redo

        self.__menu = {
            "1": self.ui_list_clients,
            "2": self.ui_add_client,
            "3": self.ui_remove_client,
            "4": self.ui_update_client,
            "5": self.ui_list_movies,
            "6": self.ui_add_movie,
            "7": self.ui_remove_movie,
            "8": self.ui_update_movie,
            "9": self.ui_list_rentals,
            "10": self.ui_add_rental,
            "11": self.ui_return_movie,
            "12": self.ui_search_key_word,
            "13": self.ui_most_rented_movies,
            "14": self.ui_most_active_clients,
            "15": self.ui_late_rentals,
            "16": self.undo,
            "17": self.redo

        }

    @staticmethod
    def prRed(skk):
        return "\033[91m {}\033[00m".format(skk)

    @staticmethod
    def prLightPurple(skk):
        return "\033[94m {}\033[00m".format(skk)


    def start(self):



        while True:
            print(UI.prLightPurple("""
        ### MENU ###
        
        ### CLIENTS ###     ### MOVIES ###      ### RENTALS ###         ### STATISTICS ###
        1. list clients     5. list movies      9. list all rentals     13. most rented movies
        2. add a client     6. add movie        10. rent a movie        14. most active clients
        3. remove client    7. remove movie     11. return a movie      15. late rentals
        4. update client    8. update movie     12. search a key-word   
        
                
        16. undo    17. redo    0. exit
        """ ))
            option = input(UI.prLightPurple("Enter an option: ")).strip()
            if option == '0':
                return False
            else:
                self.__menu[option]()

    def ui_list_clients(self):

        clients_list = self.__c_list.client_list
        print("")
        print(UI.prLightPurple("\t\tTHE LIST OF CLIENTS:"))
        print("")
        for x in clients_list:
            print(UI.prLightPurple("client's id:"), x.client_id, UI.prLightPurple(" client's name:"), x.name)


    def ui_add_client(self):

        print('Enter the:')
        try:
            client_id = input('\t\tCLIENT ID:').strip()
            self.__c_list.verify_client_id(client_id)
            Client_service.verify_isdigit_input(client_id)
            Client_service.verify_ispositive(client_id)
            Client_service.verify_4digits(client_id)

            client_name = input('\t\tCLIENT NAME:')
            Client_service.verify_isletter_input(client_name)

            self.__c_list.add_client(int(client_id), client_name)
            self.__undo_redo.add_client(client_id, client_name)
        except TheIdMustHave4Digits:
            print(UI.prRed("The id must contain four digits."))
        except IsPositive:
            print(UI.prRed("The id can't be negative."))
        except IsDigit:
            print(UI.prRed("The name can't contain digits."))
        except IsLetter:
            print(UI.prRed("The id can't contain letters."))
        except IdAlreadyExists:
            print(UI.prRed("A client with this id already exists."))

    def ui_remove_client(self):
        try:
            client_id = input("Enter the client's id:")
            Client_service.verify_isdigit_input(client_id)
            self.__undo_redo.remove_client(client_id)
            self.__c_list.remove_client(client_id)

        except NoClientWithThisId:
            print(UI.prRed("There is no client with this id in the list."))

    def ui_update_client(self):
        try:
            client_id = input("Enter the id:")
            self.__c_list.verify_if_client_exist(client_id)
            client_name = input("Enter the name:")
            self.__c_list.update_client(client_id, client_name)
            self.__undo_redo.update_client(client_id)
        except NoClientWithThisId:
            print(UI.prRed("There is no client with this id in the list."))

    def ui_list_movies(self):

        movie_list = self.__m_list.movie_list
        print("")
        print(UI.prLightPurple("\t\tTHE LIST OF MOVIES:"))
        print("")
        for x in movie_list:
            print(UI.prLightPurple("movies's id:"), x.movie_id, UI.prLightPurple(" title:"), x.title, UI.prLightPurple("description:"), x.description, UI.prLightPurple("genre:"), x.genre)

    def ui_add_movie(self):
        try:
            movie_id = input("Enter the movie's id (must have 4 digits):")
            self.__m_list.verify_movie_id(movie_id)
            Movie_service.verify_isdigit_input(movie_id)
            Movie_service.verify_4digits(movie_id)

            title = input("Enter the title:")

            description = input("Enter the description:")

            genre = input("Enter the genre:")

            self.__m_list.add_movie(int(movie_id), title, description, genre)
            self.__undo_redo.add_movie(int(movie_id), title, description, genre)
        except IdAlreadyExists:
            print(UI.prRed("A movie with this id already exists."))
        except IsLetter:
            print(UI.prRed("The id can't contain letters."))
        except TheIdMustHave4Digits:
            print(UI.prRed("The id must contain four digits."))

    def ui_remove_movie(self):
        try:
            movie_id = input("Enter the movie's id:")
            self.__m_list.verify_if_movie_exist(movie_id)
            self.__m_list.remove_movie(movie_id)
            self.__undo_redo.remove_movie(movie_id)
        except NoMovieWithThisId:
            print(UI.prRed("There is no movie with this id."))

    def ui_update_movie(self):
        try:
            movie_id = input("Enter the movie's id:")
            self.__m_list.verify_if_movie_exist(movie_id)
            Movie_service.verify_isdigit_input(movie_id)
            title = input("New title:")
            description = input("New description:")
            genre = input("New genre:")

            self.__m_list.update_movie(movie_id, title, description, genre)
            self.__undo_redo.update_movie(movie_id)
        except NoMovieWithThisId:
            print(UI.prRed("There is no movie with this id."))

    def ui_list_rentals(self):

        rental_table = self.__r_list.rental_list
        print("")
        print(UI.prLightPurple("\t\tTHE RENTALS LIST:"))
        print("")
        r_id = UI.prLightPurple("Rental's ID:")
        m_id = UI.prLightPurple("Movie's ID:")
        c_id = UI.prLightPurple("Client's ID:")
        date_1 = UI.prLightPurple("Rental date:")
        date_2 = UI.prLightPurple("Due date:")
        date_3 = UI.prLightPurple("Return date:")
        for x in rental_table:
            print(r_id, x.rental_id, m_id, x.movie_id, c_id, x.client_id, date_1, x.rented_date, date_2, x.due_date, date_3, x.returned_date)

    def ui_add_rental(self):

            tday = datetime.date.today()
            tdelta = datetime.timedelta(days=14)
            due_d = tday + tdelta
            new_client = input("Are you a new client? (yes/no): ")
            try:
                if new_client == 'yes':
                    print('Enter your new:')
                    try:
                        client_id = input('\t\tCLIENT ID:').strip()
                        self.__c_list.verify_client_id(client_id)
                        Client_service.verify_isdigit_input(client_id)
                        Client_service.verify_ispositive(client_id)
                        Client_service.verify_4digits(client_id)
                        client_name = input('\t\tCLIENT NAME:')
                        Client_service.verify_isletter_input(client_name)
                        self.__c_list.add_client(int(client_id), client_name)

                        movie_id = input("Enter the movie's id that you wish to rent: ")
                        self.__m_list.verify_if_movie_exist(movie_id)

                        rental_id = input("Your rental id: ")
                        self.__r_list.verify_rental_id(rental_id)

                        self.__r_list.add_rental(rental_id, movie_id, client_id, tday, due_d, 'Not returned yet.')
                        self.__undo_redo.rent_movie(rental_id, movie_id, client_id, due_d)
                    except TheIdMustHave4Digits:
                        print(UI.prRed("The id must contain four digits."))
                    except IsPositive:
                        print(UI.prRed("The id can't be negative."))
                    except IsDigit:
                        print(UI.prRed("The name can't contain digits."))
                    except IsLetter:
                        print(UI.prRed("The id can't contain letters."))
                    except IdAlreadyExists:
                        print(UI.prRed("A client with this id already exists."))
                    except NoMovieWithThisId:
                        print(UI.prRed("There is no movie with this id."))


                elif new_client == 'no':
                    try:
                        client_id = input("Please enter your personal ID: ")
                        RentalService.verify_isdigit_input(client_id)
                        self.__c_list.verify_if_client_exist(client_id)
                        self.__r_list.verify_past_rented_movies(client_id)

                        movie_id = input("Enter the movie's id that you wish to rent: ")
                        RentalService.verify_isdigit_input(movie_id)
                        self.__m_list.verify_if_movie_exist(movie_id)

                        rental_id = input("Your rental id: ")
                        self.__r_list.verify_rental_id(rental_id)
                        RentalService.verify_isdigit_input(rental_id)
                        Client_service.verify_4digits(rental_id)

                        self.__r_list.add_rental(rental_id, movie_id, client_id, tday, due_d, 'Not returned yet.')
                        self.__undo_redo.rent_movie(rental_id, movie_id, client_id, due_d)
                    except NoClientWithThisId:
                        print(UI.prRed("There is no registered client with this id."))
                    except LateReturn:
                        print(UI.prRed("Sorry, you can't rent movies from us until you return the ones that you have."))
                    except IdAlreadyExists:
                        print(UI.prRed("A rental with this id already exists."))
                    except NoMovieWithThisId:
                        print(UI.prRed("There is no movie with this id."))
                    except IsLetter:
                        print(UI.prRed("The ID can't contain letters."))
                    except TheIdMustHave4Digits:
                        print(UI.prRed("The id must contain four digits."))

                else:
                    raise WrongAnswer

            except WrongAnswer:
                print(UI.prRed("Wrong answer."))

    def ui_return_movie(self):
        try:
            rental_id = input("Enter your rental's ID:")
            self.__r_list.verify_if_rental_exist(rental_id)
            self.__r_list.return_movie(rental_id)
            self.__undo_redo.return_movie(rental_id)
        except NoRentalWithThisId:
            print(UI.prRed("There is no rental with this id."))

    def ui_search_key_word(self):

            try:
                keyword = input("Enter the key-word:")
                a = 0

                client_list = self.__c_list.client_list
                for i in client_list:
                    if keyword in str(i.client_id) or keyword.lower() in i.name.lower():
                        print(UI.prLightPurple("client's id:"), i.client_id, UI.prLightPurple(" client's name:"), i.name)
                        a = 1


                movie_list = self.__m_list.movie_list
                for i in movie_list:
                    if keyword in str(i.movie_id) or keyword.lower() in i.title.lower() or keyword.lower() in i.description.lower() or keyword.lower() in i.genre.lower():
                        print(UI.prLightPurple("movies's id:"), i.movie_id, UI.prLightPurple(" title:"), i.title, UI.prLightPurple("description:"), i.description, UI.prLightPurple("genre:"), i.genre)
                        a = 1

                if a == 0:
                    raise NoItemMatching

            except NoItemMatching:
                print(UI.prRed("There is no item matching your key-word."))

    def ui_most_rented_movies(self):

        self.__r_list.most_rented_movies()
        day_counter_table = self.__r_list.most_rent
        for line in day_counter_table:
            print(UI.prLightPurple("Movie's title:"), line[0], UI.prLightPurple("Days rented:"), line[1])

    def ui_most_active_clients(self):
        self.__r_list.most_active_clients()
        day_counter_table = self.__r_list.most_act
        for line in day_counter_table:
            print(UI.prLightPurple("Client's name:"), line[0], UI.prLightPurple("Days rented:"), line[1])

    def ui_late_rentals(self):
        self.__r_list.late_rentals()
        day_counter_table = self.__r_list.late_rental
        for line in day_counter_table:
            print(UI.prLightPurple("Movie's title:"), line[0], UI.prLightPurple("Days late:"), line[1])

    def undo(self):
        try:
            self.__undo_redo.undo(self.__c_list, self.__m_list, self.__r_list)
        except NothingToUndo:
            print(UI.prRed("There is nothing to undo!"))

    def redo(self):
        try:
            self.__undo_redo.redo(self.__c_list, self.__m_list, self.__r_list)
        except NothingToRedo:
            print(UI.prRed("There is nothing to redo!"))