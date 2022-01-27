from datetime import datetime
from chess_tournament.models.tournaments import Tournament, TournamentManager
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
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "q":
            return "quit", None
        else:
            print("invalid value")
            return "list_tournament"

    @classmethod
    def create(cls, store, route_params=None):
        # call the view that will return us a dict with the new tournament info
        data = TournamentView.create_tournament()
        # You could specify each argument
        # but it's easier to use `**` to pass the arguments
        tournament = Tournament(**data)
        if tournament.validate() and len(store["players"]) >= NUMBER_PLAYERS:
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
        # we add the tournament to the store
        store["tournaments"].append(tournament)
        TournamentManager().create_tournament(tournament)
        return "detail_tournament", tournament.name

    @classmethod
    def detail(cls, store, route_params):
        tournament = next(t for t in store["tournaments"] if t.name == route_params)
        if tournament.finished_tournament():
            return "finished", tournament.name
        if not tournament.rounds:
            Tournament.create_first_round(tournament)
            return "manage_round", (tournament.rounds[0], tournament)
        if tournament.rounds[-1].finished_rounds() and not tournament.finished_tournament():
            Tournament.start_other_round(tournament)
            return "manage_round", (tournament.rounds[len(tournament.rounds) - 1], tournament)

        choice = TournamentView.detail_tournament(tournament)
        TournamentManager().edit_tournament(tournament)

        if choice.lower() == "l":
            return "list_tournament", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "q":
            return "quit", None

        return "list_tournament", None

    @classmethod
    def manage(cls, store, route_params):
        rounds, tournament = route_params
        choice, extra_info = TournamentView.manage_round(rounds)
        if choice == "1":
            tournament.score_management(extra_info, rounds.matches[0])
            return "manage_round", (rounds, tournament)
        elif choice == "2":
            tournament.score_management(extra_info, rounds.matches[1])
            return "manage_round", (rounds, tournament)
        elif choice == "3":
            tournament.score_management(extra_info, rounds.matches[2])
            return "manage_round", (rounds, tournament)
        elif choice == "4":
            tournament.score_management(extra_info, rounds.matches[3])
            return "manage_round", (rounds, tournament)
        elif choice == "5":
            rounds.end_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            return "detail_tournament", tournament.name

    @classmethod
    def finished(cls, store, route_params):
        tournament = next(t for t in store["tournaments"] if t.name == route_params)
        choice = TournamentView.finished_tournament(tournament)
        TournamentManager().edit_tournament(tournament)

        if choice.lower() == "l":
            return "list_tournament", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "q":
            return "quit", None

        return "list_tournament", None
