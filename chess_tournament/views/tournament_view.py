class TournamentView:

    @classmethod
    def display_list(cls, tournaments):
        print("\tTournament_name\tLocation\tCreation_date\tTimer\tDescription")
        for tournament in tournaments:
            print(f"\t{tournament.tournament_name}\t{tournament.location}\t"
                  f"{tournament.creation_date}\t{tournament.timer}\t"
                  f"{tournament.description}")

        print("1. View Tournament")
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
    def view_tournament(cls, tournament):
        print(f"Name: {tournament.tournament_name}")
        print(f"Location: {tournament.location}")
        print(f"Creation_date: {tournament.creation_date}")
        print(f"Timer: {tournament.timer}")
        print(f"Description: {tournament.description}")

        print("Q. Exit")
        print("H. Homepage")
        return input("Choice:")

    @classmethod
    def create_tournament(cls):
        return {
            "tournament_name": str(input("Enter a tournament name: ")),
            "location": str(input("Enter a location: ")),
            "creation_date": input("Enter the date: "),
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
            "creation_date": input(f"Enter new Creation_date "
                                   f"[{tournament.creation_date}]: "),
            "timer": str(input(f"Enter new Timer [{tournament.timer}]: ")),
            "description": str(input(f"Enter new description"
                                     f" [{tournament.description}]: "))
        }

    @classmethod
    def detail_tournament(cls, tournament):
        print(f"Name: {tournament.tournament_name}")
        print(f"Location: {tournament.location}")
        print(f"Creation_date: {tournament.creation_date}")
        print(f"Timer: {tournament.timer}")
        print(f"Description: {tournament.description}\n")

        print("players\n")
        print("\tId\tLast_name\tFirst_name\tBirthday\tGender\tRank\tScore")
        for player in tournament.players:
            print(f"\t{player.id_}\t{player.last_name}\t{player.first_name}\t"
                  f"{player.birthday}\t{player.gender}\t{player.rank}\t"
                  f"{player.score}")

        count_round = len(tournament.rounds)

        print(f"Round: {count_round}\n")

        print("1. Start first round")
        print("2. Start other round")
        print("Q. Exit")
        print("H. Homepage")
        return input("Choice:")

    @classmethod
    def manage_round(cls, rounds):
        print(f"Name : {rounds.name}")
        print(f"Creation date : {rounds.start_date}")

        print("\nPlayer 1 First name Last name Rank Score VS "
              "Player 2 First name Last name Rank Score")
        for index, match in enumerate(rounds.matches, start=1):
            match_player1 = (match.player1.first_name, match.player1.last_name,
                             match.player1.rank, match.player1.score)
            match_player2 = (match.player2.first_name, match.player2.last_name,
                             match.player2.rank, match.player2.score)
            print("Match", index, ":"'\n', "Player 1 :", *match_player1, "VS",
                  "Player 2 :", *match_player2)

        print("set winners match, 1 for player1, 2 for player2, 0 for tie")
        print("1. Set winner match 1: ")
        print("2. Set winner match 2: ")
        print("3. Set winner match 3: ")
        print("4. Set winner match 4: ")
        print("5. End Round")
        print("Q. Exit")
        print("H. Homepage")
        return input("Choice:")
