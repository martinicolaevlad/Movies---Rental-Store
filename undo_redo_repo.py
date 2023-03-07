from datetime import date

from src.domain.client import Client
from src.domain.exceptions import NothingToUndo, NothingToRedo
from src.domain.movie import Movie
from src.domain.rental import Rental


class UndoService:

    def __init__(self, client_repo, movie_repo, rental_repo):
        self.__undo_repo = []
        self.__redo_repo = []
        self.__movie_repo = movie_repo
        self.__client_repo = client_repo
        self.__rental_repo = rental_repo

    def add_client(self, client_id, name):
        client = Client(client_id, name)
        self.__undo_repo.append(['client', 'add', client])

    def remove_client(self, client_id):
        client = self.__client_repo.find_by_id(client_id)
        self.__undo_repo.append(['client', 'remove', client])

    def update_client(self, client_id):
        client = self.__client_repo.find_by_id(client_id)
        self.__undo_repo.append(['client', 'update', client])

    def add_movie(self, movie_id, title, description, genre):
        movie = Movie(movie_id, title, description, genre)
        self.__undo_repo.append(['movie', 'add', movie])

    def remove_movie(self, movie_id):
        movie = self.__movie_repo.find_by_id(movie_id)
        self.__undo_repo.append(['movie', 'remove', movie])

    def update_movie(self, movie_id):
        movie = self.__movie_repo.find_by_id(movie_id)
        self.__undo_repo.append(['movie', 'update', movie])

    def rent_movie(self, rental_id, movie_id, client_id, due_day):
        today = date.today()
        current_date = today.strftime('%d/%m/%Y')
        rental = Rental(rental_id, movie_id, client_id, current_date, due_day, 'Not returned yet')
        self.__undo_repo.append(['rental', 'rent', rental])

    def return_movie(self, rental_id):
        rental = self.__rental_repo.find_rental_by_id(rental_id)
        self.__undo_repo.append(['rental', 'return', rental])

    def undo(self, client_service, movie_service, rental_service):
        if len(self.__undo_repo) == 0:
            raise NothingToUndo("There is nothing to undo!")

        last_command_to_undo = self.__undo_repo[-1]

        category = last_command_to_undo[0]
        action = last_command_to_undo[1]
        element = last_command_to_undo[2]
        print(last_command_to_undo)
        if category == 'movie':
            if action == 'add':
                movie_service.remove_movie(element.movie_id)
                self.__redo_repo.append(['movie', 'remove', element])

            elif action == 'remove':
                movie_service.add_movie(element.movie_id, element.title, element.description, element.genre)
                self.__redo_repo.append(['movie', 'add', element])

            elif action == 'update':
                movie_service.update_movie(element.movie_id, element.title, element.description, element.genre)
                self.__redo_repo.append(['movie', 'update', element])

        elif category == 'client':
            if action == 'add':
                client_service.remove_client(element.client_id)
                self.__redo_repo.append(['client', 'remove', element])

            elif action == 'remove':

                client_service.add_client(element.client_id, element.name)
                self.__redo_repo.append(['client', 'add', element])

            elif action == 'update':
                client_service.update_client(element.client_id, element.name)
                self.__redo_repo.append(['client', 'update', element])

        elif category == 'rental':

            if action == 'return':
                rental_service.modify_returned_date_(element.rental_id)
                self.__redo_repo.append(['rental', 'not_returned', element])

            if action == 'rent':
                rental_service.remove_rental(element.rental_id)
                self.__redo_repo.append(['rental', 'remove', element])

            if action == 'remove':
                rental_service.append_rental_(element)
                self.__redo_repo.append(['rental', 'rent', element])

            if action == 'not_returned':
                rental_service.return_movie(element.rental_id)
                self.__redo_repo.append(['rental', 'return', element])

        self.__undo_repo.pop()

    def redo(self, client_service, movie_service, rental_service):
        if len(self.__redo_repo) == 0:
            raise NothingToRedo("There is nothing to redo!")

        last_command_to_redo = self.__redo_repo[-1]

        category = last_command_to_redo[0]
        action = last_command_to_redo[1]
        element = last_command_to_redo[2]
        print(last_command_to_redo)

        if category == 'movie':
            if action == 'add':
                movie_service.remove_movie(element.movie_id)
                self.__undo_repo.append(['movie', 'remove', element])

            elif action == 'remove':
                movie_service.add_movie(element.movie_id, element.title, element.description, element.genre)
                self.__undo_repo.append(['movie', 'add', element])

            elif action == 'update':
                movie_service.update_movie(element.movie_id, element.title, element.description, element.genre)
                self.__undo_repo.append(['movie', 'update', element])

        elif category == 'client':
            if action == 'add':
                client_service.remove_client(element.client_id)
                self.__undo_repo.append(['client', 'remove', element])

            elif action == 'remove':
                client_service.add_client(element.client_id, element.name)
                self.__undo_repo.append(['client', 'add', element])

            elif action == 'update':
                client_service.update_client(element.client_id, element.name)
                self.__undo_repo.append(['client', 'update', element])

        elif category == 'rental':

            if action == 'return':
                rental_service.modify_returned_date_(element.rental_id)
                self.__undo_repo.append(['rental', 'not_returned', element])

            if action == 'rent':
                rental_service.remove_rental(element.rental_id)
                self.__undo_repo.append(['rental', 'remove', element])

            if action == 'remove':
                rental_service.append_rental_(element)
                self.__undo_repo.append(['rental', 'rent', element])

            if action == 'not_returned':
                rental_service.return_movie(element.rental_id)
                self.__undo_repo.append(['rental', 'return', element])

        self.__redo_repo.pop()