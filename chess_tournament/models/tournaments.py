from pathlib import Path
from tinydb import TinyDB, Query
from constants import NUMBER_OF_ROUNDS
from chess_tournament.models.rounds import Round
from chess_tournament.models.matchs import Match
from chess_tournament.models.players import Player, PlayerManager


class Tournament:
    """Tournament with is attributes tournament_name, location,
    creation_date, number_of_rounds, timer, description"""
    def __init__(self, name, location, creation_date, timer,
                 description):
        self.name = name
        self.location = location
        self.creation_date = creation_date
        self.number_of_rounds = NUMBER_OF_ROUNDS
        self.timer = timer or 'bullet' or 'blitz' or 'coup_rapide'
        self.description = description
        self.players = []
        self.rounds = []

    def add_tournament_player(self, player):
        """Add player in the tournament"""
        if isinstance(player, Player):
            self.players.append(player)

    def create_first_round(self):
        """Create first round and the matches from this one"""
        first_round = Round(name="Round1")
        players = sorted(self.players, key=lambda
            player: player.rank, reverse=False)
        length = len(players)
        middle_index = length // 2
        above = players[:middle_index]
        below = players[middle_index:]
        for player1, player2 in zip(above, below):
            player1.history.append(player2.id)
            player2.history.append(player1.id)
            first_round.add_match(Match(player1, player2))
        self.rounds.append(first_round)

    def start_other_round(self):
        """Create other round and the matches from this one"""
        new_round = Round(name="Round"+str(len(self.rounds)+1))
        players = sorted(self.players, key=lambda
            player: (float(player.score), int(player.rank)), reverse=True)
        locked_id = []
        missing_players = []
        for player in players:
            if player.id in locked_id:
                continue
            locked_id.append(player.id)
            for opponent in players:
                if opponent.id in locked_id or opponent.id in player.history:
                    continue
                locked_id.append(opponent.id)
                player.history.append(opponent.id)
                opponent.history.append(player.id)
                new_round.add_match(Match(player, opponent))
                break
            else:
                missing_players.append(player.id)
                locked_id.remove(player.id)
        for player in players:
            if player.id in missing_players:
                locked_id.append(player.id)
                missing_players.remove(player.id)
                for opponent in players:
                    if opponent.id in missing_players:
                        locked_id.append(opponent.id)
                        missing_players.remove(opponent.id)
                        new_round.add_match(Match(player, opponent))
        self.rounds.append(new_round)

    def validate(self):
        """validate input data by user"""
        return (
                isinstance(self.location, str) and
                isinstance(self.timer, str) and
                isinstance(self.description, str)
        )

    def edit(self, name, location, creation_date, timer,
             description):
        """edit a tournament by user"""
        self.name = name
        self.location = location
        self.creation_date = creation_date
        self.timer = timer or 'bullet' or 'blitz' or 'coup_rapide'
        self.description = description

    def serialized_tournament(self):
        return {
            'name': self.name,
            'location': self.location,
            'creation_date': self.creation_date,
            'timer': self.timer,
            'description': self.description,
            'players': [player.id for player in self.players],
            'rounds': [round.serialized_round() for round in self.rounds]
        }


class TournamentManager:
    def __init__(self):
        database_path = Path(__file__).parent / "database"
        db = TinyDB(database_path / 'db.json')
        self.tournaments_table = db.table('tournaments')

    def create_tournament(self, tournament):
        serialized_tournament = tournament.serialized_tournament()
        tournament_id = self.tournaments_table.insert(serialized_tournament)
        tournament.id = tournament_id

    def delete_all(self):
        self.tournaments_table.truncate()

    def get_all(self, store):
        import pdb; pdb.set_trace()
        players_ids = []
        all_tournaments = []
        serialized_tournaments = self.tournaments_table.all()
        for tournament_dict in serialized_tournaments:
            for id in tournament_dict['players']:
                for player in store["players"]:
                    if player.id == id:
                        players_ids.append(player)
            tournament= Tournament(
                            name=tournament_dict["name"],
                            location=tournament_dict["location"],
                            creation_date=tournament_dict["creation_date"],
                            timer=tournament_dict["timer"],
                            description=tournament_dict["description"],
                            )
            tournament.players = players_ids
            tournament.rounds = Round.get_all(store, tournament_dict["rounds"])
            all_tournaments.append(tournament)
        return all_tournaments

    def edit_tournament(self, tournament):
        serialized_tournament = tournament.serialized_tournament()
        q = Query()
        self.tournaments_table.update(serialized_tournament,
                                      q.name == tournament.name)
