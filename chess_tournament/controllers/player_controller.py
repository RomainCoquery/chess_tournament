from chess_tournament.models.players import Player, PlayerManager
from chess_tournament.views.player_view import PlayerView


class PlayerController:

    @classmethod
    def list(cls, store, route_params=None):
        choice, player_id = PlayerView.display_list(store["players"])

        if choice == "1":
            return "view_player", player_id
        elif choice == "2":
            return "new_player", None
        elif choice == "3":
            return "edit_player", player_id
        elif choice.lower() == "4":
            store["players"] = sorted(store["players"],
                                      key=lambda p: p.last_name)
            return "list_player", None
        elif choice.lower() == "5":
            store["players"] = sorted(store["players"],
                                      key=lambda p: (int(p.rank)), reverse=True)
            return "list_player", None
        elif choice.lower() == "h":
            return "homepage", None
        elif choice.lower() == "q":
            return "quit", None
        else:
            raise Exception("invalid choice")

    @classmethod
    def create(cls, store, route_params=None):
        # call the view that will return us a dict with the new player info
        data = PlayerView.create_player()
        # You could specify each argument like:
        # player = Player(id=data["id"], name=data["name"], age=data["age"])
        # but it's easier to use `**` to pass the arguments
        player = Player(**data)
        if player.validate():
            print("Good, player add in the game!")
        else:
            print("Error, Data for player are not good!")
            return "list_player", None
        # we add the player to the store
        store["players"].append(player)
        PlayerManager().create_player(player)
        return "list_player", None

    @classmethod
    def view(cls, store, route_params):
        """
        Display one single player, the route_params correspond to the player ID
        we want to display
        """
        try:
            # search the player on the store
            player = next(p for p in store["players"]
                          if p.id == route_params)
            # we pass the player to the view that will display the player
            # info and the next options
            choice = PlayerView.view_player(player)
            if choice.lower() == "l":
                return "list_player", None
            elif choice.lower() == "h":
                return "homepage", None
            elif choice.lower() == "q":
                return "quit", None
        except StopIteration:
            print("No player with this id")
            return "list_player", None

    @classmethod
    def edit(cls, store, route_params):
        player = next(p for p in store["players"] if p.id == route_params)
        data = PlayerView.edit_player(player)
        player.edit(**data)
        PlayerManager().edit_player(player)
        return "list_player", None
