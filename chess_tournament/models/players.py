from pathlib import Path
from tinydb import TinyDB, Query


class Player:
    """Player with is attributes id_player, last_name, first_name,
    birthday, gender, rank"""
    def __init__(self, id, last_name, first_name, birthday, gender, rank):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.rank = rank
        self.score = 0
        self.history = []

    def update_score(self, score):
        """update player score after match"""
        self.score = self.score + score

    def validate(self):
        return (
                isinstance(self.id, int) and
                isinstance(self.last_name, str) and
                isinstance(self.first_name, str) and
                isinstance(self.gender, str) and
                isinstance(self.rank, int)
        )

    def edit(self, id, last_name, first_name, birthday, gender, rank):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.rank = rank

    def full_name(self):
        """define the full name of player"""
        return f"{self.last_name} {self.first_name}"

    def serialized_player(self):
        return {
            'id': self.id,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birthday': self.birthday,
            'gender': self.gender,
            'rank': self.rank
        }


class PlayerManager:
    def __init__(self):
        database_path = Path(__file__).parent / "database"
        db = TinyDB(database_path / 'db.json')
        self.players_table = db.table('players')

    def create_player(self, player):
        serialized_player = player.serialized_player()
        player_id = self.players_table.insert(serialized_player)
        player.id = player_id

    def delete_all(self):
        self.players_table.truncate()

    def get_all(self):
        serialized_players = self.players_table.all()
        all_players = []
        for player_dict in serialized_players:
            player = Player(
                            id=player_dict["id"],
                            last_name=player_dict["last_name"],
                            first_name=player_dict["first_name"],
                            birthday=player_dict["birthday"],
                            gender=player_dict["gender"],
                            rank=player_dict["rank"]
                            )
            all_players.append(player)
        return all_players

    def edit_player(self, player):
        serialized_player = player.serialized_player()
        q = Query()
        self.players_table.update(serialized_player, q.id == player.id)
