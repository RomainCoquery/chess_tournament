class TournamentView:

    @classmethod
    def display_list(cls, tournaments):
        print("\tTournament_name\tLocation\tCreation_date\tNumber_of_rounds\t"
              "Timer\tDescription")
        for tournament in tournaments:
            print(f"\t{tournament.tournament_name}\t{tournament.location}\t"
                  f"{tournament.creation_date}\t{tournament.number_of_rounds}\t"
                  f"{tournament.timer}\t{tournament.description}")

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
    def detail_tournament(cls, tournament):
        print(f"Name: {tournament.tournament_name}")
        print(f"Location: {tournament.location}")
        print(f"Creation_date: {tournament.creation_date}")
        print(f"Timer: {tournament.timer}")
        print(f"Number_of_rounds: {tournament.number_of_rounds}")
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
            "number_of_rounds": input("Enter number of rounds 'default = 4': "),
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
            "number_of_rounds": input(f"Enter new Number_of_rounds"
                         f" [{tournament.number_of_rounds}]: "),
            "timer": str(input(f"Enter new Timer [{tournament.timer}]: ")),
            "description": str(input(f"Enter new description"
                                     f" [{tournament.description}]: "))
        }
