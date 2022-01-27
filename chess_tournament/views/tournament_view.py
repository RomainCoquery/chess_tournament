from constants import NUMBER_PLAYERS


def win(winner, player):
    if winner is None:
        return' '
    if winner is False:
        return'☺  '
    elif winner.id == player.id:
        return'☺  '
    else:
        return' '


class TournamentView:

    @classmethod
    def display_list(cls, tournaments):
        print('--------------------------------------------------------------')
        print("[              List Tournaments                              ]")
        print('--------------------------------------------------------------')
        print("\tName\tLocation\tCreation_date\tTimer\tDescription")
        for tournament in tournaments:
            cls.display_tournament(tournament)

        print("1. Detail Tournament")
        print("2. New Tournament")
        print("H. Homepage")
        print("Q. Exit")

        choice = input("Choice:")
        extra_info = None

        if choice in "1":
            extra_info = input("Enter Tournament Name:")

        return choice, extra_info

    @classmethod
    def create_tournament(cls):
        return {
            "name": str(input("Enter a tournament name: ")),
            "location": str(input("Enter a location: ")),
            "creation_date": input("Enter creation date DD.MM.YYYY: "),
            "timer": str(input("Enter timer 'blitz', 'bullet' or 'coup rapide': ")),
            "description": input("Enter the description: ")
        }

    @classmethod
    def detail_tournament(cls, tournament):
        print('--------------------------------------------------------------')
        print("[              Detail Tournament                             ]")
        print('--------------------------------------------------------------')
        print("\tName\tLocation\tCreation_date\tTimer\tDescription")
        cls.display_tournament(tournament)
        if len(tournament.players) >= NUMBER_PLAYERS:
            print("players\n")
            print("\tId\tFull_name\tBirthday\tGender\tRank")
            for player in tournament.players:
                cls.display_player(player)
            for rounds in tournament.rounds:
                cls.display_round(rounds)

        print("L. List tournament")
        print("H. Homepage")
        print("Q. Exit")
        return input("Choice:")

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

        choice = input("Choice:")
        extra_info = None

        if choice in ("1", "2", "3", "4"):
            extra_info = int(input("Enter Winner:"))

        return choice, extra_info

    @classmethod
    def finished_tournament(cls, tournament):
        print('--------------------------------------------------------------')
        print("[              Resume Tournament                             ]")
        print('--------------------------------------------------------------')
        print("\tName\tLocation\tCreation_date\tTimer\tDescription")
        cls.display_tournament(tournament)
        print("players\n")
        print("\tId\tFull_name\tBirthday\tGender\tRank\tScore")
        for k, v in tournament.players_scores.items():
            player = next(p for p in tournament.players if str(p.id) == str(k))
            score = v
            print(f"\t{player.id}\t{player.full_name()}"
                  f"\t{player.birthday}\t{player.gender}\t{player.rank}\t{score}")
        for rounds in tournament.rounds:
            cls.display_round(rounds)

        print("L. List tournament")
        print("H. Homepage")
        print("Q. Exit")
        return input("Choice:")

    @classmethod
    def display_tournament(cls, tournament):
        print(f"\t{tournament.name}\t{tournament.location}\t"
              f"{tournament.creation_date}\t{tournament.timer}\t"
              f"{tournament.description}")

    @classmethod
    def display_round(cls, rounds):
        print('--------------------------------------------------------------')
        print(f"[               Name : {rounds.name}                        ]")
        print('--------------------------------------------------------------')
        print(f"Creation date : {rounds.start_date}")
        print(f"End date : {rounds.end_date}")
        print("\nPlayer 1 Full name Rank Winner VS "
              "Player 2 Full name Rank Winner\n")
        for index, match in enumerate(rounds.matches, start=1):
            match_player1 = (match.player1.full_name(),
                             match.player1.rank, win(match.winner, match.player1))
            match_player2 = (match.player2.full_name(),
                             match.player2.rank, win(match.winner, match.player2))
            print("Match", index, ":"'\n', "Player 1 :", *match_player1, "VS",
                  "Player 2 :", *match_player2)

    @classmethod
    def display_player(cls, player):
        print(f"\t{player.id}\t{player.full_name()}"
              f"\t{player.birthday}\t{player.gender}\t{player.rank}\t")
