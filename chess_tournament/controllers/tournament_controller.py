from chess_tournament.models.tournaments import Tournament, TournamentManager
from chess_tournament.models.matchs import Match
from chess_tournament.views.tournament_view import TournamentView
from chess_tournament.views.player_view import PlayerView
from constants import NUMBER_PLAYERS

class TournamentController:

    @classmethod
    def list(cls, store, route_params=None):
        choice, tournament_name = (TournamentView.display_list
                                   (store["tournaments"]))
        if choice == "1":
            return "detail_tournament", tournament_name
        elif choice == "2":
            return "new_tournament", None
        elif choice == "3":
            return "edit_tournament", tournament_name
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "q":
            return "quit", None
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
            TournamentManager().create_tournament(tournament)
            data_player = PlayerView.select_list(store["players"])
            for player_id in data_player:
                player = next(p for p in store["players"] if p.id == player_id)
                if player:
                    tournament.players.append(player)
                else:
                    print("Player not found")
                    input("press ENTER key to continue..")
                    return "homepage", None
        else:
            print("Error, tournament data are wrong!")
            input("press ENTER key to continue..")
            return "list_tournament", None

        return "detail_tournament", tournament.name

    @classmethod
    def detail(cls, store, route_params):
        tournament = next(t for t in store["tournaments"]
                          if t.name == route_params)
        choice = TournamentView.detail_tournament(tournament)

        if choice == "1":
            Tournament.create_first_round(tournament)
            return "manage_round", (tournament.rounds[0],
                                    tournament)
        elif choice == "2":
            Tournament.start_other_round(tournament)
            return "manage_round", (tournament.rounds
                                    [len(tournament.rounds) - 1],
                                    tournament)
        elif choice.lower() == "l":
            return  "list_tournament", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "q":
            return "quit", None

    @classmethod
    def edit(cls, store, route_params):
        tournament = next(t for t in store["tournaments"] if t.name
                          == route_params)
        data = TournamentView.edit_tournament(tournament)
        tournament.edit(**data)
        return "list_tournament", None

    @classmethod
    def manage(cls, store, route_params):
        rounds, tournament =  route_params
        choice = TournamentView.manage_round(rounds)
        if choice == "1":
            Match.set_winner(rounds.matches[0],
                             winner=int(input(f"enter winner: ")))
            return "manage_round", (rounds, tournament)
        elif choice == "2":
            Match.set_winner(rounds.matches[1],
                             winner=int(input(f"enter winner: ")))
            return "manage_round", (rounds, tournament)
        elif choice == "3":
            Match.set_winner(rounds.matches[2],
                             winner=int(input(f"enter winner: ")))
            return "manage_round", (rounds, tournament)
        elif choice == "4":
            Match.set_winner(rounds.matches[3],
                             winner=int(input(f"enter winner: ")))
            return "manage_round", (rounds, tournament)
        elif choice == "5":
            return "detail_tournament", tournament.name
