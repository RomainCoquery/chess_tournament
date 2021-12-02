from chess_tournament.controllers.home_controller import HomePageController
from chess_tournament.models.players import Player
from chess_tournament.models.tournaments import Tournament
from chess_tournament.controllers.player_controller import PlayerController
from chess_tournament.controllers.tournament_controller import TournamentController
import subprocess as sp


class Application:

    routes = {
        "homepage": HomePageController.dispatch,
        "list_player": PlayerController.list,
        "new_player": PlayerController.create,
        "view_player": PlayerController.view,
        "delete_player": PlayerController.delete,
        "edit_player": PlayerController.edit,
        "list_tournament": TournamentController.list,
        "view_tournament": TournamentController.view,
        "new_tournament": TournamentController.create,
        "delete_tournament": TournamentController.delete,
        "edit_tournament": TournamentController.edit
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        player_one = Player(id_=1, first_name='Breton', last_name='Pedro',
                            birthday='18.10.1900', gender='M', rank=20)
        player_two = Player(id_=2, first_name='Raoul', last_name='bernard',
                            birthday='12.10.2020', gender='F', rank=10)
        player_three = Player(id_=3, first_name='baby', last_name='run run',
                              birthday='22.22.2001', gender='M', rank=30)
        player_four = Player(id_=4, first_name='Pepe', last_name='Bo',
                             birthday='04.06.1995', gender='F', rank=40)
        player_five = Player(id_=5, first_name='Pablo', last_name='Picasso',
                             birthday='02.03.2000', gender='M', rank=523)
        player_six = Player(id_=6, first_name='Marc', last_name='Bambi',
                            birthday='01.02.3026', gender='F', rank=235)
        player_seven = Player(id_=7, first_name='Bea', last_name='Beo',
                              birthday='25.12.1782', gender='F', rank=852)
        player_eight = Player(id_=8, first_name='Babe', last_name='Pig',
                              birthday='01.11.2005', gender='M', rank=3)
        tournoi = Tournament(tournament_name='Tournoi', location='Ici',
                             creation_date='16.11.2021', number_of_rounds=4,
                             timer='Blitz', description='test')
        tournoi2 = Tournament(tournament_name='tournoi2', location='Paris',
                              creation_date='12.10.2021',number_of_rounds=4,
                              timer='bullet', description='le grand tournoi des'
                                                          ' débutants en python')
        self.store = {
            "players": [
                player_one, player_two, player_three, player_four, player_five,
                player_six, player_seven, player_eight,
            ],
            "tournaments": [
                tournoi, tournoi2
            ]
        }

    def run(self):
        while not self.exit:
            # Clear the shell output
            sp.call('clear', shell=True)

            # Get the controller method that should handle our current route
            controller_method = self.routes[self.route]

            # Call the controller method, we pass the store and the route's
            # parameters.
            # Every controller should return two things:
            # - the next route to display
            # - the parameters needed for the next route
            next_route, next_params = controller_method(
                self.store, self.route_params
            )

            # set the next route and input
            self.route = next_route
            self.route_params = next_params

            # if the controller returned "quit" then we end the loop
            if next_route == "quit":
                self.exit = True
