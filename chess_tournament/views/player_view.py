class PlayerView:

    @classmethod
    def display_list(cls, players):
        print('--------------------------------------------------------------')
        print("[                   List players                             ]")
        print('--------------------------------------------------------------')
        print("\tId\tFull_name\tBirthday\tGender\tRank")
        for player in players:
            cls.display_player(player)

        print("1. View Player")
        print("2. New Player")
        print("3. Edit Player")
        print("4. Sort players by last_name")
        print("5. Sort players by rank")
        print("H. Homepage")
        print("Q. Exit")

        choice = input("Choice:")
        extra_info = None

        if choice in ("1", "3"):
            extra_info = int(input("Enter Player Id:"))

        return choice, extra_info

    @classmethod
    def view_player(cls, player):
        print('--------------------------------------------------------------')
        print("[                   View player                              ]")
        print('--------------------------------------------------------------')
        print("\tId\tFull_name\tBirthday\tGender\tRank")
        cls.display_player(player)

        print("L. List player")
        print("H. Homepage")
        print("Q. Exit")

        return input("Choice:")

    @classmethod
    def create_player(cls):
        return {
            "id": int(input("Enter an Id: ")),
            "last_name": str(input("Enter a Last_name: ")),
            "first_name": str(input("Enter a First_name: ")),
            "birthday": input("Enter date of birth 'DD.MM.YYYY': "),
            "gender": str(input("Enter Gender: ")),
            "rank": int(input("Enter Rank: "))
        }

    @classmethod
    def edit_player(cls, player):
        return {
            "id": int(input(f"Enter new Id [{player.id}]: ")),
            "last_name": str(input(f"Enter new Last_name "
                                   f"[{player.last_name}]: ")),
            "first_name": str(input(f"Enter new First_name "
                                    f"[{player.first_name}]: ")),
            "birthday": input(f"Enter new date of birth 'DD.MM.YYYY'"
                              f" [{player.birthday}]: "),
            "gender": str(input(f"Enter new gender [{player.gender}]: ")),
            "rank": int(input(f"Enter new Rank [{player.rank}]: "))
        }

    @classmethod
    def select_list(cls, players):
        print('--------------------------------------------------------------')
        print("[                     Players                                ]")
        print('--------------------------------------------------------------')
        print("\tId\tFull_name\tBirthday\tGender\tRank")
        for player in players:
            cls.display_player(player)

        return [
            int(input("Enter player_one Id: ")),
            int(input("Enter player_two Id: ")),
            int(input("Enter player_three Id: ")),
            int(input("Enter player_four Id: ")),
            int(input("Enter player_five Id: ")),
            int(input("Enter player_six Id: ")),
            int(input("Enter player_seven Id: ")),
            int(input("Enter player_eight Id: "))
        ]

    @classmethod
    def display_player(cls, player):
        print(f"\t{player.id}\t{player.full_name()}\t{player.birthday}\t"
              f"{player.gender}\t{player.rank}")
