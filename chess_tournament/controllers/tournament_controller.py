from chess_tournament.models.tournaments import Tournament
from chess_tournament.views.tournament_view import TournamentView
from chess_tournament.views.player_view import PlayerView
from constants import NUMBER_PLAYERS

class TournamentController:

    @classmethod
    def list(cls, store, route_params=None):
        choice, tournament_name = (TournamentView.display_list
                                   (store["tournaments"]))
        if choice == "1":
            return "view_tournament", tournament_name
        elif choice == "2":
            return "new_tournament", None
        elif choice == "3":
            return "delete_tournament", tournament_name
        elif choice == "4":
            return "edit_tournament", tournament_name
        elif choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None
        else:
            raise Exception("invalid choice")

    @classmethod
    def create(cls, store, route_params=None):
        # call the view that will return us a dict with the new tournament info
        data = TournamentView.create_tournament()
        # You could specify each argument
        # but it's easier to use `**` to pass the arguments
        tournament = Tournament(**data)
        if tournament.validate() and len(store["players"]) >= NUMBER_PLAYERS:
            # we add the tournament to the store
            store["tournaments"].append(tournament)
            data_player = PlayerView.select_list(store["players"])
            list_player = store["players"]
            for player_id in data_player:
                player = None
                for p in list_player:
                    if p.id_ == player_id:
                        player = p
                        break
                if player:
                    tournament.players.append(player)
                else:
                    print("Player not found")
                    input("press ENTER key to continue..")
                    return "homepage", None
        else:
            print("Error, Data for tournament are wrong!")
            input("press ENTER key to continue..")
            return "list_tournament", None

        return "detail_tournament", tournament.tournament_name

    @classmethod
    def view(cls, store, route_params):
        """
        Display one single tournament, the route_params correspond to the
        tournament name we want to display
        """
        try:
            # search the tournament on the store
            tournament = next(t for t in store["tournaments"]
                          if t.tournament_name == route_params)
            # we pass the tournament to the view that will display the tournament
            # info and the next options
            choice = TournamentView.view_tournament(tournament)
            if choice.lower() == "q":
                return "quit", None
            elif choice.lower() == "h":
                return "homepage", None
        except StopIteration:
            print("No tournament with this name")
            input("press ENTER key to continue..")
            return "list_tournament", None

    @classmethod
    def delete(cls, store, route_params):
        count_tournaments = len(store["tournaments"])
        # remove the tournament from the store
        store["tournaments"] = [t for t in store["tournaments"]
                            if t.tournament_name != route_params]
        if count_tournaments == len(store["tournaments"]):
            print("No tournament with this name")
            input("press ENTER key to continue..")
        return "list_tournament", None

    @classmethod
    def edit(cls, store, route_params):
        tournament = next(t for t in store["tournaments"] if t.tournament_name
                          == route_params)
        data = TournamentView.edit_tournament(tournament)
        tournament.edit(**data)
        return "list_tournament", None

    @classmethod
    def detail(cls, store, route_params):
        tournament = next(t for t in store["tournaments"]
                          if t.tournament_name == route_params)
        choice = TournamentView.detail_tournament(tournament)

        if choice == "1":
            Tournament.create_first_round(tournament)
            return "manage_tournament", tournament.tournament_name
        elif choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None

    @classmethod
    def manage(cls, store, route_params):
        tournament = next(t for t in store["tournaments"]
                          if t.tournament_name == route_params)
        choice = TournamentView.manage_tournament(tournament)


        if choice.lower() == "q":
            return "quit", None
        elif choice.lower() == "h":
            return "homepage", None