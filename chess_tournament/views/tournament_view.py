from chess_tournament.views.player_view import PlayerView
from constants import NUMBER_OF_ROUNDS

class TournamentView:

    @classmethod
    def display_list(cls, tournaments):
        print("\tTournament_name\tLocation\tCreation_date\tTimer\tDescription")
        for tournament in tournaments:
            cls.display_tournament(tournament)

        print("1. Detail Tournament")
        print("2. New Tournament")
        print("3. Delete tournament")
        print("4. Edit Tournament")
        print("Q. Exit")
        print("H. Homepage")

        choice = input("Choice:")
        extra_info = None

        if choice in ("1", "3", "4"):
            extra_info = input("Enter Tournament Name:")

        return choice, extra_info

    @classmethod
    def create_tournament(cls):
        return {
            "tournament_name": str(input("Enter a tournament name: ")),
            "location": str(input("Enter a location: ")),
            "creation_date": input("Enter creation date DD.MM.YYYY"),
            "timer": str(input("Enter timer 'blitz', 'bullet' or 'coup rapide': ")),
            "description": input("Enter the description: ")
        }

    @classmethod
    def edit_tournament(cls, tournament):
        return {
            "tournament_name": input(f"Enter new Tournament_name "
                                     f" [{tournament.tournament_name}]: "),
            "location": str(input(f"Enter new Location "
                                   f"[{tournament.location}]: ")),
            "creation_date": input(f"Enter a new creation date "
                                   f"[{tournament.creation_date}]: "),
            "timer": str(input(f"Enter new Timer [{tournament.timer}]: ")),
            "description": str(input(f"Enter new description"
                                     f" [{tournament.description}]: "))
        }

    @classmethod
    def detail_tournament(cls, tournament):
        print("\tTournament_name\tLocation\tCreation_date\tTimer\tDescription")
        cls.display_tournament(tournament)
        if len(tournament.players) != 0:
            print("players\n")
            print("\tId\tLast_name\tFirst_name\tBirthday\tGender\tRank\tScore")
            for player in tournament.players:
                PlayerView.display_player(player)
                for rounds in tournament.rounds:
                    cls.display_round(rounds)
                count_round = len(tournament.rounds)
                if count_round == 0:
                    print("1. Start first round")
                elif count_round < NUMBER_OF_ROUNDS:
                    print("2. Start other round")

        print("H. Homepage")
        print("Q. Exit")
        return input("Choice:")

    @classmethod
    def display_tournament(cls, tournament):
        print(f"\t{tournament.tournament_name}\t{tournament.location}\t"
              f"{tournament.creation_date}\t{tournament.timer}\t"
              f"{tournament.description}")

    @classmethod
    def manage_round(cls, rounds):
        cls.display_round(rounds)

        print("set winners match, 1 for player1, 2 for player2, 0 for tie")
        if rounds.matches[0].winner is None:
            print("1. Set winner match 1: ")
        if rounds.matches[1].winner is None:
            print("2. Set winner match 2: ")
        if rounds.matches[2].winner is None:
            print("3. Set winner match 3: ")
        if rounds.matches[3].winner is None:
            print("4. Set winner match 4: ")
        else:
            print("5. End Round")
        return input("choice:")

    @classmethod
    def display_round(cls, rounds):
        print(f"\nName : {rounds.name}")
        print(f"Creation date : {rounds.start_date}")
        print("\nPlayer 1 First name Last name Rank Score VS "
              "Player 2 First name Last name Rank Score\n")
        for index, match in enumerate(rounds.matches, start=1):
            match_player1 = (match.player1.first_name, match.player1.last_name,
                             match.player1.rank, match.player1.score)
            match_player2 = (match.player2.first_name, match.player2.last_name,
                             match.player2.rank, match.player2.score)
            print("Match", index, ":"'\n', "Player 1 :", *match_player1, "VS",
                  "Player 2 :", *match_player2)
