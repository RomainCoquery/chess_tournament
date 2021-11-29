class PlayerView:

    @classmethod
    def display_list(cls, players):
        print("\tId\tLast_name\tFirst_name\tBirthday\tGender\tRank")
        for player in players:
            print(f"\t{player.id_}\t{player.last_name}\t{player.first_name}\t"
                  f"{player.birthday}\t{player.gender}\t{player.rank}")

        print("1. View Player")
        print("2. New Player")
        print("3. Delete Player")
        print("4. Edit Player")
        print("Q. Exit")
        print("H. Homepage")

        choice = input("Choice:")
        extra_info = None

        if choice in ("1", "3", "4"):
            extra_info = int(input("Enter Player Id:"))

        return choice, extra_info

    @classmethod
    def detail_player(cls, player):
        print(f"Id: {player.id_}")
        print(f"Last_name: {player.last_name}")
        print(f"First_name: {player.first_name}")
        print(f"Birthday: {player.birthday}")
        print(f"Gender: {player.gender}")
        print(f"Rank: {player.rank}")

        print("Q. Exit")
        print("H. Homepage")
        return input("Choice:")

    @classmethod
    def create_player(cls):
        return {
            "id_": int(input("Enter an Id: ")),
            "last_name": str(input("Enter a Last_name: ")),
            "first_name": str(input("Enter a First_name: ")),
            "birthday": input("Enter date of birth 'DD.MM.YYYY': "),
            "gender": str(input("Enter Gender: ")),
            "rank": int(input("Enter Rank: "))
        }

    @classmethod
    def edit_player(cls, player):
        return {
            "id_": int(input(f"Enter new Id [{player.id_}]: ")),
            "last_name": str(input(f"Enter new Last_name "
                                   f"[{player.last_name}]: ")),
            "first_name": str(input(f"Enter new First_name "
                                   f"[{player.first_name}]: ")),
            "birthday": input(f"Enter new date of birth 'DD.MM.YYYY'"
                         f" [{player.birthday}]: "),
            "gender": str(input(f"Enter new gender [{player.gender}]: ")),
            "rank": str(input(f"Enter new Rank [{player.rank}]: "))
        }
