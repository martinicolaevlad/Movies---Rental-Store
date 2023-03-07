from src.repository.client_repo import Client_repo
from src.repository.undo_redo_repo import UndoService
from src.services.client_service import Client_service

from src.repository.movie_repo import Movie_repo
from src.services.movie_service import Movie_service

from src.repository.rental_repo import RentalRepo
from src.services.rental_service import RentalService

from src.ui.ui import UI

if __name__ == "__main__":

    client_repo = Client_repo()
    client_service = Client_service(client_repo)

    movie_repo = Movie_repo()
    movie_service = Movie_service(movie_repo)

    rental_repo = RentalRepo(client_repo, movie_repo)
    rental_service = RentalService(rental_repo)

    undo_redo = UndoService(client_repo, movie_repo, rental_repo)

    ui = UI(client_service, movie_service, rental_service, undo_redo)

    ui.start()
