from chess_tournament.controllers.home_controller import HomePageController
from chess_tournament.models.players import PlayerManager
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
        "edit_player": PlayerController.edit,
        "list_tournament": TournamentController.list,
        "new_tournament": TournamentController.create,
        "edit_tournament": TournamentController.edit,
        "detail_tournament": TournamentController.detail,
        "manage_round":TournamentController.manage,
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        all_players = PlayerManager().get_all()
        tournoi = Tournament(name='tournoi', location='Ici',
                             creation_date='16.10.2000', timer='Blitz',
                             description='test')
        tournoi2 = Tournament(name='tournoi p', location='Paris',
                              creation_date='16.10.2000' ,timer='bullet',
                              description='le grand tournoi des débutants'
                                          ' en python')
        self.store = {
            "players": all_players,
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
